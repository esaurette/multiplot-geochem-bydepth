# -*- coding: utf-8 -*-
"""
User Specified Plotting Inputs
Emily Saurette
March 12, 2019
"""

# convert the standard excel file template with your data to a csv file
file = "C:\\Users\\YourName\\Desktop\\Yourfile.csv" # input the path of the .csv file you would like to use data from

fig_title = "Title" # what would you like the file name to be?

file_type = ".pdf" # what type of file would you like the figure to save as? Options: .pdf, .png, .ps, .eps, .svg

row = 2 # integer, number of rows of plots

col = 6 # integer, number of columns of plots

xticks = 3 # integer, number of ticks you would like on the x-axis

yticks = 6 # integer, number of ticks you would like on the y=axis

# Create a list of the graphs you would like to include in your figure from starting at the top left (ax[0,0]) moving right (ax[0,5]), returning to the bottom left (ax[1,0]) and ending in the bottom right (ax[1,11])
graphs = ['pH', 'Eh', 'Cl', 'Zn', 'S(6)', 'Fe', 'Sb', 'Se', 'Mo', 'Pb', 'Sr', 'Co'] # list of graphs you would like in the plot, these are the x values

''' Currently options for graphs are: 'CORE', 'TOP (mbgs)', 'BOTTOM (mbgs)', 'LOA (cm)',
       'SAMPLE DEPTH (mbgs)', 'Month-Year', 'pH', 'Eo', 'Eh', 'pe',
       'Alkalinity Digits Titrated (to pink endpoint)',
       'Alkalinity Sample Volume (mL)', 'Alkalinity (mg/L as CaCO3)', 'Ca',
       'Na', 'Li', 'Be', 'B', 'Mg', 'Al', 'Si', 'P', 'K', 'Ti', 'V', 'Cr',
       'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'As', 'Se', 'Sr', 'Mo', 'Ag', 'Cd',
       'Sn', 'Sb', 'Cs', 'Ba', 'Tl', 'Pb', 'U', 'F', 'Cl', 'N(3)', 'Br',
       'N(5)', 'S(6)', 'S(2)', 'Formate', 'DOC', 'PO4-P', 'NH4-N', 'Fe(2+)',
       'S(2-)', 'pct_err', 'si_Calcite', 'si_Siderite', 'si_Gibbsite', 'si_Alunite', 
       'si_Gypsum', 'si_Anglesite', 'si_Jarosite-K', 'si_Melanterite','si_Epsomite',
       'si_Jarositess', 'si_JarositeH', 'si_Jarosite-Na', 'si_Fe(OH)3(a)','si_Goethite',
       'si_Fe(OH)2' '''
       
y = 'SAMPLE DEPTH (mbgs)' # the column you would like to use for the y-axis values

markers = ["o","s", "^", "D", "v"] # list of symbols for multi-line plots

colors = ["b", "g", "m", "c", "y"] # list of colours for multi-line plots

ground_water_table = 5.1 # if you have a depth for the groundwater table enter it here, if not this variable should be False

isTimeSeries = True #if you have a time-series and would like a legend this variable should = True, if not it should = False 
