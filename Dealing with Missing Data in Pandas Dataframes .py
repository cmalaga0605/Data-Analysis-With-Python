#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
df = pd.read_csv("gradedatamissing.csv")
df.head()


# In[ ]:


# To drop all the rows with missing (NaN) data:
df_no_missing = df.dropna()
df_no_missing


# In[ ]:


# To add a column filled with empty values:
import numpy as np
df['newcol'] = np.nan
df.head()


# In[ ]:


# To drop any columns that contain nothing but empty values.
df.dropna(axis=1, how='all')


# In[ ]:


# To replace all empty values with zero:
df.fillna(0)


# In[ ]:


# To fill in missing grades with the mean value of grade: 
df["grade"].fillna(df["grade"].mean(), inplace=True)


# In[ ]:


# Fill in missing grades with each gender's mean value of grade:
df["grade"].fillna(df.groupby("gender")["grade"].transform("mean"), inplace=True)


# In[ ]:


# To select the rows of df where age is not NaN and gender is not NaN.
df[df['age'].notnull() & df['gender'].notnull()]

