#!/usr/bin/env python
# coding: utf-8

# <img src="http://cfs22.simplicdn.net/ice9/new_logo.svgz "/>
# 
# # Assignment 01: Solve a Linear Algebra Problem
# 
# *The comments/sections provided are your cues to perform the assignment. You don't need to limit yourself to the number of rows/cells provided. You can add additional rows in each section to add more lines of code.*
# 
# *If at any point in time you need help on solving this assignment, view our demo video to understand the different steps of the code.*
# 
# **Happy coding!**
# 
# * * *

# #### 1: Import required libraries

# In[1]:


import numpy as np
from scipy import linalg


# #### 2: Formulate two linear equations based on the given scenario

# In[5]:


#There is a test with 30 questions worth 150 marks. The test has two types of questions:
#1. True or false – carries 4 marks each
#2. Multiple-choice – carries 9 marks each
# 4x + 9y = 150 and x + y = 30

tq_vars = np.array([[1,1],[4,9]])
tq = np.array([30,150])


# 
# #### 3: Apply a suitable method to solve the linear equation
# 

# In[6]:


linalg.solve(tq_vars,tq)


# In[ ]:




