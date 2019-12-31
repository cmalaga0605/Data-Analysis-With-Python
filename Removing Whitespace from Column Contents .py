#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def remove_whitespace(x):
    try:
        x = ''.join(x.split())
    except:
        pass
    return x

df.address = df.address.apply(remove_whitespace)
df

