#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# To eliminate all the rows where the grades are too high:
df.loc[df['Grades'] <= 100]


# In[ ]:


# To change the out of bound values to the maximum or minimum allowed value, we can:
df.loc[(df['Grades'] >= 100,'Grades')] = 100

