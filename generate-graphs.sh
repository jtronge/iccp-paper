#!/bin/sh

python ./scripts/run_graph_sleep_wfl.py \
	--width 1265 \
	profiles/sleep-workflow/*.json \
	> graphs/test-sleep-with-nums.svg
python ./scripts/run_graph_with_colors.py \
	profiles/one-node-google.json \
	profiles/two-node-chameleon-google.json \
	profiles/four-node-profile-chameleon-google.json \
	> graphs/test-with-colors.svg
python ./scripts/task_execution_time.py \
	--title "HPC (Darwin) + 4 Google Cloud Nodes" \
	--width 1100 \
	--graph-width 800 \
	--height 1200 \
	--graph-height 1000 \
	profiles/darwin-plus-google-4.json \
	> graphs/darwin-plus-google-4.svg
