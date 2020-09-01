#!/usr/bin/env python
# coding: utf-8

# ## Importing important libraries for this assignment

# In[1]:


import slate3k as slate
import numpy as np
import pandas as pd


# ## Initializtion the variable and creating empty list 

# In[2]:


i=4
arr=[]


# ## loop for opening multiple PDF profiles and append to list

# In[3]:


while(i<=53):    
    text=slate.PDF(open('Profile ('+str(i)+').pdf', 'rb')).text()
    text
    i=i+1
    arr=np.append(arr,text)
        
## Converting list to DataFrame        
arr=pd.DataFrame(arr)


# ## Printing command for DataFrame

# In[4]:


print(arr)


# ## Saving DataFrame in CSV 

# In[5]:


arr.to_csv (r'Profile_text.csv' ,index = False, header=True)


# In[ ]:




