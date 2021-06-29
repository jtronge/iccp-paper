#!/bin/sh

#python ./scripts/task_execution_time.py --height 1200 --graph-height 1000 \
#	profiles/blast-wf1-localhost-profile.json \
#	> graphs/blast-wf1-localhost-profile.svg

#python ./scripts/task_execution_time.py \
#	--height 1200 \
#	--graph-height 1000 \
#	--title "Google Compute Engine (SSH File Transfer)" \
#	profiles/workflow_name-profile-00000000001617743451.json \
#	> graphs/workflow_name-profile-00000000001617743451.svg

#python ./scripts/task_execution_time.py \
#	--height 1200 \
#	--graph-height 1000 \
#	--title "ChameleonCloud + Google Compute Engine" \
#	profiles/workflow_name-profile-00000000001618359888.json \
#	> graphs/workflow_name-profile-00000000001618359888.svg
	# > graphs/workflow_name-profile-00000000001618272656.svg
	# ididprofiles/workflow_name-profile-00000000001618272656.json \
	# profiles/workflow_name-profile-00000000001617743451.json \

# python ./scripts/task_execution_time.py \
#	--height 1200 \
#	--graph-height 1000 \
#	--title "ChameleonCloud" \
#	profiles/workflow_name-profile-00000000001618362006.json \
#	> graphs/workflow_name-profile-00000000001618362006.svg


#python ./scripts/task_execution_time.py \
#	--height 1200 \
#	--graph-height 1000 \
#	--title "One Node - Google Compute Engine" \
#	profiles/one-node-google.json \
#	> graphs/one-node-google.svg

#python ./scripts/task_execution_time.py \
#	--height 1200 \
#	--graph-height 1000 \
#	--title "Two Nodes - ChameleonCloud + Google Compute Engine" \
#	profiles/two-node-chameleon-google.json \
#	> graphs/two-node-chameleon-google.svg

#python ./scripts/run_graph.py \
#	profiles/one-node-google.json \
#	profiles/two-node-chameleon-google.json \
#	> graphs/workflow-comparison-`date +%F`.svg

#python ./scripts/run_graph.py \
#	--title "Multi-Cloud Run: BLAST Workflow" \
#	profiles/one-node-google.json \
#	profiles/two-node-chameleon-google.json \
#	profiles/four-node-profile-chameleon-google.json \
#	> graphs/workflow-comparison-4-2-1-`date +%F`.svg

#python ./scripts/run_graph.py \
#	--title "Multi-Cloud Run: Complex Dependency Workflow" \
#	profiles/sleep-workflow/*.json \
#	> graphs/sleep-workflow.svg


#python ./scripts/task_execution_time.py \
#	--height 1200 \
#	--graph-height 1000 \
#	--title "One Google Node" \
#	profiles/one-node-google.json \
#	> graphs/task-graph-one-node-google-04-23.svg
	# profiles/two-node-chameleon-google.json \
	#> graphs/two-node-chameleon-google.svg


python ./scripts/task_execution_time.py \
	--title "HPC + Google Compute Engine" \
	profiles/hpc-cloud-workflow-2021-06-28.json \
	> graphs/hpc-cloud-workflow-2021-06-28.svg

python ./scripts/task_execution_time.py \
	--title "BLAST HPC Only Run" \
	profiles/blast-run-one-resource-2021-06-29.json \
	> graphs/blast-run-one-resource-2021-06-29.svg
