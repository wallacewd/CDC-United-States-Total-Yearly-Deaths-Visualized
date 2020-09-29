"""
CDC Total United States Yearly Deaths - Visualized by week
Author: Dan Wallace
Date: 09/29/2020
Download 'Weekly Deaths by State and Age' from this CDC Link (csv format): https://www.cdc.gov/nchs/nvss/vsrr/covid19/excess_deaths.htm
Save to a folder, copy the file path and paste inside path='____" below (example included, will not work until you a provide propper file path)
"""
import numpy as np
import pandas as pd # Imports Panda's Library
import matplotlib.pyplot as plt
from matplotlib.pyplot import axes  # Imports matplotlib.pyplot and renames it to plt  # from matplot 
import matplotlib as mpl # Imports matplotlib and renames it to mp1
from matplotlib import style # In the matplotlib library, import style 

#-------------------------------------------------
# Paste csv file path here
#-------------------------------------------------

path = 'cdc_python/cdc_example_data.csv'

#-------------------------------------------------
# Create dataFrame
#-------------------------------------------------

# Creates a dataFrame named 'df' and used pd(pandas) to read the csv file above, and sets the index column to 'Week Ending Date'
df = pd.read_csv(path, index_col=['Week Ending Date']) 

# Displays the Column Names/Data Count/Object Type contained in the dataframe
df.info() 

#-------------------------------------------------
# dataFrame collection/organization 
#-------------------------------------------------

us_note = df['Week'] <= 30
print(us_note)

final_note = df[us_note]
print(final_note)

us_unweighted = final_note['Type']=='Unweighted'
print(us_unweighted) 

final = final_note[us_unweighted]
print(final) 

df_us = final['Jurisdiction']=='United States'      
print(df_us) 

final_us = final[df_us]                             
print(final_us.info())

# ct_deaths calls the pandas library and uses the crosstab() function to arrange the data
# in a way that we can plot the total deaths in the US by year against the weeks in the year
ct_deaths = pd.crosstab(final_us['Week'],final_us['Year'],values=final_us['Number of Deaths'],aggfunc="sum")

#-------------------------------------------------
# Begin Plotting
#-------------------------------------------------

mpl.rc('figure', figsize=(8, 6))                                                                                        # Sets the figure size width and height
mpl.__version__                                                                                                         # Outputs MatPlotLib version number in terminal 
style.use('seaborn-muted')                                                                                              # Graph theme 
mpl.rc('lines', linewidth=3)                                                                                            # Style of graph to use
                                  
ct_deaths.plot(label='Number of Deaths').grid(color='lightgrey', linestyle='solid')                                     # Plots the Number of deaths to the graph

plt.title('United States 2015-2020: Total Deaths by Week \n (All Age Groups Through First 15 Weeks)', fontsize=14)
plt.ylabel('Number of Deaths', fontsize=13)                                                                             # Changes the y-axis label to 'Number of Deaths'
plt.xlabel('Week', fontsize=13)                                                                                         # Changes the x-axis label to 'Deaths Reported by Week'
plt.subplot(111).set_xlim(1, 30)
dim=np.arange(1,31,1)
dim2=np.arange(45000,90000,5000)
plt.xticks(dim, fontsize=11)
plt.yticks(dim2, fontsize=11)

plt.show()             
