#!/bin/sh

python scripts/generate_workflow.py \
	--prefix blast-cloud \
	--sequence-dir data/assembled-fish_mito \
	--workdir /home/cc

python scripts/generate_blast_workflow.py \
	--output-dir workflows \
	--prefix blast-cloud \
	--ref-sequence data/carAur01.sm.fa \
	--sequence-dir data/assembled-fish_mito \
	--workdir /home/cc \
	--docker-ctr ncbi/blast \
	--ch-ctr /home/cc/blast.tar.gz
