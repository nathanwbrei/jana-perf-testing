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




plot1 = PlotDef()
plot1.filename = "comp_scaling"
plot1.title = "JANA2 computation scaling"

plot1.add_exp('exp1', 'Cori KNL, 2.8e5 sqrt ops/event', 'green', "s")
plot1.add_exp('exp2', 'Cori KNL, 2.8e6 sqrt ops/event', 'blue', "s")
plot1.add_exp('exp3', 'Cori KNL, 2.8e7 sqrt ops/event', 'cyan', "s")
plot1.add_exp('exp4', 'Cori KNL, 2.8e8 sqrt ops/event', 'magenta', "s")
plot1.add_exp('exp5', 'Farm 18, 2.8e5 sqrt ops/event', 'green', "o")
plot1.add_exp('exp6', 'Farm 18, 2.8e6 sqrt ops/event', 'blue', "o")
plot1.add_exp('exp7', 'Farm 18, 2.8e7 sqrt ops/event', 'cyan', "o")
plot1.add_exp('exp8', 'Farm 18, 2.8e8 sqrt ops/event', 'magenta', "o")

plot1.create()

plot2 = PlotDef()
plot2.filename = "comp_scaling_coriknl"
plot2.title = "JANA2 computation scaling, Cori KNL"

plot2.add_exp('exp1', '2.8e5 sqrt ops/event', 'green', "s")
plot2.add_exp('exp2', '2.8e6 sqrt ops/event', 'blue', "s")
plot2.add_exp('exp3', '2.8e7 sqrt ops/event', 'cyan', "s")
plot2.add_exp('exp4', '2.8e8 sqrt ops/event', 'magenta', "s")

plot2.create(loc="upper right")

plot3 = PlotDef()
plot3.filename = "comp_scaling_farm18"
plot3.title = "JANA2 computation scaling, Farm 18"

plot3.add_exp('exp5', '2.8e5 sqrt ops/event', 'green', "o")
plot3.add_exp('exp6', '2.8e6 sqrt ops/event', 'blue', "o")
plot3.add_exp('exp7', '2.8e7 sqrt ops/event', 'cyan', "o")
plot3.add_exp('exp8', '2.8e8 sqrt ops/event', 'magenta', "o")
plot3.create(loc="center right")
