#!/bin/bash

# Running similar scaling tests as 2019-05-23,
# except we are running these on the farm instead

set -e  # Terminate script on error

cd /home/nbrei/src/jana2
git checkout a9683c
scons --clean
scons -j8

cd /home/nbrei/jana-perf-testing/2019-05-23/

jsub -xml jtest_augur.xml