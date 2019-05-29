#!/bin/bash

# IV: nthreads, legacy_mode, {coriknl, farm80}
# DV: throughput
# C:  new_jtest

set -e  # terminate script on error
set -x  # Echo on

module swap craype-haswell craype-mic-knl
module unload darshan

cd ~/JANA2
git checkout 5dd814e
scons --clean
scons -j8

cd ~/jana-perf-testing/new_jtest_scaling/exp1
sbatch slurm.sh

cd ~/jana-perf-testing/new_jtest_scaling/exp2
sbatch slurm.sh

