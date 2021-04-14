# -*- mode: YAML; -*-
# Generated on 2021-04-14
class: Workflow
cwlVersion: v1.0
inputs: {sequence_file: File}
outputs: []
steps:
  makeblastdb:
    in: {sequence_file: sequence_file}
    out: [db_dir]
    run:
      baseCommand: makeblastdb -in carAur01.sm.fa -title reference -dbtype nucl -out
        databases/reference
      class: CommandLineTool
      hints:
        DockerRequirement: {dockerImageId: /home/cc/blast.tar.gz}
      inputs:
        sequence_file: {type: string}
      outputs:
        db_dir: {type: string}
  task-NC_009057-fasta:
    in: {db_dir: makeblastdb/db_dir}
    out: [out]
    run:
      baseCommand: blastn -db databases/reference -query NC_009057.fasta -evalue 1e-3
        -word_size 11 -outfmt 0 > task-NC_009057-fasta.reference
      class: CommandLineTool
      hints:
        DockerRequirement: {dockerImageId: /home/cc/blast.tar.gz}
      inputs:
        db_dir: {type: string}
      outputs:
        out: {type: string}
  task-NC_009058-fasta:
    in: {db_dir: makeblastdb/db_dir}
    out: [out]
    run:
      baseCommand: blastn -db databases/reference -query NC_009058.fasta -evalue 1e-3
        -word_size 11 -outfmt 0 > task-NC_009058-fasta.reference
      class: CommandLineTool
      hints:
        DockerRequirement: {dockerImageId: /home/cc/blast.tar.gz}
      inputs:
        db_dir: {type: string}
      outputs:
        out: {type: string}
  task-NC_009059-fasta:
    in: {db_dir: makeblastdb/db_dir}
    out: [out]
    run:
      baseCommand: blastn -db databases/reference -query NC_009059.fasta -evalue 1e-3
        -word_size 11 -outfmt 0 > task-NC_009059-fasta.reference
      class: CommandLineTool
      hints:
        DockerRequirement: {dockerImageId: /home/cc/blast.tar.gz}
      inputs:
        db_dir: {type: string}
      outputs:
        out: {type: string}
  task-NC_009060-fasta:
    in: {db_dir: makeblastdb/db_dir}
    out: [out]
    run:
      baseCommand: blastn -db databases/reference -query NC_009060.fasta -evalue 1e-3
        -word_size 11 -outfmt 0 > task-NC_009060-fasta.reference
      class: CommandLineTool
      hints:
        DockerRequirement: {dockerImageId: /home/cc/blast.tar.gz}
      inputs:
        db_dir: {type: string}
      outputs:
        out: {type: string}
  task-NC_009062-fasta:
    in: {db_dir: makeblastdb/db_dir}
    out: [out]
    run:
      baseCommand: blastn -db databases/reference -query NC_009062.fasta -evalue 1e-3
        -word_size 11 -outfmt 0 > task-NC_009062-fasta.reference
      class: CommandLineTool
      hints:
        DockerRequirement: {dockerImageId: /home/cc/blast.tar.gz}
      inputs:
        db_dir: {type: string}
      outputs:
        out: {type: string}
  task-NC_009063-fasta:
    in: {db_dir: makeblastdb/db_dir}
    out: [out]
    run:
      baseCommand: blastn -db databases/reference -query NC_009063.fasta -evalue 1e-3
        -word_size 11 -outfmt 0 > task-NC_009063-fasta.reference
      class: CommandLineTool
      hints:
        DockerRequirement: {dockerImageId: /home/cc/blast.tar.gz}
      inputs:
        db_dir: {type: string}
      outputs:
        out: {type: string}
  task-NC_009064-fasta:
    in: {db_dir: makeblastdb/db_dir}
    out: [out]
    run:
      baseCommand: blastn -db databases/reference -query NC_009064.fasta -evalue 1e-3
        -word_size 11 -outfmt 0 > task-NC_009064-fasta.reference
      class: CommandLineTool
      hints:
        DockerRequirement: {dockerImageId: /home/cc/blast.tar.gz}
      inputs:
        db_dir: {type: string}
      outputs:
        out: {type: string}
  task-NC_009065-fasta:
    in: {db_dir: makeblastdb/db_dir}
    out: [out]
    run:
      baseCommand: blastn -db databases/reference -query NC_009065.fasta -evalue 1e-3
        -word_size 11 -outfmt 0 > task-NC_009065-fasta.reference
      class: CommandLineTool
      hints:
        DockerRequirement: {dockerImageId: /home/cc/blast.tar.gz}
      inputs:
        db_dir: {type: string}
      outputs:
        out: {type: string}
  task-NC_009066-fasta:
    in: {db_dir: makeblastdb/db_dir}
    out: [out]
    run:
      baseCommand: blastn -db databases/reference -query NC_009066.fasta -evalue 1e-3
        -word_size 11 -outfmt 0 > task-NC_009066-fasta.reference
      class: CommandLineTool
      hints:
        DockerRequirement: {dockerImageId: /home/cc/blast.tar.gz}
      inputs:
        db_dir: {type: string}
      outputs:
        out: {type: string}
  task-NC_009067-fasta:
    in: {db_dir: makeblastdb/db_dir}
    out: [out]
    run:
      baseCommand: blastn -db databases/reference -query NC_009067.fasta -evalue 1e-3
        -word_size 11 -outfmt 0 > task-NC_009067-fasta.reference
      class: CommandLineTool
      hints:
        DockerRequirement: {dockerImageId: /home/cc/blast.tar.gz}
      inputs:
        db_dir: {type: string}
      outputs:
        out: {type: string}
  task-NC_009459-fasta:
    in: {db_dir: makeblastdb/db_dir}
    out: [out]
    run:
      baseCommand: blastn -db databases/reference -query NC_009459.fasta -evalue 1e-3
        -word_size 11 -outfmt 0 > task-NC_009459-fasta.reference
      class: CommandLineTool
      hints:
        DockerRequirement: {dockerImageId: /home/cc/blast.tar.gz}
      inputs:
        db_dir: {type: string}
      outputs:
        out: {type: string}
  task-NC_010205-fasta:
    in: {db_dir: makeblastdb/db_dir}
    out: [out]
    run:
      baseCommand: blastn -db databases/reference -query NC_010205.fasta -evalue 1e-3
        -word_size 11 -outfmt 0 > task-NC_010205-fasta.reference
      class: CommandLineTool
      hints:
        DockerRequirement: {dockerImageId: /home/cc/blast.tar.gz}
      inputs:
        db_dir: {type: string}
      outputs:
        out: {type: string}
  task-NC_011168-fasta:
    in: {db_dir: makeblastdb/db_dir}
    out: [out]
    run:
      baseCommand: blastn -db databases/reference -query NC_011168.fasta -evalue 1e-3
        -word_size 11 -outfmt 0 > task-NC_011168-fasta.reference
      class: CommandLineTool
      hints:
        DockerRequirement: {dockerImageId: /home/cc/blast.tar.gz}
      inputs:
        db_dir: {type: string}
      outputs:
        out: {type: string}
  task-NC_011169-fasta:
    in: {db_dir: makeblastdb/db_dir}
    out: [out]
    run:
      baseCommand: blastn -db databases/reference -query NC_011169.fasta -evalue 1e-3
        -word_size 11 -outfmt 0 > task-NC_011169-fasta.reference
      class: CommandLineTool
      hints:
        DockerRequirement: {dockerImageId: /home/cc/blast.tar.gz}
      inputs:
        db_dir: {type: string}
      outputs:
        out: {type: string}
  task-NC_011170-fasta:
    in: {db_dir: makeblastdb/db_dir}
    out: [out]
    run:
      baseCommand: blastn -db databases/reference -query NC_011170.fasta -evalue 1e-3
        -word_size 11 -outfmt 0 > task-NC_011170-fasta.reference
      class: CommandLineTool
      hints:
        DockerRequirement: {dockerImageId: /home/cc/blast.tar.gz}
      inputs:
        db_dir: {type: string}
      outputs:
        out: {type: string}
  task-NC_011171-fasta:
    in: {db_dir: makeblastdb/db_dir}
    out: [out]
    run:
      baseCommand: blastn -db databases/reference -query NC_011171.fasta -evalue 1e-3
        -word_size 11 -outfmt 0 > task-NC_011171-fasta.reference
      class: CommandLineTool
      hints:
        DockerRequirement: {dockerImageId: /home/cc/blast.tar.gz}
      inputs:
        db_dir: {type: string}
      outputs:
        out: {type: string}
  task-NC_011177-fasta:
    in: {db_dir: makeblastdb/db_dir}
    out: [out]
    run:
      baseCommand: blastn -db databases/reference -query NC_011177.fasta -evalue 1e-3
        -word_size 11 -outfmt 0 > task-NC_011177-fasta.reference
      class: CommandLineTool
      hints:
        DockerRequirement: {dockerImageId: /home/cc/blast.tar.gz}
      inputs:
        db_dir: {type: string}
      outputs:
        out: {type: string}
  task-NC_011179-fasta:
    in: {db_dir: makeblastdb/db_dir}
    out: [out]
    run:
      baseCommand: blastn -db databases/reference -query NC_011179.fasta -evalue 1e-3
        -word_size 11 -outfmt 0 > task-NC_011179-fasta.reference
      class: CommandLineTool
      hints:
        DockerRequirement: {dockerImageId: /home/cc/blast.tar.gz}
      inputs:
        db_dir: {type: string}
      outputs:
        out: {type: string}
  task-NC_012055-fasta:
    in: {db_dir: makeblastdb/db_dir}
    out: [out]
    run:
      baseCommand: blastn -db databases/reference -query NC_012055.fasta -evalue 1e-3
        -word_size 11 -outfmt 0 > task-NC_012055-fasta.reference
      class: CommandLineTool
      hints:
        DockerRequirement: {dockerImageId: /home/cc/blast.tar.gz}
      inputs:
        db_dir: {type: string}
      outputs:
        out: {type: string}
  task-NC_013564-fasta:
    in: {db_dir: makeblastdb/db_dir}
    out: [out]
    run:
      baseCommand: blastn -db databases/reference -query NC_013564.fasta -evalue 1e-3
        -word_size 11 -outfmt 0 > task-NC_013564-fasta.reference
      class: CommandLineTool
      hints:
        DockerRequirement: {dockerImageId: /home/cc/blast.tar.gz}
      inputs:
        db_dir: {type: string}
      outputs:
        out: {type: string}
  task-NC_013577-fasta:
    in: {db_dir: makeblastdb/db_dir}
    out: [out]
    run:
      baseCommand: blastn -db databases/reference -query NC_013577.fasta -evalue 1e-3
        -word_size 11 -outfmt 0 > task-NC_013577-fasta.reference
      class: CommandLineTool
      hints:
        DockerRequirement: {dockerImageId: /home/cc/blast.tar.gz}
      inputs:
        db_dir: {type: string}
      outputs:
        out: {type: string}
  task-NC_013663-fasta:
    in: {db_dir: makeblastdb/db_dir}
    out: [out]
    run:
      baseCommand: blastn -db databases/reference -query NC_013663.fasta -evalue 1e-3
        -word_size 11 -outfmt 0 > task-NC_013663-fasta.reference
      class: CommandLineTool
      hints:
        DockerRequirement: {dockerImageId: /home/cc/blast.tar.gz}
      inputs:
        db_dir: {type: string}
      outputs:
        out: {type: string}
  task-NC_013750-fasta:
    in: {db_dir: makeblastdb/db_dir}
    out: [out]
    run:
      baseCommand: blastn -db databases/reference -query NC_013750.fasta -evalue 1e-3
        -word_size 11 -outfmt 0 > task-NC_013750-fasta.reference
      class: CommandLineTool
      hints:
        DockerRequirement: {dockerImageId: /home/cc/blast.tar.gz}
      inputs:
        db_dir: {type: string}
      outputs:
        out: {type: string}
  task-NC_018814-fasta:
    in: {db_dir: makeblastdb/db_dir}
    out: [out]
    run:
      baseCommand: blastn -db databases/reference -query NC_018814.fasta -evalue 1e-3
        -word_size 11 -outfmt 0 > task-NC_018814-fasta.reference
      class: CommandLineTool
      hints:
        DockerRequirement: {dockerImageId: /home/cc/blast.tar.gz}
      inputs:
        db_dir: {type: string}
      outputs:
        out: {type: string}
  task-NC_018815-fasta:
    in: {db_dir: makeblastdb/db_dir}
    out: [out]
    run:
      baseCommand: blastn -db databases/reference -query NC_018815.fasta -evalue 1e-3
        -word_size 11 -outfmt 0 > task-NC_018815-fasta.reference
      class: CommandLineTool
      hints:
        DockerRequirement: {dockerImageId: /home/cc/blast.tar.gz}
      inputs:
        db_dir: {type: string}
      outputs:
        out: {type: string}
