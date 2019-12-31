#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def right(s, amount):
    return s[-amount]

def standardize_ssn(ssn):
    try:
        ssn = ssn.replace("-","")
        ssn = "".join(ssn.split())
        if len(ssn)<9 and ssn != 'Missing':
            ssn="000000000" + ssn
            ssn=right(ssn,9)
    except:
        pass
    
    return ssn

df.ssn = df.ssn.apply(standardize_ssn)
df

