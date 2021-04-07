
"""Workflow generator for ICCP code."""

import argparse
import json
import os
import re
import sys
import time
import yaml

parser = argparse.ArgumentParser(description='workflow generator')
parser.add_argument('--prefix', default='workflow1')
parser.add_argument('--sequence-dir', default='data')
parser.add_argument('--workdir', default='/home/jaket')
parser.add_argument('--db-name', default='databases/reference')
parser.add_argument('--ref-sequence', default='carAur01.sm.fa')
args = parser.parse_args()

# Hard-coded for now
PREFIX = args.prefix
SEQUENCE_DIR = args.sequence_dir
WORKDIR = args.workdir
DB_NAME = args.db_name
REF_SEQUENCE = args.ref_sequence

#WORKDIR = '/home/jaket'
#DB_NAME = 'databases/reference'
#REF_SEQUENCE = 'carAur01.sm.fa'

steps = {
    'makeblastdb': {
        'run': {
            'baseCommand': 'makeblastdb -in '
                           f'{REF_SEQUENCE} -title '
                           'reference -dbtype nucl -out '
                           'databases/reference',
            'class': 'CommandLineTool',
            'hints': {'DockerRequirement': {'dockerImageId': f'{WORKDIR}/blast.tar.gz'}},
            'inputs': {'sequence_file': {'type': 'string'}},
            'outputs': {'db_dir': {'type': 'string'}},
        },
        'in': {'sequence_file': 'sequence_file'},
        'out': ['db_dir'],
    },
}
extra_requirements = {
    'makeblastdb': {
        'workdir': WORKDIR,
        'push': [os.path.dirname(DB_NAME)],
        'pull': [REF_SEQUENCE],
    }
}

# Get the command line arguments
# PREFIX = sys.argv[1]
# seq_names = sys.argv[2:]

# Create a task for each file in the sequence directory
for seq_name in os.listdir(SEQUENCE_DIR):
    # Generate a task for each input argument
    task_name = 'task-{}'.format(re.sub(r'\W+', '-', seq_name))
    steps[task_name] = {
        'run': {
            'baseCommand': f'blastn -db {DB_NAME} '
                           f'-query {seq_name} -evalue '
                           '1e-3 -word_size 11 -outfmt 0 > '
                           f'{task_name}.reference',
            'class': 'CommandLineTool',
            'hints': {
                'DockerRequirement': {'dockerImageId': f'{WORKDIR}/blast.tar.gz'}
            },
            'inputs': {'db_dir': {'type': 'string'}},
            'outputs': {'out': {'type': 'string'}},
        },
        'in': {'db_dir': 'makeblastdb/db_dir'},
        'out': ['out'],
    }
    extra_requirements[task_name] = {
        'workdir': WORKDIR,
        'push': [f'{task_name}.reference'],
        'pull': [os.path.dirname(DB_NAME), seq_name],
    }

wfl = {
    'class': 'Workflow',
    'cwlVersion': 'v1.0',
    'inputs': {'sequence_file': 'File'},
    'outputs': [],
    'steps': steps,
}

# Write the workflow file
t = int(time.time())
with open(f'{PREFIX}.cwl', 'a') as fp:
    print('# -*- mode: YAML; -*-', file=fp)
    yaml.dump(wfl, fp)
# Write the extra requirements file
with open(f'{PREFIX}.json', 'w') as fp:
    json.dump(extra_requirements, fp, indent=4)
