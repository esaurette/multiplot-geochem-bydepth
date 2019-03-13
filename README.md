# multiplot-geochem-bydepth
Code for automating the creation of multi-plots of geochemistry data by depth

How to use this code:

1. Download all files
2. Input your data into the .xlsx template file
  2.1 Leave any missing values blank, all values except pH, Eo, Eh, Alkalinity are in micrograms per L
    2.1.1 Don't use any of the si columns yet... they are untested and will not have the correct units!!
  2.2 Save the AQ_CHEM sheet as a .csv file
3. Update the userinput.py file with the specifications for your plot
4. Run the main.py file
5. Enjoy your plot!
  5.1 Raise any issues or feature requests here
