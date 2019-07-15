
#!/bin/bash

# Running similar scaling tests as 2019-05-23,
# except we are running these on the farm instead

set -e  # Terminate script on error
set -x  # Echo on

cd /global/homes/n/nbrei/JANA2
git checkout be8fc5d94a6f7bcb4159101b05dc0523cd3e037d
scons --clean
scons -j8

