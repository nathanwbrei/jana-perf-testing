#!/bin/bash

#SBATCH --qos=debug
#SBATCH --nodes=1
#SBATCH --time=30
#SBATCH --constraint=knl
#SBATCH --cpus-per-task=272

export JANA_HOME="/global/homes/n/nbrei/JANA2/Linux-x86_64-cc18.0.1"
export RESULTS_DIR="/global/homes/n/nbrei/2019-05-22-4"

srun $JANA_HOME/bin/jana -l jana.config -Pbenchmark:resultsdir=$RESULTS_DIR -b > $RESULTS_DIR/stdout.txt
