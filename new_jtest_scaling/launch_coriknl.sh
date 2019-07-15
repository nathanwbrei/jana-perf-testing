
#!/bin/bash

set -e  # terminate script on error
set -x  # Echo on

module swap craype-haswell craype-mic-knl
module unload darshan

cd /global/homes/n/nbrei/JANA2
git checkout be8fc5d94a6f7bcb4159101b05dc0523cd3e037d
scons --clean
scons -j8


cd /global/homes/n/nbrei/jana-perf-testing/new_jtest_scaling/exp1
sbatch slurm.sh


cd /global/homes/n/nbrei/jana-perf-testing/new_jtest_scaling/exp2
sbatch slurm.sh

