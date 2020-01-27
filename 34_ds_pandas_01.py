"""
Data Science/Analytics -> process of analyzing datasets to find useful information! 

"""

import pandas as pd

#create a data frame -> tabular data in 2-d format!
df = pd.read_csv('nyc_weather.csv')
print(df)

print(df['Temperature'].max())

print(df['EST'][df['Events']=='Rain'])

print(df['WindSpeedMPH'].mean())