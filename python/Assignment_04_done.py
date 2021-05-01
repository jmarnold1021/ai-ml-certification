#!/usr/bin/env python
# coding: utf-8

# <img src="http://cfs22.simplicdn.net/ice9/new_logo.svgz "/>
# 
# # Assignment 02: Perform CDF and PDF
# 
# *The comments/sections provided are your cues to perform the assignment. You don't need to limit yourself to the number of rows/cells provided. You can add additional rows in each section to add more lines of code.*
# 
# *If at any point in time you need help on solving this assignment, view our demo video to understand the different steps of the code.*
# 
# **Happy coding!**
# 
# * * *

# #### 1: Import required library
# 

# In[1]:


from scipy.stats import norm


# #### 2: Perfrom Cumulative Distribution Function or CDF on variables, with loc 1 and scale 3
# 

# In[9]:


print(norm.rvs(loc=0, scale=1, size=20))

norm.cdf(10, loc=1, scale=3)


# #### 3: Perfrom Probability Density Function or PDF on variables, with loc 1 and scale 1

# In[8]:


norm.pdf(14, loc=1, scale=1)


# In[ ]:




