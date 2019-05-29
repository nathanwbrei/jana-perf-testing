#!/bin/bash

# IV: nthreads, nloopiters, {coriknl, farm80}
# DV: throughput
# C:  new_jtest

set -e  # Terminate script on error
set -x  # Echo on

cd /home/nbrei/src/jana2
git checkout 5dd814e
scons --clean
scons -j8

cd /home/nbrei/jana-perf-testing/computation_scaling
jsub -xml augur.xml

