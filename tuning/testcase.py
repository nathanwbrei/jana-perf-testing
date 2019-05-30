
class TestCase:

    def __init__(self, platform="coriknl"):

        if platform == "coriknl":
            self.cores = 272
            self.benchmark_minthreads = 4
            self.benchmark_maxthreads = 272
            self.benchmark_threadstep = 8

        elif platform == "farm18":
            self.cores = 80
            self.benchmark_minthreads = 4
            self.benchmark_maxthreads = 80
            self.benchmark_threadstep = 4

        elif platform == "farm14":
            self.cores = 40
            self.benchmark_minthreads = 4
            self.benchmark_maxthreads = 48
            self.benchmark_threadstep = 4

        else:
            raise Exception("Invalid platform!")

        self.expname = "tuning"
        self.jobname = "exp1"
        self.comment = ""
        self.platform = platform
        self.jana_git_commit = "findme"
        self.plugins = "JTest"
        self.jana_legacy_mode = 0

        self.jana_src_dir_cori = "/global/homes/n/nbrei/JANA2"
        self.jana_home_dir_cori = "/global/homes/n/nbrei/JANA2/Linux-x86_64-cc18.0.1"
        self.results_dir_cori = "/global/homes/n/nbrei/jana-perf-testing"

        self.jana_src_dir_farm = "/home/nbrei/src/jana2"
        self.jana_home_dir_farm = "/home/nbrei/src/jana2/Linux_CentOS7-x86_64-gcc4.8.5"
        self.results_dir_farm = "/home/nbrei/jana-perf-testing"

        self.results_dir_local = "/u/home/nbrei/jana-perf-testing"

        self.jtest_parser_bytes = 2000000
        self.jtest_disentangler_bytes = 500000
        self.jtest_tracker_bytes = 1000
        self.jtest_plotter_bytes = 1000

        self.jtest_parser_ms = 1
        self.jtest_disentangler_ms = 20
        self.jtest_tracker_ms = 200
        self.jtest_plotter_ms = 20




