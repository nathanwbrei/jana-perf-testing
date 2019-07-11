
#!/bin/bash

set -e  # terminate script on error
set -x  # Echo on

module swap craype-haswell craype-mic-knl
module unload darshan

cd /home/nbrei/src/jana2
git checkout a33521bdd5ff19b103162276718ae8e71f19eb51
scons --clean
scons -j8

