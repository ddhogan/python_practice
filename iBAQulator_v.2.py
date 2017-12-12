# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 17:05:01 2014
@author: donna
"""

# this next command is commented out because it's not needed yet
#from pandas import Series, DataFrame

#this command imports pandas and gives it a short-cut name
import pandas as pd

#print ("Please enter the file name of the data report from Skyline, excluding the .csv")

my_file = input(print ("Please enter the file name of the data report from Skyline, excluding the .csv"))

# import the iBAQ data from a .csv file into a data frame
df = pd.read_csv(my_file+'.csv')

# group all the rows according to accession number
grouped = df['Max Height'].groupby(df['Protein'])

# sum all numbers within each group, call this data set "height_sum"
height_sum = df.groupby('Protein').sum().add_prefix('sum')

#print(height_sum)
pd.merge(df, height_sum, left_on='Protein', right_index=True)

#write it all out to another .csv file
height_sum.to_csv('Protein_result_'+my_file+'.csv')