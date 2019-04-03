# -*- coding: utf-8 -*-
"""
Plot Style Elements
Emily Saurette
March 12, 2019
"""

subplotstyles = {
        'markerfacecolor': 'w',
        'linewidth': 1,
        'markersize': 5
        }

groundwaterstyle = {
        'linestyle':'dashed', 
        'linewidth': 1
        }

legendstyle = {
        'loc': 8,
        'ncol': 4,
        'borderaxespad': 0,
        'fontsize': 'x-small',
        'fancybox': False,
        'frameon': False
        }

def sub_plot_format(ax, titles, i):
    '''takes the variables ax, and iterable titles and a counter i, and produces the formatting shared across all subplots'''
    ax.invert_yaxis()
    ax.xaxis.tick_top()
    ax.tick_params(direction="inout", which="both", labelsize=7, length=7)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlabel(titles[i], horizontalalignment="center", multialignment="center", fontsize=8)
    ax.xaxis.set_label_position('top')
