#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegress = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]

GradeList = zip(names,grades,bsdegress,msdegrees,phddegrees)
df = pd.DataFrame(data = GradeList, columns=['Names','Grades','BS','MS','PhD'])
df


# In[ ]:


# We can drop a column by simply adding:
df.drop('PhD', axis=1)


# In[ ]:


# We can add a column filled with 0's by setting the new column name equal to a 0.
df['HighSchool']=0


# In[ ]:


# If you want to set the new columns to equal null values, you can do that too.
df['PreSchool'] = np.nan


# In[ ]:


d = ([0,1,0,1,0])
s = pd.Series(d, index= df.index)
df['DriversLicense'] = s
df

