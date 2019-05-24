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
    def __init__(self, dir, label, color):
        self.dir = dir
        self.label = label
        self.color = color


class PlotDef:
    def __init__(self, filename="", title="", description=""):
        self.filename = filename
        self.title = title
        self.description = description
        self.exps = []

    def add_exp(self, dir, label, color):
        self.exps.append(Experiment(dir, label, color))

    def create(self):
        plt.figure()
        plt.title(self.title)
        plt.xlabel('Nthreads')
        plt.ylabel('Rate (Hz)')
        for exp in self.exps:
            fname = exp.dir + "/rates.dat"

            # Load data using numpy
            nthreads,avg_rate,rms_rate = np.loadtxt(fname, skiprows=1,usecols=(0,1,2), unpack=True)
            minnthreads = nthreads.min()
            maxnthreads = nthreads.max()

            # Create plot using matplotlib
            plt.errorbar(nthreads, avg_rate, rms_rate,
                         linestyle='', ecolor='red',
                         elinewidth=1, capthick=1, marker='o',
                         ms=6, markerfacecolor=exp.color, label=exp.label)

            plt.xlim(minnthreads-1.0, maxnthreads+1.0)
            plt.grid(True)

        plt.legend()
        plt.savefig(self.filename + ".png")

