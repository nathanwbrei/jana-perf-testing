from generator import generate_from_dict as generate

platforms = {
    "coriknl": {
        "cores": 272,
        "benchmark_minthreads": 4,
        "benchmark_maxthreads": 272,
        "benchmark_threadstep": 8,
        "src_dir": "/global/homes/n/nbrei/JANA2",
        "jana_home_dir": "/global/homes/n/nbrei/JANA2/Linux-x86_64-cc18.0.1",
        "results_dir": "/global/homes/n/nbrei/jana-perf-testing"
        },

    "farm18":  {
        "cores": 80,
        "benchmark_minthreads": 4,
        "benchmark_maxthreads": 80,
        "benchmark_threadstep": 4,
        "src_dir": "/home/nbrei/src/jana2",
        "jana_home_dir": "/home/nbrei/src/jana2/Linux_CentOS7-x86_64-gcc4.8.5",
        "results_dir": "/home/nbrei/jana-perf-testing",
        },

    "farm14":  {
        "cores": 40,
        "benchmark_minthreads": 4,
        "benchmark_maxthreads": 48,
        "benchmark_threadstep": 4,
        "src_dir": "/home/nbrei/src/jana2",
        "jana_home_dir": "/home/nbrei/src/jana2/Linux_CentOS7-x86_64-gcc4.8.5",
        "results_dir": "/home/nbrei/jana-perf-testing",
    },
}

plugins = {
    "JTest": {
        "jtest_parser_bytes": 2000000,
        "jtest_disentangler_bytes": 500000,
        "jtest_tracker_bytes": 1000,
        "jtest_plotter_bytes": 1000,
        "jtest_parser_ms": 1,
        "jtest_disentangler_ms": 20,
        "jtest_tracker_ms": 200,
        "jtest_plotter_ms": 20,
    }
}

experiment = {
    "expname": "tuning",
    "comment": "Large and small block sizes on different architectures",
    "git_commit": "asdf",
    "plugins": "JTest",
    "jana_legacy_mode": 0,
    "results_dir_local": "/u/home/nbrei/jana-perf-testing",
}

jobs = [
    {
        "jobname": "exp1",
        "platform": "coriknl",
        "jtest_parser_bytes": 2000000
    },
    {
        "jobname": "exp2",
        "platform": "coriknl",
        "jtest_parser_bytes": 32000000
    },
    {
        "jobname": "exp3",
        "platform": "farm18",
        "jtest_parser_bytes": 2000000
    },
    {
        "jobname": "exp4",
        "platform": "farm18",
        "jtest_parser_bytes": 32000000
    },
]

def get_jobs():
    for job in jobs:
        d = {}
        d.update(experiment)
        d.update(job)

        defaults = {}
        defaults.update(platforms[d["platform"]])
        defaults.update(plugins[d["plugins"]])

        defaults.update(d)
        yield defaults


