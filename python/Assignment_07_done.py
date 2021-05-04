#!/usr/bin/env python
# coding: utf-8

# <img src="http://cfs22.simplicdn.net/ice9/new_logo.svgz "/>
# 
# # Assignment 01: Evaluate the Ad Budget Dataset of XYZ Firm
# 
# *The comments/sections provided are your cues to perform the assignment. You don't need to limit yourself to the number of rows/cells provided. You can add additional rows in each section to add more lines of code.*
# 
# *If at any point in time you need help on solving this assignment, view our demo video to understand the different steps of the code.*
# 
# **Happy coding!**
# 
# * * *

# #### 1: Import the dataset

# In[1]:


#Import the required libraries
import pandas as pd


# In[5]:


#Import the advertising dataset
adv_data = pd.read_csv('./Advertising Budget and Sales.csv', index_col=0)


# #### 2: Analyze the dataset

# In[18]:


#View the initial few records of the dataset
adv_data.head()


# In[7]:


#Check the total number of elements in the dataset
adv_data.size


# #### 3: Find the features or media channels used by the firm

# In[14]:


#Check the number of observations (rows) and attributes (columns) in the dataset
adv_data.shape


# In[15]:


#View the names of each of the attributes
adv_data.columns.format()


# #### 4: Create objects to train and test the model; find the sales figures for each channel

# In[16]:


#Create a feature object from the columns
x_features = adv_data[['TV Ad Budget ($)','Radio Ad Budget ($)','Newspaper Ad Budget ($)']]


# In[17]:


#View the feature object
x_features.head()


# In[21]:


#Create a target object (Hint: use the sales column as it is the response of the dataset)
y_features = adv_data[['Sales ($)']]


# In[22]:


#View the target object
y_features.head()


# In[24]:


#Verify if all the observations have been captured in the feature object
x_features.shape


# In[25]:


#Verify if all the observations have been captured in the target object
y_features.shape


# #### 5: Split the original dataset into training and testing datasets for the model

# In[27]:


#Split the dataset (by default, 75% is the training data and 25% is the testing data)
from sklearn.model_selection import train_test_split


# In[34]:


#Verify if the training and testing datasets are split correctly (Hint: use the shape() method)
x_train, x_test, y_train, y_test = train_test_split(x_features, y_features, random_state=1)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)


# #### 6: Create a model  to predict the sales outcome

# In[39]:


#Create a linear regression model
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x_train, y_train)


# In[40]:


#Print the intercept and coefficients 
print(lin_reg.intercept_)
print(lin_reg.coef_)


# In[41]:


#Predict the outcome for the testing dataset
y_pred = lin_reg.predict(x_test)
y_pred


# #### 7: Calculate the Mean Square Error (MSE)

# In[43]:


#Import required libraries for calculating MSE (mean square error)
from sklearn.metrics import mean_squared_error
import numpy as np


# In[44]:


#Calculate the MSE
np.sqrt(mean_squared_error(y_test, y_pred))


# In[ ]:




