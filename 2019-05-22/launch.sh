#!/bin/bash

module swap craype-haswell craype-mic-knl
module unload darshan

cd ~/JANA2
git checkout a9683c
scons --clean
scons -j8

cd ~/jana-perf-testing/2019-05-22/exp1
sbatch jtest.sh

cd ~/jana-perf-testing/2019-05-22/exp2
sbatch jtest.sh

cd ~/jana-perf-testing/2019-05-22/exp3
sbatch jtest.sh

cd ~/jana-perf-testing/2019-05-22/exp4
sbatch jtest.sh
