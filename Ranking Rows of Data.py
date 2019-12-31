#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

Location = "gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[ ]:


df['graderanked'] = df['grade'].rank(ascending=1)
df.tail()


# In[ ]:


df[df['graderanked'] < 21]


# In[ ]:


df[df['graderanked'] < 6].sort_values('graderanked')

