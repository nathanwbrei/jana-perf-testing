
#!/bin/bash

# Running similar scaling tests as 2019-05-23,
# except we are running these on the farm instead

set -e  # Terminate script on error
set -x  # Echo on

cd /home/nbrei/src/jana2
git checkout a33521bdd5ff19b103162276718ae8e71f19eb51
scons --clean
scons -j8


cd /home/nbrei/jana-perf-testing/queue_threshold_scaling/exp1
jsub -xml augur.xml

cd /home/nbrei/jana-perf-testing/queue_threshold_scaling/exp2
jsub -xml augur.xml

cd /home/nbrei/jana-perf-testing/queue_threshold_scaling/exp3
jsub -xml augur.xml

cd /home/nbrei/jana-perf-testing/queue_threshold_scaling/exp4
jsub -xml augur.xml

cd /home/nbrei/jana-perf-testing/queue_threshold_scaling/exp5
jsub -xml augur.xml

cd /home/nbrei/jana-perf-testing/queue_threshold_scaling/exp6
jsub -xml augur.xml
