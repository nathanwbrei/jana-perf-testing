#!/bin/bash

export JANA_HOME="/home/nbrei/src/jana2/Linux_CentOS7-x86_64-gcc4.8.5"

lscpu > cpuinfo.txt

#$JANA_HOME/bin/jana -l jana.config -b > stdout.txt 2> stderr.txt
$JANA_HOME/bin/jana -Pjana:legacy_mode=1 -Pbenchmark:minthreads=4 -Pbenchmark:maxthreads=88 -Pbenchmark:threadstep=4 -b > stdout.txt 2> stderr.txt
