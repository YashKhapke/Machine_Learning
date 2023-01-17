#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd
import numpy as np
import matplotlib 


# In[2]:


dataset=pd.read_csv('/home/pg/Downloads/Iris Dataset/iris.csv')


# In[3]:


dataset.head()


# In[4]:


df = spreadsheet.sort_values('sepal.length',ascending=False)


# In[5]:


df = dataset.sort_values('sepal.length',ascending=False)


# In[6]:


df.head()


# In[7]:


df[0:2]


# In[8]:


df.loc[df['petal.length']>6.5]


# In[10]:


print("Maximum value : ",df.sepal.length.max())
print("Minimum value : ",df.sepal.length.min())


# In[11]:


df = pd.DataFrame(dataset)


# In[12]:


print("Maximum value : ",df.sepal.length.max())
print("Minimum value : ",df.sepal.length.min())


# In[13]:


print(df)


# In[14]:


df.columns


# In[15]:


df.rows


# In[16]:


df.columns


# In[19]:


groupby_.get_group(variety).agg([np.mean,np.median,np.std,np.var ])


# In[24]:


df.select_dtypes(include=np.number).columns.tolist()


# In[25]:


df.select_dtypes(include=['object']).columns.tolist()


# In[26]:


df.plot.hist('sepal.length')


# In[30]:


x = np.random.normal('sepal.length')

plt.hist(x)
plt.show() 


# In[36]:


df.drop(labels=['sepal.width'],axis=1,inplace=True)


# In[37]:


df.head()


# In[38]:


df.isna().sum()


# In[39]:


numeric_col = ['sepal.length','petal.length','petal.width']


# In[41]:


dataset.boxplot(numeric_col)


# In[ ]:




