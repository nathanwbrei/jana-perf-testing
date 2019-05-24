#!/bin/bash

export JANA_HOME="/home/nbrei/src/jana2/Linux_CentOS7-x86_64-gcc4.8.5"

lscpu > cpuinfo.txt

$JANA_HOME/bin/jana -l jana.config -Pplugins=JTest -b
