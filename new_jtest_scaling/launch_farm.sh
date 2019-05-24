#!/bin/bash

# IV: nthreads, legacy_mode, {coriknl, farm80}
# DV: throughput
# C:  new_jtest

set -e  # Terminate script on error
set -x  # Echo on

cd /home/nbrei/src/jana2
git checkout a9683c
scons --clean
scons -j8

cd /home/nbrei/jana-perf-testing/new_jtest_scaling
jsub -xml jtest_augur.xml


