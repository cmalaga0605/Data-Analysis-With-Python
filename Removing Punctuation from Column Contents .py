#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import string
exclude = set(string.punctuation)

def remove_punctuation(x):
    try:
        x = ''.join(ch for ch in x if ch not in exclude)
    except:
        pass
    return x

df.address = df.address.apply(remove_punctuation)
df

