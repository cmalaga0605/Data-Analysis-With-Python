#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import sqlite3 as lite
## SQL database name and initialize the sql connection.
db_filename = r'mydb.db'
con = lite.connect(db_filename)
## Convert to dataframe and write to sql database.
df.to_sql('mytable', con, flavor='sqlite',
          schema=None, if_exists='replace', index=True,
          index_label=None, chunksize=None, dtype=None)
## Close the SQL connection
con.close()

