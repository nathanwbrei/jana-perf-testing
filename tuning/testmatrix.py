from collections import OrderedDict


class TestMatrix:

    experiment = {
        "expname": "tuning",
        "comment": "Examine how different affinity/locality strategies affect throughput",
        "git_commit": "be8fc5d94a6f7bcb4159101b05dc0523cd3e037d",
        "scenario": "JTest",
        "platform": "farm18",
        "results_dir_local": "/u/home/nbrei/jana-perf-testing",
        "jana:event_queue_threshold": 80,
        "jana:legacy_mode": 0,
    }

    jobs = [
        {
            "jobname": "exp1",
            "jana:affinity": 0,
            "jana:locality": 0,
        },
        {
            "jobname": "exp2",
            "jana:affinity": 0,
            "jana:locality": 1,
        },
        {
            "jobname": "exp3",
            "jana:affinity": 0,
            "jana:locality": 2,
        },
        {
            "jobname": "exp4",
            "jana:affinity": 0,
            "jana:locality": 3,
        },
        {
            "jobname": "exp5",
            "jana:affinity": 0,
            "jana:locality": 4,
        },
        {
            "jobname": "exp6",
            "jana:affinity": 1,
            "jana:locality": 0,
        },
        {
            "jobname": "exp7",
            "jana:affinity": 1,
            "jana:locality": 1,
        },
        {
            "jobname": "exp8",
            "jana:affinity": 1,
            "jana:locality": 2,
        },
        {
            "jobname": "exp9",
            "jana:affinity": 1,
            "jana:locality": 3,
        },
        {
            "jobname": "exp10",
            "jana:affinity": 1,
            "jana:locality": 4,
        },
        {
            "jobname": "exp11",
            "jana:affinity": 2,
            "jana:locality": 0,
        },
        {
            "jobname": "exp12",
            "jana:affinity": 2,
            "jana:locality": 1,
        },
        {
            "jobname": "exp13",
            "jana:affinity": 2,
            "jana:locality": 2,
        },
        {
            "jobname": "exp14",
            "jana:affinity": 2,
            "jana:locality": 3,
        },
        {
            "jobname": "exp15",
            "jana:affinity": 2,
            "jana:locality": 4,
        }
    ]

    platforms = {
        "coriknl": {
            "cores": 272,
            "benchmark:minthreads": 4,
            "benchmark:maxthreads": 272,
            "benchmark:threadstep": 8,
            "src_dir": "/global/homes/n/nbrei/JANA2",
            "jana_home_dir": "/global/homes/n/nbrei/JANA2/Linux-x86_64-cc18.0.1",
            "results_dir": "/global/homes/n/nbrei/jana-perf-testing"
        },

        "farm18":  {
            "cores": 80,
            "benchmark:minthreads": 4,
            "benchmark:maxthreads": 80,
            "benchmark:threadstep": 4,
            "src_dir": "/home/nbrei/src/jana2",
            "jana_home_dir": "/home/nbrei/src/jana2/Linux_CentOS7-x86_64-gcc4.8.5",
            "results_dir": "/home/nbrei/jana-perf-testing",
        },

        "farm14":  {
            "cores": 40,
            "benchmark:minthreads": 4,
            "benchmark:maxthreads": 48,
            "benchmark:threadstep": 4,
            "src_dir": "/home/nbrei/src/jana2",
            "jana_home_dir": "/home/nbrei/src/jana2/Linux_CentOS7-x86_64-gcc4.8.5",
            "results_dir": "/home/nbrei/jana-perf-testing",
        },
    }

    scenarios = {
        "JTest": {
            "plugins": "JTest",
            "jtest:parser_bytes": 2000000,
            "jtest:disentangler_bytes": 500000,
            "jtest:tracker_bytes": 1000,
            "jtest:plotter_bytes": 1000,
            "jtest:parser_ms": 1,
            "jtest:disentangler_ms": 20,
            "jtest:tracker_ms": 200,
            "jtest:plotter_ms": 20,
        },
        "JTestOld": {
            "plugins": "JTestOld",
        }
    }

    blacklist = ["expname", "jobname", "comment", "git_commit", "platform", "results_dir_local", "cores", "src_dir",
                 "jana_home_dir", "results_dir", "scenario"]

    def hydrate_jobs(self):

        for job in self.jobs:
            d = {}
            d.update(self.experiment)
            d.update(job)

            defaults = {}
            defaults.update(self.platforms[d["platform"]])
            defaults.update(self.scenarios[d["scenario"]])

            defaults.update(d)
            result = OrderedDict(sorted(defaults.items(), key=lambda t: t[0]))
            yield result

    def hydrate_experiment(self):

        d = {}
        d.update(self.platforms[self.experiment["platform"]])
        d.update(self.scenarios[self.experiment["scenario"]])
        d.update(self.experiment)
        return d

    def exp_path(self):
        exp = self.hydrate_experiment()
        return exp["results_dir_local"] + "/" + exp["expname"]
