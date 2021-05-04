#!/usr/bin/env python
# coding: utf-8

# <img src="http://cfs22.simplicdn.net/ice9/new_logo.svgz "/>
# 
# # Assignment 01: Evaluate the FAA Dataset
# 
# *The comments/sections provided are your cues to perform the assignment. You don't need to limit yourself to the number of rows/cells provided. You can add additional rows in each section to add more lines of code.*
# 
# *If at any point in time you need help on solving this assignment, view our demo video to understand the different steps of the code.*
# 
# **Happy coding!**
# 
# * * *

# #### 1: VIew and import the dataset

# In[2]:


#Import necessary libraries
import pandas as pd


# In[43]:


#Import the FAA (Federal Aviation Authority) dataset
faa_data = pd.read_csv("./faa_ai_prelim.csv")


# #### 2: View and understand the dataset

# In[44]:


#View the dataset shape
faa_data.shape


# In[9]:


#View the first five observations
faa_data.head(5)


# In[14]:


#View all the columns present in the dataset
faa_data.columns.format()


# #### 3: Extract the following attributes from the dataset:
# 1. Aircraft make name
# 2. State name
# 3. Aircraft model name
# 4. Text information
# 5. Flight phase
# 6. Event description type
# 7. Fatal flag

# In[45]:


#Create a new dataframe with only the required columns
faa_filter_data = faa_data[['ACFT_MAKE_NAME','LOC_STATE_NAME','ACFT_MODEL_NAME','RMK_TEXT','FLT_PHASE','EVENT_TYPE_DESC','FATAL_FLAG']]


# In[21]:


#View the type of the object
type(faa_filter_data)


# In[46]:


#Check if the dataframe contains all the required attributes
faa_filter_data.head()


# #### 4. Clean the dataset and replace the fatal flag NaN with “No”

# In[50]:


#Replace all Fatal Flag missing values with the required output
faa_filter_data['FATAL_FLAG'].fillna(value='No', inplace=True)


# In[51]:


#Verify if the missing values are replaced
faa_filter_data.head()


# In[36]:


#Check the number of observations
len(faa_filter_data.index)


# #### 5. Remove all the observations where aircraft names are not available

# In[59]:


#Drop the unwanted values/observations from the dataset
faa_filter_data.dropna(subset=['ACFT_MAKE_NAME'], inplace=True)


# #### 6. Find the aircraft types and their occurrences in the dataset

# In[60]:


#Check the number of observations now to compare it with the original dataset and see how many values have been dropped
# old had 83...5 less
len(faa_filter_data.index)


# In[68]:


#Group the dataset by aircraft name
faa_make_count = faa_filter_data.groupby("ACFT_MAKE_NAME")


# In[69]:


#View the number of times each aircraft type appears in the dataset (Hint: use the size() method)
faa_make_count.size()


# #### 7: Display the observations where fatal flag is “Yes”

# In[70]:


#Group the dataset by fatal flag
faa_fatal_count = faa_filter_data.groupby("FATAL_FLAG")


# In[71]:


#View the total number of fatal and non-fatal accidents
faa_fatal_count.size()


# In[73]:


#Create a new dataframe to view only the fatal accidents (Fatal Flag values = Yes)
faa_fatal_count.get_group('Yes')


# In[ ]:




