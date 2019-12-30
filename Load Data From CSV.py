#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd #Imported the pandas library 
Location = 'Documents/Python_Data_Analysis/USA_Accident_Feb2016_March2019/us-accidents/US_Accidents_May19.csv' #set the location of the csv
df = pd.read_csv(Location) #created the dataFrame
pd.set_option('display.max_columns',None) #took of restrictions in the number of columns that are shown
pd.set_option('display.max_rows',None) #took of restrictions in the number of rows that are shown
df.head(201)#Printed the dataFrame with 200 rows of data


# In[ ]:





# In[ ]:




