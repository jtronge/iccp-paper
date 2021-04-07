"""Generate a graph of the results."""
import argparse
import json
import sys

import svgtool

parser = argparse.ArgumentParser()
parser.add_argument('workflow_profile', help='workflow profile file')
parser.add_argument('--width', type=int, default=800, help='full width')
parser.add_argument('--height', type=int, default=500, help='full height')
parser.add_argument('--graph-width', type=int, default=600, help='graph/diagram width')
parser.add_argument('--graph-height', type=int, default=200, help='graph/diagram height')
parser.add_argument('--title', default='Blast Workflow 1 Task Execution Time',
                    help='graph title')
args = parser.parse_args()

title = args.title
width = args.width
height = args.height
graph_width = args.graph_width
graph_height = args.graph_height

#if len(sys.argv) != 2:
#    print('Usage: %s [WORKFLOW PROFILE]' % (sys.argv[0],), file=sys.stderr)
#    sys.exit(1)

# Read in the workflow profile
#with open(sys.argv[1]) as fp:
#    wfl = json.load(fp)
with open(args.workflow_profile) as fp:
    wfl = json.load(fp)

# Get all of the state changes for the tasks
tasks = set([sc['task_name'] for sc in wfl['state_changes']])

# Get the start time and end time of the workflow
start_time = min(sc['timestamp'] for sc in wfl['state_changes'])
end_time = max(sc['timestamp'] for sc in wfl['state_changes'])
total_time = end_time - start_time

#width = 800
#height = 500
#graph_width = 600
#graph_height = 200
left_padding = 10
right_padding = 10
top_padding = 10
bottom_padding = 10

xscale = svgtool.ScaleLinear(domain=(start_time, end_time),
                             range_=(left_padding, graph_width - left_padding - right_padding))
yscale = svgtool.ScaleBand(domain=tasks, range_=(top_padding, graph_height - bottom_padding))

# Build a dict from task_name to a list of sorted state_changes
task_state_changes = {}
for sc in wfl['state_changes']:
    name = sc['task_name']
    if name in task_state_changes:
        task_state_changes[name].append(sc)
    else:
        task_state_changes[name] = [sc]
# Sort each by timestamp
for name in task_state_changes:
    task_state_changes[name].sort(key=lambda sc: sc['timestamp'])

# Map task states to fills
task_states = list(set(sc['next_state'] for sc in wfl['state_changes']))
fill = svgtool.ScaleOrdinal(domain=task_states, range_=('#ff0000', '#0000ff'))

# Create the bar rectangles
rects = []
left_labels = []
for name in task_state_changes:
    states = task_state_changes[name]
    y = yscale.scale(name)
    bar_height = yscale.bandwidth
    # Add the task label
    left_labels.append(svgtool.text(name, x=10, y=y + bar_height / 2))
    # Add bars for each state
    for i, sc in enumerate(states):
        # Determine the x and  y values
        x = xscale.scale(sc['timestamp'])
        next_time = (states[i + 1]['timestamp'] if i < (len(states) - 1)
                     else end_time)
        bar_width = xscale.scale(next_time) - x
        state = sc['next_state']
        if state == 'COMPLETED':
            # Don't do anything here
            continue
        rects.append(
            svgtool.rect(
                x=x,
                y=y,
                width=bar_width,
                height=bar_height,
                fill=fill.scale(state),
            )
        )

# Create a title
title = svgtool.text(title, x=width / 4, y=30, style='font-size:20pt;')

# Create a key
key = []
task_states = list(task_states)
task_states.sort()
task_states.remove('COMPLETED')
for i, state in enumerate(task_states):
    x = i * 150
    key.append(svgtool.text(state, x=x, y=20))
    key.append(svgtool.rect(x=x + len(state) * 12, y=0, width=40, height=40, fill=fill.scale(state)))
key = svgtool.g(transform='translate(120 %i)' % (graph_height + 120,), content=key)

# Create the axis and title
axis = [
    xscale.axis_horizontal(tick_count=10, label=lambda tick_val: '%i' % (tick_val - start_time,)),
    svgtool.text('Execution time (s)', x=xscale.scale(start_time + total_time / 3), y=40),
]
axis = svgtool.g(transform='translate(0 %i)' % (graph_height,), content=axis)

# Create the final graph content
rects_axis = []
rects_axis.extend(rects)
rects_axis.append(axis)
# Slide the bars over to make room for the left labels
left_label_width = max(len(name) * 10 for name in task_state_changes)
rects = svgtool.g(transform='translate(%i 0)' % (left_label_width,), content=rects_axis)
# Add in the left labels
left_labels = ''.join(left_labels)
content = svgtool.g(transform='translate(0 50)', content=[left_labels, rects])
content = svgtool.g(content=[title, key, content])

print(svgtool.svg(width=width, height=height, content=content))
