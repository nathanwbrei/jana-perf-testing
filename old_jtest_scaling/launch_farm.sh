#!/bin/bash

# Running similar scaling tests as 2019-05-23,
# except we are running these on the farm instead

set -e  # Terminate script on error
set -x  # Echo on

cd /home/nbrei/src/jana2
git checkout ecb66f
scons --clean
scons -j8

cd /home/nbrei/jana-perf-testing/old_jtest_scaling/exp3
jsub -xml jtest_augur.xml

cd /home/nbrei/jana-perf-testing/old_jtest_scaling/exp4
jsub -xml jtest_augur.xml
