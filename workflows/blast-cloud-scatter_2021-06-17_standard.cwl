# -*- mode: YAML; -*-
# Generated on 2021-06-17
class: Workflow
cwlVersion: v1.0
inputs: {db_title: string, sequence_file: File, sequence_queries: 'File[]'}
outputs: []
requirements:
  InlineJavascriptRequirement: {}
  ScatterFeatureRequirement: {}
steps:
  makeblastdb:
    in: {db_title: db_title, sequence_file: sequence_file}
    out: [db_dir]
    run:
      arguments:
      - {prefix: -out, valueFrom: $("databases/" + inputs.db_title)}
      baseCommand: [makeblastdb, -dbtype, nucl]
      class: CommandLineTool
      hints:
        DockerRequirement: {dockerPull: ncbi/blast}
      inputs:
        db_title:
          inputBinding: {prefix: -title}
          type: string
        sequence_file:
          inputBinding: {prefix: -in}
          type: File
      outputs:
        db_dir:
          outputBinding: {glob: databases}
          type: Directory
      requirements:
        ResourceRequirement: {tmpdirMin: '10000'}
  sequence:
    in: {db_dir: makeblastdb/db_dir, db_title: db_title, seq_file: sequence_queries}
    out: [out]
    run:
      baseCommand: [blastn, -evalue, '1e-3', -word_size, '11', -outfmt, '0']
      class: CommandLineTool
      hints:
        DockerRequirement: {dockerPull: ncbi/blast}
      inputs:
        db_dir:
          inputBinding: {prefix: -db, valueFrom: $(inputs.db_dir.path + "/" + inputs.db_title)}
          type: Directory
        db_title: {type: string}
        seq_file:
          inputBinding: {prefix: -query}
          type: File
      outputs:
        out: {type: stdout}
      requirements:
        ResourceRequirement: {tmpdirMin: '10000'}
      stdout: $(inputs.seq_file.basename + ".reference")
    scatter: seq_file
