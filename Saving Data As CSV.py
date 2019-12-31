#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
id_ = [1,2,3,4,5,6,7,8,9,10] #Create id column
Fname = ['Cris','Juliana','Boneque','Telly','Tony','George','Monica','Roberta','Desiree','Henny'] #Create first name column
Lname = ['Mallag','Lopez','Malaga','Merryd','Inpenny','Rennt','Bob','UUB','Temb','Yud'] #Create last name column
State = ['Florida','California','New York','Georgia','Washington','New Jersey','Tennessee','New Hampshire','Kentucky','Florida'] #Create state column
City = ['Tampa','Sacremento','New York City','Atlanta','Olympia','Trenton','Nashville','Concord','Frankfort','Miami'] #create city column

Together = zip(id_,Fname,Lname,State,City) #Combine list with the zip function and assign to a variable
df = pd.DataFrame(data = Together,columns = ['Id','Fname','Lname','State','City']) #Create dataframe 
df


# In[4]:


df.to_csv('Documents/Python_Data_Analysis/ClientInfo.csv',index = False , header = True) #Saved File as a csv to the director


# In[ ]:




