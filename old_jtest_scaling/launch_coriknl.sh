#!/bin/bash

set -e  # terminate script on error
set -x  # Echo on

module swap craype-haswell craype-mic-knl
module unload darshan

cd ~/JANA2
git checkout 5dd814e
scons --clean
scons -j8

cd ~/jana-perf-testing/old_jtest_scaling/exp1
sbatch jtest_slurm.sh

cd ~/jana-perf-testing/old_jtest_scaling/exp2
sbatch jtest_slurm.sh

