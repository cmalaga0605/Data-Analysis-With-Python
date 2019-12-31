#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from time import strftime
from datetime import datetime
def standardize_date(the_date):
    """
    Standardizes a date
    :param the_date: the date to standardize
    :return formatted_date
    """
    formatted_date = ""
    # Convert what we have to a string, just in case
    the_date = str(the_date)
    # Handle missing dates, however pandas should have filled this in as missing
    if not the_date or the_date.lower() == "missing" or the_date == "nan":
        formatted_date = "MISSING"
    # Handle dates that end with 'XXXX', start with 'XX', or are less than 1900
    if the_date.lower().find('x') != -1:
        formatted_date = "Incomplete"
    # Handle dates that start with something like "0056"
    if the_date[0:2] == "00":
        formatted_date = the_date.replace("00", "19")
    # 03/03/15
    try:
        formatted_date = str(datetime.strptime(the_date, '%m/%d/%y').strftime('%m/%d/%y'))
    except:
        pass
    # 03/03/2015
    try:
        formatted_date = str(datetime.strptime(the_date, '%m/%d/%Y').strftime('%m/%d/%y'))
    except:
        pass
    # 0000-03-03
    try:
        if int(the_date[0:4]) < 1900:
            formatted_date = "Incomplete"
        else:
            formatted_date = str(datetime.strptime(the_date, '%Y-%m-%d').strftime('%m/%d/%y'))
    except:
        pass
    return formatted_date

df.birthdates = df.birthdates.apply(standardize_date)
df

