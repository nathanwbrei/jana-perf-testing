#!/bin/bash

# IV: nthreads, nloopiters, {coriknl, farm80}
# DV: throughput
# C:  new_jtest

set -e  # terminate script on error
set -x  # Echo on

module swap craype-haswell craype-mic-knl
module unload darshan

cd ~/JANA2
git checkout findme
scons --clean
scons -j8

cd ~/jana-perf-testing/computation_scaling/exp1
sbatch slurm.sh

cd ~/jana-perf-testing/computation_scaling/exp2
sbatch slurm.sh

cd ~/jana-perf-testing/computation_scaling/exp3
sbatch slurm.sh

cd ~/jana-perf-testing/computation_scaling/exp4
sbatch slurm.sh


