#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
path="http://archive.ics.uci.edu/ml/machine-learning-databases/"
directory="iris/iris.data"
newfilereference=path+directory
dataread=pd.read_csv(newfilereference,header=None)
dataread.columns=["sepalLength","sepalWidth","petalLength","petalWidth","Class"]
print(dataread.info())
print(dataread.head())
print(dataread.tail())


# In[ ]:




