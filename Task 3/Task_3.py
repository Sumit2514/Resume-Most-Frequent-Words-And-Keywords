#!/usr/bin/env python
# coding: utf-8

# ## Importing important libraries for the assignmnent

# In[1]:


import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
from rake_nltk import Rake
import nltk


# ## Loading the dataset

# In[2]:


data= pd.read_csv("Profile_text.csv")


# ##  Tokenized sentences into words

# In[3]:


data['tokenized_sents']= data.apply(lambda row: nltk.word_tokenize(row['0']), axis=1)


# ## Removal of stop words

# In[4]:


stop = stopwords.words('english')


# In[5]:


data['tokenized_sents']=data['tokenized_sents'].apply(lambda x: [item for item in x if item not in stop])


# ## Display top five row of dataset ,showing tokenized words

# In[6]:


data.head()


# ## Extracting importnant keyword of each profile using RAKE library

# In[7]:


data['Key_words'] = ''
r = Rake()
for index, row in data.iterrows():
    r.extract_keywords_from_text(row['0'])
    key_words_dict_scores = r.get_word_degrees()
    row['Key_words'] = list(key_words_dict_scores.keys())


# ## Displaying top five row of dataset , showing keyword for each profile

# In[8]:


data.head()


# ## Saving DataFrame in CSV

# In[9]:


data.to_csv (r'C:\Users\Sumit Ranjan\Downloads\Profile_keyword.csv' ,index = False, header=True)


# In[ ]:




