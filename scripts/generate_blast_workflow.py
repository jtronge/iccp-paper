
"""Workflow generator for ICCP code."""

import argparse
import datetime
import json
import os
import re
import sys
import time
import yaml

parser = argparse.ArgumentParser(description='workflow generator')
parser.add_argument('--output-dir', default='workflows')
parser.add_argument('--prefix', default='workflow1')
parser.add_argument('--sequence-dir', default='data')
parser.add_argument('--workdir', default='/home/jaket')
parser.add_argument('--db-name', default='databases/reference')
parser.add_argument('--ref-sequence', default='carAur01.sm.fa')
parser.add_argument('--docker-ctr', default='ncbi/blast',
                    help='Docker container tag')
parser.add_argument('--ch-ctr', default='/home/cc/blast.tar.gz',
                    help='Charliecloud container image')
args = parser.parse_args()

OUTPUT_DIR = args.output_dir
PREFIX = args.prefix
SEQUENCE_DIR = args.sequence_dir
WORKDIR = args.workdir
DB_NAME = args.db_name
REF_SEQUENCE = args.ref_sequence
DOCKER_CTR = args.docker_ctr
CH_CTR = args.ch_ctr

# Steps for a standard CWL workflow
# This corresponds to the YAML input file to the standard CWL
inputs_file = {
    'sequence_file': {
        'class': 'File',
        'path': REF_SEQUENCE,
    }
}
# The inputs field of the CWL file
inputs = {
    'sequence_file': 'File',
}
# The steps of the CWL file
steps = {
    'makeblastdb': {
        'run': {
            'baseCommand': [
                'makeblastdb',
                '-title',
                'reference',
                '-dbtype',
                'nucl',
                '-out',
                'databases/reference',
            ],
            'class': 'CommandLineTool',
            'hints': {
                'DockerRequirement': {
                    'dockerPull': DOCKER_CTR,
                },
            },
            'inputs': {
                'sequence_file': {
                    'type': 'File',
                    'inputBinding': {
                        'prefix': '-in',
                    },
                },
            },
            'outputs': {
                'db_dir': {
                    # TODO: Should type be a Directory?
                    'type': 'File',
                    'outputBinding': {
                        'glob': 'databases',
                    },
                },
            },
        },
        'in': {'sequence_file': 'sequence_file'},
        'out': ['db_dir'],
    },
}
tool = {
    'cwlVersion': 'v1.0',
    'class': 'CommandLineTool',
    'baseCommand': 'blastn -evalue 1e-3 -word_size 11 -outfmt 0',
    'class': 'CommandLineTool',
    'hints': {
        'DockerRequirement': {
            'dockerPull': DOCKER_CTR,
        },
    },
    'inputs': {
        'db_dir': {
            'type': 'File',
            'inputBinding': {
                'prefix': '-db',
            },
        },
        'seq_file': {
            'type': 'File',
            'inputBinding': {
                'prefix': '-query',
            },
        },
        'out_file': {
            'type': 'str',
        },
    },
    'outputs': {
    # Capture stdout
        'out': {'type': 'stdout'},
    },
    # Save stdout to this file
    #'stdout': stdout_file,
    'stdout': {
        'valueFrom': '$(inputs.out_file)'
    }
}

# Steps for BEE CWL
bee_steps = {
    'makeblastdb': {
        'run': {
            'baseCommand': 'makeblastdb -in '
                           f'{os.path.basename(REF_SEQUENCE)} -title '
                           'reference -dbtype nucl -out '
                           'databases/reference',
            'class': 'CommandLineTool',
            'hints': {'DockerRequirement': {'dockerImageId': CH_CTR}},
            'inputs': {'sequence_file': {'type': 'string'}},
            'outputs': {'db_dir': {'type': 'string'}},
        },
        'in': {'sequence_file': 'sequence_file'},
        'out': ['db_dir'],
    },
}
# Extra BEE requirements
extra_requirements = {
    'makeblastdb': {
        'workdir': WORKDIR,
        'push': [os.path.dirname(DB_NAME)],
        'pull': [os.path.basename(REF_SEQUENCE)],
    }
}

# Save files with a date string
date_str = datetime.datetime.now().strftime('%F')
tool_fname = f'{PREFIX}_{date_str}_tool.yml'

# Create a task for each file in the sequence directory
for seq_path in os.listdir(SEQUENCE_DIR):
    # Generate a task for each input argument
    seq_file = re.sub(r'\W+', '-', seq_path)
    task_name = 'task-{}'.format(re.sub(r'\W+', '-', seq_path))
    stdout_file = f'{seq_file}.reference'
    # Add an input to the YAML input file
    inputs_file[seq_file] = {
        'class': 'File',
        # Add in the relative path so it can be run the repository root
        'path': os.path.join(SEQUENCE_DIR, seq_path),
    }
    # Add an input for the workflow
    inputs[seq_file] = 'File'
    # Add a step for the real CWL workflow
    steps[task_name] = {
        'run': tool_fname,
        'in': {
            'db_dir': 'makeblastdb/db_dir',
            'seq_file': seq_file,
            'out_file': stdout_file,
        },
        'out': ['out'],
    }
    # Add a step for the BEE CWL Workflow
    bee_steps[task_name] = {
        'run': {
            'baseCommand': f'blastn -db {DB_NAME} '
                           f'-query {seq_path} -evalue '
                           '1e-3 -word_size 11 -outfmt 0 > '
                           f'{task_name}.reference',
            'class': 'CommandLineTool',
            'hints': {
                'DockerRequirement': {'dockerImageId': CH_CTR}
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
        'pull': [os.path.dirname(DB_NAME), seq_path],
    }

# Write out the tool definition
with open(os.path.join(OUTPUT_DIR, tool_fname), 'w') as fp:
    print('# Generated on', date_str, file=fp)
    yaml.dump(tool, fp)
# The CWL workflow
cwl_wfl = {
    'class': 'Workflow',
    'cwlVersion': 'v1.0',
    'inputs': inputs,
    'outputs': [],
    'steps': steps,
}
# Write the input YAML file
fname = f'{PREFIX}_{date_str}_inputs.yml'
with open(os.path.join(OUTPUT_DIR, fname), 'w') as fp:
    print('# Generated on', date_str, file=fp)
    yaml.dump(inputs_file, fp)
# Write the real CWL file
fname = f'{PREFIX}_{date_str}_standard.cwl'
with open(os.path.join(OUTPUT_DIR, fname), 'w') as fp:
    print('# -*- mode: YAML; -*-', file=fp)
    print('# Generated on', date_str, file=fp)
    yaml.dump(cwl_wfl, fp)
# The BEE Workflow
bee_wfl = {
    'class': 'Workflow',
    'cwlVersion': 'v1.0',
    'inputs': {'sequence_file': 'File'},
    'outputs': [],
    'steps': bee_steps,
}
# Write the BEE workflow file
fname = f'{PREFIX}_{date_str}_bee.cwl'
with open(os.path.join(OUTPUT_DIR, fname), 'w') as fp:
    print('# -*- mode: YAML; -*-', file=fp)
    print('# Generated on', date_str, file=fp)
    yaml.dump(bee_wfl, fp)
# Write the extra requirements file
fname = f'{PREFIX}_{date_str}_bee.json'
with open(os.path.join(OUTPUT_DIR, fname), 'w') as fp:
    json.dump(extra_requirements, fp, indent=4)
