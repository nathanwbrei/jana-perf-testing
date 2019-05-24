#!/bin/bash

set -e  # terminate script on error
set -x  # Echo on

module swap craype-haswell craype-mic-knl
module unload darshan

cd ~/JANA2
git checkout a9683c
scons --clean
scons -j8

cd ~/jana-perf-testing/block_size_scaling/exp1
sbatch slurm.sh

cd ~/jana-perf-testing/block_size_scaling/exp2
sbatch slurm.sh

cd ~/jana-perf-testing/block_size_scaling/exp3
sbatch slurm.sh

cd ~/jana-perf-testing/block_size_scaling/exp4
sbatch slurm.sh


