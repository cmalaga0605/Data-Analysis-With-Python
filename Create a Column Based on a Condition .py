#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

Location = "gradedata.csv"
df = pd.read_csv(Location)

df.head()


# In[ ]:


import numpy as np
df['isFailing'] = np.where(df['grade']<70, 'yes', 'no')
df.tail(10)


# In[ ]:


df['isFailingMale'] = np.where((df['grade']<70)  & (df['gender'] == 'male'), 'yes', 'no')
df.tail(10)

