#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[ ]:


df.hist()


# In[ ]:


df.hist(column="hours")


# In[ ]:


df.hist(column="hours", by="gender")

