#!/bin/bash

module swap craype-haswell craype-mic-knl

cd ~/JANA2
git checkout fc416f
scons --clean
scons -j8

cd ~/jana-perf-testing/2019-05-22

sbatch exp1/jtest.sh
sbatch exp2/jtest.sh
sbatch exp3/jtest.sh
sbatch exp4/jtest.sh
