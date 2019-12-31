#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from sqlalchemy import create_engine

#connect to sql database
db_file = r'datasets/gradedata.db'
engine = create_engine(r"sqlite:///{}".format(db_file))

sql = 'SELECT * FROM test WHERE Grades in (76,77,78)'

sales_data_df = pd.read_sql(sql,engine)
sales_data_df.head()


# In[ ]:




