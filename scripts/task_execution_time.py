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

# I print some metrics to stderr, so print the title so I can see which graph they're for
print('Title:', title, file=sys.stderr)

with open(args.workflow_profile) as fp:
    wfl = json.load(fp)

# Get all of the state changes for the tasks
tasks = set([sc['task_name'] for sc in wfl['state_changes']])

# Get the start time and end time of the workflow
start_time = min(sc['timestamp'] for sc in wfl['state_changes'])
end_time = max(sc['timestamp'] for sc in wfl['state_changes'])
total_time = end_time - start_time

# Print some metrics
print('Total run time:', total_time, file=sys.stderr)

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

# Set some values based on the input profile
left_label_width = max(len(name) * 10 for name in task_state_changes)

# Map task states to fills
# task_states = set(sc['next_state'] for sc in wfl['state_changes'])
# Only care about PENDING and RUNNING
task_states = set(['PENDING', 'RUNNING'])
# fill = svgtool.ScaleOrdinal(domain=task_states, range_=('#0000ff', '#000088', '#004488', '#008844'))
def fill(state):
    """Give a fill color for the state."""
    if state == 'RUNNING':
        return '#0000ff'
    elif state == 'PENDING':
        return '#ff0000'
    return '#000000'

# Create the bar rectangles
rects = []
left_labels = []
gridlines = []
for name in task_state_changes:
    states = task_state_changes[name]
    y = yscale.scale(name)
    bar_height = yscale.bandwidth
    # Add the task label
    left_labels.append(svgtool.text(name, x=10, y=y + bar_height / 2, style='font-size: 14pt;'))
    # Add bars for each state
    for i, sc in enumerate(states):
        # Determine the x and  y values
        x = xscale.scale(sc['timestamp'])
        next_time = (states[i + 1]['timestamp'] if i < (len(states) - 1)
                     else end_time)
        bar_width = xscale.scale(next_time) - x
        state = sc['next_state']
        if state not in task_states:
            # Ignore states we don't care about
            continue
        rects.append(
            svgtool.rect(
                x=x,
                y=y,
                width=bar_width,
                height=bar_height,
                fill=fill(state),
            )
        )
    # Add a line
    path = [
        svgtool.path_move_to(0, y - 6),
        svgtool.path_line_to(left_label_width + graph_width, y - 6),
    ]
    gridlines.append(svgtool.path(path, 'stroke: #000000; stroke-width: 1px;'))

# Determine the average PENDING time
pending_times = [task_state_changes[name][i + 1]['timestamp'] - sc['timestamp']
                 for name in task_state_changes
                 for i, sc in enumerate(task_state_changes[name])
                 # for i, sc in enumerate(states)
                 if sc['next_state'] == 'PENDING' and i < (len(task_state_changes[name]) - 1)]
average_pending_time = sum(pending_times) / len(pending_times)
print('Average pending time:', average_pending_time, file=sys.stderr)

# Add a vertical gridline
vertical_path = [
    svgtool.path_move_to(left_label_width, 0),
    svgtool.path_line_to(left_label_width, max(yscale.scale(name)
                                               + yscale.bandwidth
                                               for name in task_state_changes) + 10)
]
gridlines.append(svgtool.path(vertical_path, 'stroke: #000000; stroke-width: 1px;'))

# Create a title
title = svgtool.text(title, x=width / 4, y=30, style='font-size:20pt;')

# Create a key
key = []
task_states = list(task_states)
task_states.sort()
x = 0
for i, state in enumerate(task_states):
    key.append(svgtool.text(state, x=x, y=28, style='font-size: 15pt;'))
    x += len(state) * 14
    key.append(svgtool.rect(x=x, y=0, width=40, height=40, fill=fill(state)))
    x += 60
key = svgtool.g(transform='translate(200 %i)' % (graph_height + 120,), content=key)

# Create the axis and title
axis = [
    xscale.axis_horizontal(tick_count=10, label=lambda tick_val: '%i' % (tick_val - start_time,),
                           text_style='font-size: 15pt;'),
    svgtool.text('Execution time (s)',
                 x=xscale.scale(start_time + total_time / 3), y=50,
                 style='font-size: 18pt;'),
]
axis = svgtool.g(transform='translate(0 %i)' % (graph_height,), content=axis)

# Create the final graph content
rects_axis = []
rects_axis.extend(rects)
rects_axis.append(axis)
# Slide the bars over to make room for the left labels
rects = svgtool.g(transform='translate(%i 0)' % (left_label_width,), content=rects_axis)
# Add in the left labels
left_labels = ''.join(left_labels)
# Add in the grid lines
gridlines = ''.join(gridlines)
# Create the content
content = svgtool.g(transform='translate(0 50)', content=[left_labels, gridlines, rects])
content = svgtool.g(content=[title, key, content])

print(svgtool.svg(width=width, height=height, content=content))
