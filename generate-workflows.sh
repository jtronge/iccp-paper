#!/bin/sh

python scripts/generate_blast_workflow.py \
	--output-dir workflows \
	--prefix blast-cloud-scatter \
	--ref-sequence data/carAur01.sm.fa \
	--sequence-dir data/assembled-fish_mito \
	--docker-ctr ncbi/blast \
	--ch-ctr blast.tar.gz
