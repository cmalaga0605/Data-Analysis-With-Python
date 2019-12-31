#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

Location = "gradedata.csv"
df = pd.read_csv(Location)

df.head()


# In[ ]:


def singlename(fn, ln):
    return fn + " " + ln


# In[ ]:


df['fullname'] = singlename(df['fname'], df['lname'])
df.head(10)

