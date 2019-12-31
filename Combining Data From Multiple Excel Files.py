#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd 
import numpy as np 
import glob as g

all_data=pd.DataFrame()
for x in glob.glob('datasets/week/weekdata*.xlsx'): #looped through the directory
    print(x) #printing just to make sure
    df = pd.read_excel(x) #read each excel file
    all_data = all_data.append(df,ignore_index = True) #combining the files
all_data.describe()#describe the new file

