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
