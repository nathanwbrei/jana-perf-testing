
import os
from string import Template

jana_config = """
# $comment

plugins                   ${plugins}

jana:legacy_mode          ${jana_legacy_mode}
jana:debug_plugin_loading 1
jana:extended_report      1
jana:max_num_open_sources 1

benchmark:minthreads      ${benchmark_minthreads}
benchmark:maxthreads      ${benchmark_maxthreads}
benchmark:threadstep      ${benchmark_threadstep}

jtest:parser_ms           ${jtest_parser_ms}
jtest:disentangler_ms     ${jtest_disentangler_ms}
jtest:tracker_ms          ${jtest_tracker_ms}
jtest:plotter_ms          ${jtest_plotter_ms}

jtest:parser_bytes        ${jtest_parser_bytes}
jtest:disentangler_bytes  ${jtest_disentangler_bytes}
jtest:tracker_bytes       ${jtest_tracker_bytes}
jtest:plotter_bytes       ${jtest_plotter_bytes}
"""

slurm_sh = """#!/bin/bash

#SBATCH --job-name=jana2_${expname}_${jobname}
#SBATCH --qos=debug
#SBATCH --nodes=1
#SBATCH --time=30
#SBATCH --constraint=knl
#SBATCH --cpus-per-task=${cores}

export JANA_HOME="${jana_home_dir_cori}"
export RESULTS_DIR="${results_dir_cori}/${expname}/${jobname}"

lscpu > $$RESULTS_DIR/cpuinfo.txt

srun $$JANA_HOME/bin/jana -l $$RESULTS_DIR/jana.config -Pbenchmark:resultsdir=$$RESULTS_DIR -b > $$RESULTS_DIR/stdout.txt

"""

augur_sh = """#!/bin/bash

export JANA_HOME="${jana_home_dir_farm}"

lscpu > cpuinfo.txt

$$JANA_HOME/bin/jana -l jana.config -b

"""


augur_xml = """
<Request>
    <Project name="gluex"/>
    <Track name="debug"/>
    <Name name="jana2_${expname}_${jobname}"/>
    <NodeTag name="${platform}"/>
    <CPU core="${cores}"/>
    <Memory space="16" unit="GB"/>
    <Command><![CDATA[ 
        ${results_dir_farm}/${expname}/${jobname}/augur.sh
        ]]></Command>
    <List name="exp">
        ${results_dir_farm}/${expname}/${jobname}
    </List>
    <ForEach list="exp">
        <Job>
            <Input src="$${exp}/jana.config" dest="jana.config"/>
            <Output src="cpuinfo.txt" dest="$${exp}/cpuinfo.txt"/>
            <Output src="JANA_Test_Results/rates.dat" dest="$${exp}/rates.dat"/>
            <Output src="JANA_Test_Results/samples.dat" dest="$${exp}/samples.dat"/>
            <Stdout dest="$${exp}/stdout.txt"/>
            <Stderr dest="$${exp}/stderr.txt"/>
        </Job>
    </ForEach>
</Request>
"""

launch_farm_sh ="""
#!/bin/bash

# Running similar scaling tests as 2019-05-23,
# except we are running these on the farm instead

set -e  # Terminate script on error
set -x  # Echo on

cd ${jana_src_dir_farm}
git checkout ${jana_git_commit}
scons --clean
scons -j8

"""

launch_farm_sh_job = """
cd ${results_dir_farm}/${expname}/${jobname}
jsub -xml augur.xml
"""


launch_cori_sh = """
#!/bin/bash

set -e  # terminate script on error
set -x  # Echo on

module swap craype-haswell craype-mic-knl
module unload darshan

cd ${jana_src_dir_cori}
git checkout ${jana_git_commit}
scons --clean
scons -j8

"""

launch_cori_sh_job = """
cd ${results_dir_cori}/${expname}/${jobname}
sbatch slurm.sh

"""


def generate(testcase):

    path = testcase.results_dir_local + "/" + testcase.expname + "/" + testcase.jobname

    if not os.path.exists(path):
        os.mkdir(path)

    with open(path + "/jana.config", "w") as f:
        f.write(Template(jana_config).substitute(vars(testcase)))

    if testcase.platform == "coriknl":
        with open(path + "/slurm.sh", "w") as f:
            f.write(Template(slurm_sh).substitute(vars(testcase)))

    elif testcase.platform == "farm14" or testcase.platform == "farm18":
        with open(path + "/augur.sh", "w") as f:
            f.write(Template(augur_sh).substitute(vars(testcase)))

        with open(path + "/augur.xml", "w") as f:
            f.write(Template(augur_xml).substitute(vars(testcase)))

    else:
        raise Exception("Invalid platform!")




