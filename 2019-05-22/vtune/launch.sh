#!/bin/bash

module swap craype-haswell craype-mic-knl
module load vtune
module unload darshan

cd ~/JANA2
git checkout fc416f
scons --clean
scons -j8

cd ~/jana-perf-testing/2019-05-22/vtune

sbatch jtest.sh

# amplxe-cl -finalize -r ~/jana-perf-testing/2019-05-22/vtune/vtune_results
