#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('weather_data.csv')
df


# In[5]:


weather_data = {
'day':['01-01-2017','01-02-2017','01-03-2017','01-04-2017','01-05-2017','01-06-2017'],
'temperature':[32,35,28,24,32,31],
'event':['Rain','Sunny','Snow','Snow','Rain','Sunny']
}
df = pd.DataFrame(weather_data)
df


# In[6]:


df.shape


# In[7]:


df.head()


# In[8]:


df.head(2)


# In[9]:


df.tail()


# In[10]:


df.tail(2)


# In[11]:


df[3:6]


# In[13]:


df[0:2]


# In[14]:


df[:]


# In[16]:


df


# In[17]:


df.columns


# In[18]:


df['day']


# In[19]:


type(df['day'])


# In[20]:


df[['day', 'event']]


# In[22]:


df['temperature']


# In[23]:


df['temperature'].max()


# In[24]:


df[df['temperature']>=31]


# In[26]:


df[df['temperature']>31]


# In[28]:


df[df['temperature']==df['temperature'].max()]


# In[29]:


df[df['temperature'] == df['temperature'].min()]


# In[30]:


df.describe()


# In[31]:


df = pd.read_csv("weather_data.csv")


# In[32]:


df.describe()


# In[33]:


df

# In[34]:


df.set_index('day')


# In[36]:


df


# In[38]:


newdf = df.set_index('day')
newdf


# In[39]:


df.set_index('day', inplace=True)


# In[40]:


df


# In[41]:


df.index


# In[42]:


df.loc['1/3/2017']


# In[43]:


df.reset_index(inplace=True)


# In[44]:


df


# In[45]:


df.index


# In[47]:


df.set_index('event', inplace=True)


# In[48]:


df


# In[49]:


df.loc['Sunny']

