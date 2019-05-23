#!/bin/bash

#SBATCH --qos=debug
#SBATCH --nodes=1
#SBATCH --time=10
#SBATCH --constraint=knl
#SBATCH --cpus-per-task=272
#SBATCH --perf=vtune

export JANA_HOME="/global/homes/n/nbrei/JANA2/Linux-x86_64-cc18.0.1"
export RESULTS_DIR="/global/homes/n/nbrei/jana-perf-testing/2019-05-22/vtune"

module load vtune

lscpu > $RESULTS_DIR/cpuinfo.txt

srun amplxe-cl -collect general-exploration -r $RESULTS_DIR/vtune_results -- $JANA_HOME/bin/jana -l jana.config -Pbenchmark:resultsdir=$RESULTS_DIR > $RESULTS_DIR/stdout.txt


