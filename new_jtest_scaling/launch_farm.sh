#!/bin/bash

# IV: nthreads, legacy_mode, {coriknl, farm80}
# DV: throughput
# C:  new_jtest

set -e  # Terminate script on error
set -x  # Echo on

cd /home/nbrei/src/jana2
git checkout 5dd814e
scons --clean
scons -j8


cd /home/nbrei/jana-perf-testing/new_jtest_scaling/exp3
jsub -xml augur.xml

cd /home/nbrei/jana-perf-testing/new_jtest_scaling/exp4
jsub -xml augur.xml

cd /home/nbrei/jana-perf-testing/new_jtest_scaling/exp5
jsub -xml augur.xml

cd /home/nbrei/jana-perf-testing/new_jtest_scaling/exp6
jsub -xml augur.xml
