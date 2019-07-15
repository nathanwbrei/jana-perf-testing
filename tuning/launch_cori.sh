
#!/bin/bash

set -e  # terminate script on error
set -x  # Echo on

module swap craype-haswell craype-mic-knl
module unload darshan

cd /global/homes/n/nbrei/JANA2
git checkout be8fc5d94a6f7bcb4159101b05dc0523cd3e037d
scons --clean
scons -j8


cd /global/homes/n/nbrei/jana-perf-testing/tuning/exp1
sbatch slurm.sh


cd /global/homes/n/nbrei/jana-perf-testing/tuning/exp2
sbatch slurm.sh


cd /global/homes/n/nbrei/jana-perf-testing/tuning/exp3
sbatch slurm.sh


cd /global/homes/n/nbrei/jana-perf-testing/tuning/exp4
sbatch slurm.sh


cd /global/homes/n/nbrei/jana-perf-testing/tuning/exp5
sbatch slurm.sh


cd /global/homes/n/nbrei/jana-perf-testing/tuning/exp6
sbatch slurm.sh


cd /global/homes/n/nbrei/jana-perf-testing/tuning/exp7
sbatch slurm.sh


cd /global/homes/n/nbrei/jana-perf-testing/tuning/exp8
sbatch slurm.sh


cd /global/homes/n/nbrei/jana-perf-testing/tuning/exp9
sbatch slurm.sh


cd /global/homes/n/nbrei/jana-perf-testing/tuning/exp10
sbatch slurm.sh


cd /global/homes/n/nbrei/jana-perf-testing/tuning/exp11
sbatch slurm.sh


cd /global/homes/n/nbrei/jana-perf-testing/tuning/exp12
sbatch slurm.sh


cd /global/homes/n/nbrei/jana-perf-testing/tuning/exp13
sbatch slurm.sh


cd /global/homes/n/nbrei/jana-perf-testing/tuning/exp14
sbatch slurm.sh


cd /global/homes/n/nbrei/jana-perf-testing/tuning/exp15
sbatch slurm.sh

