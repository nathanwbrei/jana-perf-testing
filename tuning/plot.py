#!/usr/bin/env python
#
# This script can be used to plot the results of running the
# JANA JTest plugin in scaling test mode. To use it, you must
# have python installed as well as the numpy and matplotlib
# python packages. Just run it in the same directory as the
# rates.dat file.
# 
# n.b. This will automatically add the creation time of the
# rates.dat file to the plot title. Be cautious copying it!
#

import numpy as np
import matplotlib.pyplot as plt


class Experiment:
    def __init__(self, dir, label, color, marker):
        self.dir = dir
        self.label = label
        self.color = color
        self.marker = marker


class PlotDef:
    def __init__(self, filename="", title="", description=""):
        self.filename = filename
        self.title = title
        self.description = description
        self.exps = []

    def add_exp(self, dir, label, color, marker):
        self.exps.append(Experiment(dir, label, color, marker))

    def create(self, loc="best"):
        plt.figure()
        plt.title(self.title)
        plt.xlabel('Nthreads')
        plt.ylabel('Rate (Hz)')
        min_nthreads = 100
        max_nthreads = 0

        for exp in self.exps:
            fname = exp.dir + "/rates.dat"

            # Load data using numpy
            nthreads,avg_rate,rms_rate = np.loadtxt(fname, skiprows=1,usecols=(0,1,2), unpack=True)
            min_nthreads = min(min_nthreads, nthreads.min())
            max_nthreads = max(max_nthreads, nthreads.max())

            # Create plot using matplotlib
            plt.errorbar(nthreads, avg_rate, rms_rate,
                         linestyle='', ecolor='red',
                         elinewidth=1, capthick=1, marker=exp.marker,
                         ms=6, markerfacecolor=exp.color, label=exp.label)


        plt.legend(loc=loc)
        plt.xlim(min_nthreads-1.0, max_nthreads+1.0)
        plt.grid(True)
        plt.savefig(self.filename + ".png")



plot4 = PlotDef()
plot4.filename = "plot_summary_coriknl"
plot4.title = "JANA2 affinity/locality tuning (Cori KNL)"

plot1 = PlotDef()
plot1.filename = "plot_localities_with_no_affinity_coriknl"
plot1.title = "JANA2 locality strategies, no affinity"

plot1.add_exp('exp1', 'Global', 'magenta', "s")
plot4.add_exp('exp1', 'Global locality, no affinity', 'magenta', "s")
#plot1.add_exp('exp2', 'Socket', 'blue', "s")
#plot1.add_exp('exp3', 'NUMA domain', 'cyan', "s")
plot1.add_exp('exp4', 'Core', 'black', "s")
plot4.add_exp('exp4', 'Core locality, no affinity', 'black', "s")
plot1.add_exp('exp5', 'CPU', 'green', "s")

plot1.create(loc="lower right")


plot2 = PlotDef()
plot2.filename = "plot_localities_with_memory_affinity_coriknl"
plot2.title = "JANA2 locality strategies, memory-bound affinity (uses fewer locations)"

plot2.add_exp('exp6', 'Global', 'magenta', "^")
#plot2.add_exp('exp7', 'Socket', 'blue', "^")
#plot2.add_exp('exp8', 'NUMA domain', 'cyan', "^")
plot2.add_exp('exp9', 'Core', 'black', "^")
plot4.add_exp('exp9', 'Core locality, memory affinity', 'black', "^")
plot2.add_exp('exp10', 'CPU', 'green', "^")

plot2.create(loc="lower right")

plot3 = PlotDef()
plot3.filename = "plot_localities_with_compute_affinity_coriknl"
plot3.title = "JANA2 locality strategies, compute-bound affinity (uses more locations)"

plot3.add_exp('exp11', 'Global', 'magenta', "o")
#plot3.add_exp('exp12', 'Socket', 'blue', "o")
#plot3.add_exp('exp13', 'NUMA domain', 'cyan', "o")
plot3.add_exp('exp14', 'Core', 'black', "o")
plot4.add_exp('exp14', 'Core locality, compute affinity', 'black', "o")
plot3.add_exp('exp15', 'CPU', 'green', "o")

plot3.create(loc="lower right")
plot4.create(loc="lower right")
