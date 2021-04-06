"""Output a graph of the node execution times."""

import json
import sys

import svgtool

if len(sys.argv) != 2:
    print('Usage: %s [WORKFLOW PROFILE]' % (sys.argv[0],), file=sys.stderr)
    sys.exit(1)

with open(sys.argv[1]) as fp:
    wfl = json.load(fp)
#print(wfl['scheduling_results'])

width = 1200
height = 400
graph_width = 800
graph_height = 200
outer_padding = 20

xscale = svgtool.ScaleBand(
    # domain=(0, len(wfl['scheduling_results'])),
    domain=list(range(0, len(wfl['scheduling_results']))),
    range_=(20, graph_width),
    padding=100,
)

# Get all the resource / node names
# Map from ids to the Task Manager systems
resource_name_map = {
    'localhost:5055': 'Google Compute Engine',
    'localhost:6700': 'Chameleoncloud',
}

def allocation_to_name(id_, node):
    """Return a name for the allocation id_ and node."""
    return '%s -- node-%i' % (resource_name_map[id_], node)

resource_names = set(
    allocation_to_name(resource['id_'], node)
    for result in wfl['scheduling_results']
    for resource in result['resources']
    for node in range(resource['nodes'])
)

yscale = svgtool.ScaleBand(
    domain=resource_names,
    range_=(outer_padding, graph_height - outer_padding),
    padding=10,
)

start_time = min(sc['timestamp'] for sc in wfl['state_changes'])
end_time = max(sc['timestamp'] for sc in wfl['state_changes'])
total_time = end_time - start_time

xscale = svgtool.ScaleLinear(domain=(start_time, end_time), range_=(20, graph_width))

task_id_name_table = {
    sc['task_id']: sc['task_name'] for sc in wfl['state_changes']
}
allocations = {
    task_id_name_table[id_]: result['allocations'][id_]
    for result in wfl['scheduling_results']
    for id_ in result['allocations']
}

# Map from task name to colors
fill = svgtool.ScaleOrdinal(
    domain=[task_name for task_name in allocations],
    range_=('#000033', '#000088', '#0000CC'),
)

# Add a rectangle for each task
rects = []
for task_name in allocations:
    # Get the running task start and end times
    task_start_time = [
        sc['timestamp']
        for sc in wfl['state_changes']
        if sc['next_state'] == 'RUNNING' and sc['task_name'] == task_name
    ]
    task_start_time = task_start_time[0]
    task_end_time = [
        sc['timestamp']
        for sc in wfl['state_changes']
        if sc['next_state'] == 'COMPLETED' and sc['task_name'] == task_name
    ]
    task_end_time = task_end_time[0]
    # Add a rectangle for each allocation
    for alloc in allocations[task_name]:
        for node in range(alloc['nodes']):
            x = xscale.scale(task_start_time)
            y = yscale.scale(allocation_to_name(alloc['id_'], node))
            rect_width = xscale.scale(task_end_time) - xscale.scale(task_start_time)
            rect_height = yscale.bandwidth
            rect = svgtool.rect(
                x=x,
                y=y,
                width=rect_width,
                height=rect_height,
                fill=fill.scale(task_name)
            )
            rects.append(rect)
            label_x = x + rect_width / 3
            label_y = y + rect_height / 1.8
            # Also add the task name label
            label = svgtool.text(task_name, x=label_x, y=label_y, style='font-size:14pt;fill:#FFFFFF;')
            rects.append(label)
content = list(rects)
content.append(svgtool.g(
    transform='translate(0 %i)' % (graph_height,),
    content=xscale.axis_horizontal(
        tick_count=12,
        label=lambda tick_val: '%is' % (tick_val - start_time,),
    )
))
# Add in the axis and labels
content = [
    svgtool.text('Nodes', x=100, y=0),
    yscale.axis_vertical(text_style='font-weight:bold;'),
    svgtool.g(transform='translate(250 0)', content=content),
]
content = svgtool.g(transform='translate(10 80)', content=content)
# Add in the title
content = [
    content,
    svgtool.text('Task Node Execution', x=width / 3, y=40, style='font-size:20pt;'),
]
print(svgtool.svg(width=width, height=height, content=content))
