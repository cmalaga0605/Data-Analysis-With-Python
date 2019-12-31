#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# To indicate the duplicate rows, we can simply run the following:
df.duplicated()


# In[ ]:


# To show the dataset without duplicates, we can run this code:
df.drop_duplicates()


# In[ ]:


# To drop duplicate rows where only certain values indicate duplication
df.drop_duplicates(['Names'], keep='last')

