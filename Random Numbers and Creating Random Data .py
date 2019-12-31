#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from numpy import random
fnames = ['Bob','Jessica','Mary','John','Mel']
lnames = ['Smith', 'Jones', 'Johnson', 'Jackson', 'Mallory', 'Wolf']
random.seed(500)
random_fnames = [fnames[random.randint(low=0,high=len(fnames))] 
                for i in range(1000)]   
random_lnames = [lnames[random.randint(low=0,high=len(lnames))] 
                for i in range(1000)]    
satscores = [random.randint(low=400, high=1600)
         for i in range(1000)]
SatScoreList = list(zip(random_fnames, random_lnames, satscores ))
df = pd.DataFrame(data = SatScoreList, columns=['first', 'last', 'sat'])

