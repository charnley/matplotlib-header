#!/usr/bin/env python

import matplotlib.pyplot as plt

### Fonts
plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
# plt.rc('font',**{'family':'serif','serif':['Palatino']})
plt.rc('text', usetex=True)     # Use Latex formatting
plt.rc('text.latex', preamble=r'\usepackage{cmbright}') # Use sans-serif font

plt.rc('font', size=15)         # Fontsize
plt.rc('xtick', labelsize=15)   # Fontsize for x-ticks
plt.rc('ytick', labelsize=15)   # Fontsize for y-ticks


## Colors
# Default color cycle for plot lines
plt.rc('axes', color_cycle = [
        'e41a1c',
        '377eb8',
        '4daf4a',
        '984ea3',
        'ff7f00',
        'ffff33']);


### Lines
plt.rc('lines', antialiased = True) # render lines in antialised (no jaggies)


### AXES
# plt.rc('axes', facecolor='eeeeee')   # axes background color
plt.rc('axes', edgecolor='bcbcbc')     # axes edge color
plt.rc('axes', linewidth=2)            # edge linewidth
plt.rc('axes', grid=True)              # display grid or not
plt.rc('axes', titlesize='x-large')    # fontsize of the axes title
plt.rc('axes', labelsize='large')      # fontsize of the x any y labels
plt.rc('axes', labelcolor='111111')    # font color of labels
plt.rc('axes', axisbelow=True)         # whether axis gridlines and ticks are below the axes elements (lines, text, etc)


### TICKS
# see http://matplotlib.sourceforge.net/api/axis_api.html#matplotlib.axis.Tick
plt.rc('xtick.major', size = 0)      # major tick size in points
plt.rc('xtick.minor', size = 0)      # minor tick size in points
plt.rc('xtick.major', pad = 6)       # distance to major tick label in points
plt.rc('xtick.minor', pad = 6)       # distance to the minor tick label in points
plt.rc('xtick', color = '111111')    # color of the tick labels
plt.rc('xtick', direction = 'in')    # direction: in or out

plt.rc('ytick.major', size = 0)      # major tick size in points
plt.rc('ytick.minor', size = 0)      # minor tick size in points
plt.rc('ytick.major', pad = 6)       # distance to major tick label in points
plt.rc('ytick.minor', pad = 6)       # distance to the minor tick label in points
plt.rc('ytick', color = '111111')    # color of the tick labels
plt.rc('ytick', direction = 'in')    # direction: in or out


### GRIDS
plt.rc('grid', color='black')
plt.rc('grid', linestyle=':')
plt.rc('grid', linewidth=0.5)


### Legend
plt.rc('legend', fancybox = True)  # if True, use a rounded box for the legend, else a rectangle
#legend.isaxes        : True
#legend.numpoints     : 2      # the number of points in the legend line
#legend.fontsize      : large
#legend.pad           : 0.0    # deprecated; the fractional whitespace inside the legend border
#legend.borderpad     : 0.5    # border whitspace in fontsize units
#legend.markerscale   : 1.0    # the relative size of legend markers vs. original
# the following dimensions are in axes coords
#legend.labelsep      : 0.010  # the vertical space between the legend entries
#legend.handlelen     : 0.05   # the length of the legend lines
#legend.handletextsep : 0.02   # the space between the legend line and legend text
#legend.axespad       : 0.02   # the border between the axes and legend edge
#legend.shadow        : False


### FIGURE
# TODO Set for 1 column size (with crop please)

# See http://matplotlib.sourceforge.net/api/figure_api.html#matplotlib.figure.Figure
# plt.rc('figure', figsize = (11, 8))    # figure size in inches
# figure.dpi       : 80      # figure dots per inch

