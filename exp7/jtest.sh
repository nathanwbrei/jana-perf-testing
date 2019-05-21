#!/bin/bash

#SBATCH --qos=debug
#SBATCH --nodes=1
#SBATCH --time=30
#SBATCH --constraint=knl
#SBATCH --cpus-per-task=272

export JANA_HOME="/global/homes/n/nbrei/JANA2/Linux-x86_64-cc18.0.1"
export RESULTS_DIR="/global/homes/n/nbrei/exp1"

srun $JANA_HOME/bin/jana -Pplugins=JTest.so -Pnthreads=1 -Pjana:legacy_mode=0 -Pbenchmark:resultsdir=$RESULTS_DIR -Pbenchmark:minthreads=4 -Pbenchmark:maxthreads=272 -Pbenchmark:threadstep=4 -Pjtest:parser_ms=1 -b > $RESULTS_DIR/stdout.txt
