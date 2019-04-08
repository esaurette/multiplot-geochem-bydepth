# -*- coding: utf-8 -*-
"""
Mine Waste Plots for Geochemistry vs. Depth 
Emily Saurette (with help and support from future Dr. Hilger)
March 5, 2019

"""

# importing modules
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import math as m
from roundto import nice_numbers
from titledictionary import titledict
from titledictionary import phreeqc
from titledictionary import aqgeochem
import userinput as ui
import style as s

#changing the size of the sub and superscripts relative to the font size
matplotlib.mathtext.SHRINK_FACTOR = 0.75
matplotlib.mathtext.GROW_FACTOR = 1.0/0.75

# read the csv file and convert it to a pandas data structure with headers and column indexes
data = pd.read_csv(ui.file, header=0, index_col=0) 
data = data.sort_values(by=[ui.y,'Month-Year'])

# creating the overall figure and subplots
# fig represents the variable name of the overall figure
# plt.subplot(ROWS, COLUMNS) - this is where you tell the function how many plots you want and how they will be organized, 2 ROWS of 6 COLUMNS = 12 subplots

fig, axes = plt.subplots(ui.row,ui.col) 

i=0 # counter for the for loop
titles = [] #initializes an empty list for the subplot titles
for i in range(len(ui.graphs)): # this for loop creates the subplot titles by pulling them from the dictionary created in the title_dictionary module
    titles.append(titledict[ui.graphs[i]])
    i += 1
  
times = data['Month-Year'].unique().tolist()

t= 0 #counter for the time-series loop    

i=0 # counter for the for loop

for ax in axes.flatten():
         
    x_max = m.ceil(data[ui.graphs[i]].max())
    x_min = m.floor(data[ui.graphs[i]].min())
    y_max = m.ceil(data[ui.y].max())
    y_min = m.floor(data[ui.y].min())
   
    # find the number of places in the max value for x
    x_factor = len(str(x_max))
    
    if x_factor >= 6:
        new_col = ui.graphs[i]+'_gL'
        titles[i] += '\n$\\regular^{(g\ L^{-1})}$'
        data[new_col] = data[ui.graphs[i]]/10**6
        x_max = int(m.ceil(data[new_col].max()))
        x_min = int(round(data[new_col].min()))
        
    elif x_factor > 3:
        new_col = ui.graphs[i]+'_mgL'
        titles[i] += '\n$\\regular^{(mg\ L^{-1})}$'
        data[new_col]=data[ui.graphs[i]]/10**3
        x_max = int(m.ceil(data[new_col].max()))
        x_min = int(round(data[new_col].min()))
        
    else:
        new_col = ui.graphs[i]
        data[new_col]=data[ui.graphs[i]]/1
        while ui.graphs[i] != 'pH' and ui.graphs[i] != 'Eh' and ui.graphs[i] != 'Alkalinity (mg/L as CaCO3)' and (ui.graphs[i] in phreeqc) == False:
            titles[i] += '\n$\\regular^{(\mu g\ L^{-1})}$'
            break   
    
    for t in range(len(times)):
        data_by_date = data.loc[data['Month-Year'] == times[t]]
        data_by_date = data_by_date.dropna(subset=[new_col])
        ax.plot(data_by_date[new_col], data_by_date[ui.y], marker=ui.markers[t], color=ui.colors[t], **s.subplotstyles)
        t += 1
        
    t=0    #resetting the t loop counter
    
    if (ui.graphs[i] in aqgeochem) == True and ui.graphs[i] != 'pH':
        ax.axis([0, nice_numbers(x_max, ui.xticks), 0, y_max])
        ax.set_xticks(np.around(np.linspace(0, nice_numbers(x_max, ui.xticks), ui.xticks), decimals=1))
        
    elif (ui.graphs[i] in phreeqc) == True:
        if data[ui.graphs[i]].min() > 0:
            phreeqc_min = -1

        else:
            phreeqc_min = m.floor(data[ui.graphs[i]].min())
            
        if data[ui.graphs[i]].max() < 0:
            phreeqc_max = 1

        else:
            phreeqc_max = m.ceil(data[ui.graphs[i]].max())

        ax.axis([phreeqc_min, phreeqc_max, 0, y_max])
        ax.set_xticks(np.around(np.linspace(phreeqc_min, phreeqc_max, ui.xticks), decimals=1))
        ax.vlines(0, 0, 5, **s.groundwaterstyle)
        
    else:
        ax.axis([nice_numbers(x_min, ui.xticks), nice_numbers(x_max, ui.xticks), 0, y_max])
        ax.set_xticks(np.around(np.linspace(nice_numbers(x_min, ui.xticks), nice_numbers(x_max, ui.xticks), ui.xticks), decimals=1))
    
    ax.set_yticks(np.linspace(0, y_max, ui.yticks))
    
    # if the user input for ground water table is a number, add a dashed line and open down triangle to represent it in each plot
    if ui.ground_water_table != False:
        ax.hlines(ui.ground_water_table, 0, 9999, **s.groundwaterstyle)
        ax.annotate(r'$\triangledown$', (nice_numbers(x_max, ui.xticks)*0.8, ui.ground_water_table))
    
    first_plot_in_row = [ui.col*n for n in range(ui.row)]
    if i in first_plot_in_row: #the first graph of each row should have a y-axis label
        ax.set_ylabel(titledict[ui.y])
        
    s.sub_plot_format(ax, titles, i)
    
    i += 1

#axes[0,4].axis([0, 3, 16.0, 0])
#axes[0,4].set_xticks(np.linspace(0,3,3))
if ui.isTimeSeries == True:
    handles, labels = ax.get_legend_handles_labels()
    fig.legend(handles, times, **s.legendstyle)

fig.tight_layout(pad=0.5)

# combines the specified figure title and file type to create the output file that will be saved
filename= ui.fig_title + ui.file_type

# saves the figure, bbox_inches ='tight' specifies that no extra space should be includes around the perimeter of the figure
fig.savefig(filename, bbox_inches='tight')
