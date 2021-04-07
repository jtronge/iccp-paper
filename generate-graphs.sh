#!/bin/sh

python ./scripts/task_execution_time.py --height 1200 --graph-height 1000 \
	profiles/blast-wf1-localhost-profile.json \
	> graphs/blast-wf1-localhost-profile.svg

python ./scripts/task_execution_time.py \
	--height 1200 \
	--graph-height 1000 \
	--title "Google Compute Engine (SSH File Transfer)" \
	profiles/workflow_name-profile-00000000001617743451.json \
	> graphs/workflow_name-profile-00000000001617743451.svg
