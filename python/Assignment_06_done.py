#!/usr/bin/env python
# coding: utf-8

# <img src="http://cfs22.simplicdn.net/ice9/new_logo.svgz "/>
# 
# # Assignment 02: Evaluate the FDNY Dataset
# 
# *The comments/sections provided are your cues to perform the assignment. You don't need to limit yourself to the number of rows/cells provided. You can add additional rows in each section to add more lines of code.*
# 
# *If at any point in time you need help on solving this assignment, view our demo video to understand the different steps of the code.*
# 
# **Happy coding!**
# 
# * * *

# #### 1: View and import the dataset

# In[3]:


#Import the required libraries
import pandas as pd


# In[8]:


#Import the Fire Department of New York City (FDNY) file
fdny_data = pd.read_csv("./FDNY.csv")


# #### 2: Analyze the dataset

# In[11]:


#View the content of the data
fdny_data.describe


# In[7]:


#View the first five records
fdny_data.head()


# In[17]:


#Skip the duplicate header row
fdny_data = pd.read_csv("./FDNY.csv", skiprows=1)


# In[18]:


#Verify if the dataset is fixed
fdny_data.head()


# In[19]:


#View the data statistics (Hint: use describe() method)
fdny_data.describe()


# In[20]:


#View the attributes of the dataset (Hint: view the column names)
fdny_data.columns.format()


# In[21]:


#View the index of the dataset
fdny_data.index.format()


# #### 3: Find the total number of fire department facilities in New York city

# In[26]:


#Count number of records for each attribute
fdny_data.count()


# In[27]:


#view the datatypes of all three attributes
fdny_data.dtypes


# #### 4: Find the total number of fire department facilities in each borough

# In[29]:


#Select FDNY information boroughwise
fdny_borough_data = fdny_data.groupby('Borough')


# In[30]:


#View FDNY informationn for each borough
fdny_borough_data.size()


# #### 5: Find the total number of fire department facilities in Manhattan

# In[32]:


#Select FDNY information for Manhattan
fdny_manhattan_data = fdny_borough_data.get_group('Manhattan')


# In[33]:


#View FDNY information for Manhattan
fdny_manhattan_data


# In[ ]:




