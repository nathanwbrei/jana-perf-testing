from plothelper import *

plot1 = PlotDef()
plot1.filename = "varying_opt_levels"
plot1.title = "Cori KNL: Varying optimization levels"
plot1.description = "blocksize=2MB, eventsize=0.5MB"

plot1.add_exp('exp1', 'without KNL optimizations', 'green')
plot1.add_exp('exp7', 'with KNL optimizations', 'blue')

plot1.create()


plot2 = PlotDef()
plot2.filename = "varying_block_size"
plot2.title = "Cori KNL: Varying entangled block size"

plot2.add_exp('exp1', 'blocksize=2MB, eventsize=0.5MB', 'green')
plot2.add_exp('exp4', 'blocksize=4MB, eventsize=0.5MB', 'blue')
plot2.add_exp('exp5', 'blocksize=8MB, eventsize=0.5MB', 'cyan')

plot2.create()


plot3 = PlotDef()
plot3.filename = "varying_event_size"
plot3.title = "Cori KNL: Varying event size"

plot3.add_exp('exp1', 'blocksize=2MB, eventsize=0.5MB', 'green')
plot3.add_exp('exp2', 'blocksize=2MB, eventsize=1MB', 'blue')
plot3.add_exp('exp3', 'blocksize=2MB, eventsize=2MB', 'cyan')

plot3.create()


