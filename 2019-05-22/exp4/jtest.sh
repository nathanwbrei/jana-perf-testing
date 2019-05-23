#!/bin/bash

#SBATCH --qos=debug
#SBATCH --nodes=1
#SBATCH --time=30
#SBATCH --constraint=knl
#SBATCH --cpus-per-task=272

export JANA_HOME="/global/homes/n/nbrei/JANA2/Linux-x86_64-cc18.0.1"
export RESULTS_DIR="/global/homes/n/nbrei/jana-perf-testing/2019-05-22/exp4"

lscpu > $RESULTS_DIR/cpuinfo.txt

srun $JANA_HOME/bin/jana -l $RESULTS_DIR/jana.config -Pbenchmark:resultsdir=$RESULTS_DIR -b > $RESULTS_DIR/stdout.txt
