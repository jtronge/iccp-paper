# -*- mode: YAML; -*-
# Generated on 2021-04-08
class: Workflow
cwlVersion: v1.0
inputs:
  NC_009057-fasta: File
  NC_009058-fasta: File
  NC_009059-fasta: File
  NC_009060-fasta: File
  NC_009062-fasta: File
  NC_009063-fasta: File
  NC_009064-fasta: File
  NC_009065-fasta: File
  NC_009066-fasta: File
  NC_009067-fasta: File
  NC_009459-fasta: File
  NC_010205-fasta: File
  NC_011168-fasta: File
  NC_011169-fasta: File
  NC_011170-fasta: File
  NC_011171-fasta: File
  NC_011177-fasta: File
  NC_011179-fasta: File
  NC_012055-fasta: File
  NC_013564-fasta: File
  NC_013577-fasta: File
  NC_013663-fasta: File
  NC_013750-fasta: File
  NC_018814-fasta: File
  NC_018815-fasta: File
  sequence_file: File
outputs: []
steps:
  makeblastdb:
    in:
      sequence_file: sequence_file
    out:
    - db_dir
    run:
      baseCommand:
      - makeblastdb
      - -title
      - reference
      - -dbtype
      - nucl
      - -out
      - databases/reference
      class: CommandLineTool
      hints:
        DockerRequirement:
          dockerPull: ncbi/blast
      inputs:
        sequence_file:
          inputBinding:
            prefix: -in
          type: File
      outputs:
        db_dir:
          outputBinding:
            glob: databases
          type: File
  task-NC_009057-fasta:
    in:
      db_dir: makeblastdb/db_dir
      out_file: NC_009057-fasta.reference
      seq_file: NC_009057-fasta
    out:
    - out
    run: blast-cloud_2021-04-08_tool.yml
  task-NC_009058-fasta:
    in:
      db_dir: makeblastdb/db_dir
      out_file: NC_009058-fasta.reference
      seq_file: NC_009058-fasta
    out:
    - out
    run: blast-cloud_2021-04-08_tool.yml
  task-NC_009059-fasta:
    in:
      db_dir: makeblastdb/db_dir
      out_file: NC_009059-fasta.reference
      seq_file: NC_009059-fasta
    out:
    - out
    run: blast-cloud_2021-04-08_tool.yml
  task-NC_009060-fasta:
    in:
      db_dir: makeblastdb/db_dir
      out_file: NC_009060-fasta.reference
      seq_file: NC_009060-fasta
    out:
    - out
    run: blast-cloud_2021-04-08_tool.yml
  task-NC_009062-fasta:
    in:
      db_dir: makeblastdb/db_dir
      out_file: NC_009062-fasta.reference
      seq_file: NC_009062-fasta
    out:
    - out
    run: blast-cloud_2021-04-08_tool.yml
  task-NC_009063-fasta:
    in:
      db_dir: makeblastdb/db_dir
      out_file: NC_009063-fasta.reference
      seq_file: NC_009063-fasta
    out:
    - out
    run: blast-cloud_2021-04-08_tool.yml
  task-NC_009064-fasta:
    in:
      db_dir: makeblastdb/db_dir
      out_file: NC_009064-fasta.reference
      seq_file: NC_009064-fasta
    out:
    - out
    run: blast-cloud_2021-04-08_tool.yml
  task-NC_009065-fasta:
    in:
      db_dir: makeblastdb/db_dir
      out_file: NC_009065-fasta.reference
      seq_file: NC_009065-fasta
    out:
    - out
    run: blast-cloud_2021-04-08_tool.yml
  task-NC_009066-fasta:
    in:
      db_dir: makeblastdb/db_dir
      out_file: NC_009066-fasta.reference
      seq_file: NC_009066-fasta
    out:
    - out
    run: blast-cloud_2021-04-08_tool.yml
  task-NC_009067-fasta:
    in:
      db_dir: makeblastdb/db_dir
      out_file: NC_009067-fasta.reference
      seq_file: NC_009067-fasta
    out:
    - out
    run: blast-cloud_2021-04-08_tool.yml
  task-NC_009459-fasta:
    in:
      db_dir: makeblastdb/db_dir
      out_file: NC_009459-fasta.reference
      seq_file: NC_009459-fasta
    out:
    - out
    run: blast-cloud_2021-04-08_tool.yml
  task-NC_010205-fasta:
    in:
      db_dir: makeblastdb/db_dir
      out_file: NC_010205-fasta.reference
      seq_file: NC_010205-fasta
    out:
    - out
    run: blast-cloud_2021-04-08_tool.yml
  task-NC_011168-fasta:
    in:
      db_dir: makeblastdb/db_dir
      out_file: NC_011168-fasta.reference
      seq_file: NC_011168-fasta
    out:
    - out
    run: blast-cloud_2021-04-08_tool.yml
  task-NC_011169-fasta:
    in:
      db_dir: makeblastdb/db_dir
      out_file: NC_011169-fasta.reference
      seq_file: NC_011169-fasta
    out:
    - out
    run: blast-cloud_2021-04-08_tool.yml
  task-NC_011170-fasta:
    in:
      db_dir: makeblastdb/db_dir
      out_file: NC_011170-fasta.reference
      seq_file: NC_011170-fasta
    out:
    - out
    run: blast-cloud_2021-04-08_tool.yml
  task-NC_011171-fasta:
    in:
      db_dir: makeblastdb/db_dir
      out_file: NC_011171-fasta.reference
      seq_file: NC_011171-fasta
    out:
    - out
    run: blast-cloud_2021-04-08_tool.yml
  task-NC_011177-fasta:
    in:
      db_dir: makeblastdb/db_dir
      out_file: NC_011177-fasta.reference
      seq_file: NC_011177-fasta
    out:
    - out
    run: blast-cloud_2021-04-08_tool.yml
  task-NC_011179-fasta:
    in:
      db_dir: makeblastdb/db_dir
      out_file: NC_011179-fasta.reference
      seq_file: NC_011179-fasta
    out:
    - out
    run: blast-cloud_2021-04-08_tool.yml
  task-NC_012055-fasta:
    in:
      db_dir: makeblastdb/db_dir
      out_file: NC_012055-fasta.reference
      seq_file: NC_012055-fasta
    out:
    - out
    run: blast-cloud_2021-04-08_tool.yml
  task-NC_013564-fasta:
    in:
      db_dir: makeblastdb/db_dir
      out_file: NC_013564-fasta.reference
      seq_file: NC_013564-fasta
    out:
    - out
    run: blast-cloud_2021-04-08_tool.yml
  task-NC_013577-fasta:
    in:
      db_dir: makeblastdb/db_dir
      out_file: NC_013577-fasta.reference
      seq_file: NC_013577-fasta
    out:
    - out
    run: blast-cloud_2021-04-08_tool.yml
  task-NC_013663-fasta:
    in:
      db_dir: makeblastdb/db_dir
      out_file: NC_013663-fasta.reference
      seq_file: NC_013663-fasta
    out:
    - out
    run: blast-cloud_2021-04-08_tool.yml
  task-NC_013750-fasta:
    in:
      db_dir: makeblastdb/db_dir
      out_file: NC_013750-fasta.reference
      seq_file: NC_013750-fasta
    out:
    - out
    run: blast-cloud_2021-04-08_tool.yml
  task-NC_018814-fasta:
    in:
      db_dir: makeblastdb/db_dir
      out_file: NC_018814-fasta.reference
      seq_file: NC_018814-fasta
    out:
    - out
    run: blast-cloud_2021-04-08_tool.yml
  task-NC_018815-fasta:
    in:
      db_dir: makeblastdb/db_dir
      out_file: NC_018815-fasta.reference
      seq_file: NC_018815-fasta
    out:
    - out
    run: blast-cloud_2021-04-08_tool.yml
