# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 11:57:40 2018

@author: Kia
"""
#importing necesary libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
#%matplotlib inline 
from sklearn import preprocessing 
from sklearn.metrics import mean_squared_error 
## preprocessing 

pubs_df = pd.read_csv('open_pubs.csv')
print(pubs_df.info())
#pubs_df.show(20)
#plot successlevel of each generation

# color the data from very green (high successrate) to red (low successrate)
# can plot both mean successrate as well as highest successrate for that generation..


#print(pubs_df.head(10))
print(pubs_df.shape[0])
leeds_pubs_df = pubs_df.loc[pubs_df['local_authority'] == 'Leeds']
print(leeds_pubs_df.shape[0])

leeds_before_drop = leeds_pubs_df

cols_to_drop  = ['fas_id','address', 'postcode', 'latitude', 'longitude', 'local_authority']
leeds_pubs_df.drop(cols_to_drop, axis = 1, inplace = True)
print(leeds_pubs_df.head(5))

#create TSV file
leeds_before_drop.to_csv('data.tsv', header = False, index = False,  sep = '\t')
leeds_pubs_df.to_csv('data_pubs.csv', header = False, index = True)

#generate a population


