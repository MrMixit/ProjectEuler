#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Problem 5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# In[27]:


import math
minimum = 1
for i in range(1,21): # For each number, only multiply our minimum 
    minimum = int(i)*int(minimum)/math.gcd(int(i),int(minimum))
    
print(minimum)


# In[ ]:




