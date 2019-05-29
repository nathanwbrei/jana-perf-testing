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

    def create(self):
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


        plt.legend()
        plt.xlim(min_nthreads-1.0, max_nthreads+1.0)
        plt.grid(True)
        plt.savefig(self.filename + ".png")



plot1 = PlotDef()
plot1.filename = "new_jtest_scaling"
plot1.title = "Scaling of JTest (new)"

plot1.add_exp('exp1', 'Cori KNL, old engine', 'cyan', 'o')
plot1.add_exp('exp2', 'Cori KNL, new engine', 'blue', 'o')
plot1.add_exp('exp3', 'JLab Farm 14, old engine', 'cyan', 'v')
plot1.add_exp('exp4', 'JLab Farm 14, new engine', 'blue', 'v')
plot1.add_exp('exp5', 'JLab Farm 18, old engine', 'cyan', 's')
plot1.add_exp('exp6', 'JLab Farm 18, new engine', 'blue', 's')

plot1.create()