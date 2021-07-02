"""Create a run graph of a workflow profile."""
import json
import argparse

import svgtool

parser = argparse.ArgumentParser(description='create a workflow run graph')
parser.add_argument('profiles', nargs='*', help='JSON workflow profile')
parser.add_argument('--width', default=1000, type=int, help='width of graph')
parser.add_argument('--height', default=800, type=int, help='height of graph')
parser.add_argument('--padding', default=100, type=int, help='height of graph')
parser.add_argument('--title', default='Workflow Comparison: Single Cloud vs Multi-Cloud', help='title of graph')
args = parser.parse_args()

profiles = args.profiles
width = args.width
graph_width = 2 * width / 3
height = args.height
horizontal_padding = args.padding
vertical_padding = args.padding
title = args.title

def err(*pargs):
    """Print arguments to stderr."""
    import sys
    print(*pargs, file=sys.stderr)

def load_profile(profile):
    """Load a workflow profile and return the attributes."""
    # Load the profile
    with open(profile) as fp:
        wfl = json.load(fp)

    # Get a list of all task names and a dict from task names to ids
    task_names = []
    task_to_ids = {}
    for sc in wfl['state_changes']:
        if sc['task_name'] not in task_names:
            task_names.append(sc['task_name'])
            task_to_ids[sc['task_name']] = sc['task_id']
    err('Task Names', task_names)

    # Get the start and end times of each task
    task_start_times = {}
    task_end_times = {}
    for sc in wfl['state_changes']:
        task_name = sc['task_name']
        if sc['next_state'] == 'RUNNING':
            task_start_times[task_name] = sc['timestamp']
        elif sc['next_state'] == 'COMPLETED':
            task_end_times[task_name] = sc['timestamp']
    err('Task Start Times', task_start_times)

    # Get a list of all state change timestamps
    times = [sc['timestamp'] for sc in wfl['state_changes']]
    start_time = min(times)
    end_time = max(times)

    total_minutes = (end_time - start_time) / 60.0
    # Get a dict from resource IDs to names
    resource_ids_to_names = {resource_id: result['resource_ids'][resource_id] for result in wfl['scheduling_results'] for resource_id in result['resource_ids']}

    # Get a dict from task ID to allocations
    task_to_allocations = {task_name: result['allocations'][alloc] for task_name in task_names for result in wfl['scheduling_results'] for alloc in result['allocations'] if alloc == task_to_ids[task_name]}

    tasks = {
        task_name: {
            'task_id': task_to_ids[task_name],
            'start_time': task_start_times[task_name],
            'end_time': task_end_times[task_name],
            'allocation_id': task_to_allocations[task_name][0]['id_'],
        } for task_name in task_names
    }
    return start_time, end_time, tasks, resource_ids_to_names

# Load all workflow profiles
wfls = []
max_time = None
for profile in profiles:
    start_time, end_time, tasks, resource_ids_to_names = load_profile(profile)
    wfls.append({
        'start_time': start_time,
        'end_time': end_time,
        'tasks': tasks,
        'resource_ids_to_names': resource_ids_to_names,
    })
    total_time = end_time - start_time
    if max_time is None or total_time > max_time:
        max_time = total_time


xscale = svgtool.ScaleLinear(domain=(0, max_time), range_=(horizontal_padding, graph_width - horizontal_padding))
x_start = xscale.scale(0)
x_end = xscale.scale(max_time)

translate_x = 180

# Create rectangles representing the runtime of each task for each workflow
content = []
y_pos = 0
for i, wfl in enumerate(wfls):
    start_time = wfl['start_time']
    end_time = wfl['end_time']
    resource_ids = wfl['resource_ids_to_names']
    yscale = svgtool.ScaleBand(domain=resource_ids, range_=(y_pos, y_pos + len(resource_ids) * 32))
    rects = []
    for task_name in wfl['tasks']:
        task = wfl['tasks'][task_name]
        st = task['start_time'] - start_time
        t = task['end_time'] - task['start_time']
        # Set the rectangle values
        x = xscale.scale(st)
        y = yscale.scale(task['allocation_id'])
        rect_width = xscale.scale(st + t) - x
        rect_height = 24
        rects.append(svgtool.rect(x=x, y=y, width=rect_width, height=rect_height))

    # Increment the y position
    y_pos += len(resource_ids) * 32
    # Append the total time
    rects.append(svgtool.text('%0.2fs in total' % (wfl['end_time'] - wfl['start_time'],), x=xscale.scale(end_time - start_time), y=y_pos - len(resource_ids) * 16, style='font-size:16pt;'))
    wfl_content = [svgtool.g(transform=svgtool.translate(translate_x, 0), content=rects)]
    wfl_content.append(svgtool.text('Run %i' % (i,), x=0, y=y_pos - len(resource_ids) * 16, style='font-weight:bold;font-size:20pt;'))

    # Add the resource labels
    resource_labels = []
    for id_ in resource_ids:
        name = resource_ids[id_]
        resource_labels.append(svgtool.text(name, x=x_start - 10, y=yscale.scale(id_) + yscale.bandwidth * 0.9, style='font-size:16pt;text-anchor:end;'))
    wfl_content.append(svgtool.g(transform=svgtool.translate(translate_x, 0), content=resource_labels))
    wfl_content.append(svgtool.path(d=[svgtool.path_move_to(0, y_pos - 6), svgtool.path_line_to(x_end + translate_x, y_pos - 6)], style='stroke: #000000; stroke-width: 1px;'))

    g = svgtool.g(transform=svgtool.translate(20, 20), content=wfl_content)
    # Add a lower bar
    content.append(g)

# Add a title
content = [svgtool.g(transform=svgtool.translate(0, 40), content=content)]
content.append(svgtool.text(title, x=(graph_width + translate_x) / 2.0, y=30, style='font-size:30pt;text-anchor:middle;'))
print(svgtool.svg(width=width, height=height, content=content))
