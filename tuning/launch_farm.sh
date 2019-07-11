
#!/bin/bash

# Running similar scaling tests as 2019-05-23,
# except we are running these on the farm instead

set -e  # Terminate script on error
set -x  # Echo on

cd /home/nbrei/src/jana2
git checkout be8fc5d94a6f7bcb4159101b05dc0523cd3e037d
scons --clean
scons -j8


cd /home/nbrei/jana-perf-testing/tuning/exp1
jsub -xml augur.xml

cd /home/nbrei/jana-perf-testing/tuning/exp2
jsub -xml augur.xml

cd /home/nbrei/jana-perf-testing/tuning/exp3
jsub -xml augur.xml

cd /home/nbrei/jana-perf-testing/tuning/exp4
jsub -xml augur.xml

cd /home/nbrei/jana-perf-testing/tuning/exp5
jsub -xml augur.xml

cd /home/nbrei/jana-perf-testing/tuning/exp6
jsub -xml augur.xml

cd /home/nbrei/jana-perf-testing/tuning/exp7
jsub -xml augur.xml

cd /home/nbrei/jana-perf-testing/tuning/exp8
jsub -xml augur.xml

cd /home/nbrei/jana-perf-testing/tuning/exp9
jsub -xml augur.xml

cd /home/nbrei/jana-perf-testing/tuning/exp10
jsub -xml augur.xml

cd /home/nbrei/jana-perf-testing/tuning/exp11
jsub -xml augur.xml

cd /home/nbrei/jana-perf-testing/tuning/exp12
jsub -xml augur.xml

cd /home/nbrei/jana-perf-testing/tuning/exp13
jsub -xml augur.xml

cd /home/nbrei/jana-perf-testing/tuning/exp14
jsub -xml augur.xml

cd /home/nbrei/jana-perf-testing/tuning/exp15
jsub -xml augur.xml
