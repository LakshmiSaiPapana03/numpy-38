#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
rand_num = np.random.normal(0,1,25)
print("25 random numbers sampled from a standard normal distribution:")
print(rand_num)


# In[3]:


np.linspace(0, 1, 20)


# In[38]:


array = np.arange(1,101).reshape(10,10)
array


# In[39]:


print(array[1])
print(array[5])
print(array[6])


# In[43]:


array[3:11,]


# In[40]:


array[:,4:9]


# In[44]:


array[3:6,2:9]


# In[45]:


array = np.random.randint(0,1,size=1000)
print(array);


# In[46]:


import numpy
values = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(values)

print(x)


# In[47]:


y = numpy.median(values)
print(y)


# In[49]:


from scipy import stats

z=stats.mode(values)
print(z)


# In[50]:


import numpy as np
arr = [20, 2, 7, 1, 34]
np.std(arr)


# In[ ]:




