
import os, stat
from string import Template
from testmatrix import TestMatrix

slurm_sh = """#!/bin/bash

#SBATCH --job-name=jana2_${expname}_${jobname}
#SBATCH --qos=debug
#SBATCH --nodes=1
#SBATCH --time=30
#SBATCH --constraint=knl
#SBATCH --cpus-per-task=${cores}

export JANA_HOME="${jana_home_dir}"
export RESULTS_DIR="${results_dir}/${expname}/${jobname}"

lscpu > $$RESULTS_DIR/cpuinfo.txt

srun $$JANA_HOME/bin/jana -l $$RESULTS_DIR/jana.config -Pbenchmark:resultsdir=$$RESULTS_DIR -b > $$RESULTS_DIR/stdout.txt

"""

augur_sh = """#!/bin/bash

export JANA_HOME="${jana_home_dir}"

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
    <Command><![CDATA[ 
        ${results_dir}/${expname}/${jobname}/augur.sh
        ]]></Command>
    <List name="exp">
        ${results_dir}/${expname}/${jobname}
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

cd ${src_dir}
git checkout ${git_commit}
scons --clean
scons -j8

"""

launch_farm_sh_job = """
cd ${results_dir}/${expname}/${jobname}
jsub -xml augur.xml
"""


launch_cori_sh = """
#!/bin/bash

set -e  # terminate script on error
set -x  # Echo on

module swap craype-haswell craype-mic-knl
module unload darshan

cd ${src_dir}
git checkout ${git_commit}
scons --clean
scons -j8

"""

launch_cori_sh_job = """
cd ${results_dir}/${expname}/${jobname}
sbatch slurm.sh

"""

def generate_jana_config(path, d, blacklist):

    maxlen = 0
    for (k, v) in d.items():
        maxlen = max(maxlen, len(k))
    maxlen += 4

    with open(path + "/jana.config", "w") as f:
        for (k, v) in d.items():
            if k not in blacklist:
                f.write(k.ljust(maxlen) + str(v) + "\n")



def generate_from_dict(d):

    path = d["results_dir_local"] + "/" + d["expname"] + "/" + d["jobname"]

    if not os.path.exists(path):
        os.mkdir(path)

    generate_jana_config(path, d, tm.blacklist)

    if d["platform"] == "coriknl":
        with open(path + "/slurm.sh", "w") as f:
            f.write(Template(slurm_sh).substitute(d))
        os.chmod(path+"/slurm.sh", stat.S_IREAD | stat.S_IWRITE | stat.S_IEXEC)

    elif d["platform"] == "farm14" or d["platform"] == "farm18":

        with open(path + "/augur.sh", "w") as f:
            f.write(Template(augur_sh).substitute(d))

        with open(path + "/augur.xml", "w") as f:
            f.write(Template(augur_xml).substitute(d))

        os.chmod(path+"/augur.sh", stat.S_IREAD | stat.S_IWRITE | stat.S_IEXEC)

    else:
        raise Exception("Invalid platform!")


if __name__ == "__main__":
    tm = TestMatrix()
    exp = tm.hydrate_experiment()

    launch_farm = Template(launch_farm_sh).substitute(exp)
    launch_cori = Template(launch_cori_sh).substitute(exp)

    for job in tm.hydrate_jobs():
        generate_from_dict(job)

        if job["platform"] == "coriknl":
            launch_cori += Template(launch_cori_sh_job).substitute(job)

        elif job["platform"] == "farm14" or job["platform"] == "farm18":
            launch_farm += Template(launch_farm_sh_job).substitute(job)

    path = tm.exp_path()

    with open(path + "/launch_farm.sh", "w") as f:
        f.write(launch_farm)

    with open(path + "/launch_cori.sh", "w") as f:
        f.write(launch_cori)

    os.chmod(path+"/launch_farm.sh", stat.S_IREAD | stat.S_IWRITE | stat.S_IEXEC)
    os.chmod(path+"/launch_cori.sh", stat.S_IREAD | stat.S_IWRITE | stat.S_IEXEC)

