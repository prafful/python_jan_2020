#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
df = pd.read_excel('weather_data.xlsx', "data")
df


# In[7]:


weather_data = {
'day':['01-01-2017','01-02-2017','01-03-2017','01-04-2017','01-05-2017','01-06-2017'],
'temperature':[32,35,28,24,32,31],
    'windspeed':[6,7,2,7,4,2],
'event':['Rain','Sunny','Snow','Snow','Rain','Sunny']
}


df


# In[9]:


weather_data = [
    ('01-01-2017',32, 6, 'Rain'),
    ('01-02-2017',35, 7, 'Sunny')
]
df = pd.DataFrame(data=weather_data, columns=['day', 'temperature','windspeed','event'] )
df


# In[14]:


weather_data = [
    {'day':'01-01-2017','temperature':32, 'windspeed':6, 'event':'Rain'},
    {'day':'01-02-2017','temperature':35, 'windspeed':7, 'event':'Sunny'}
]


# In[15]:


df = pd.DataFrame(data=weather_data, columns=['day', 'temperature','windspeed','event'])
df

