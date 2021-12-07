#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

from csv_reader import *


# In[9]:


def get_bike_sharing_df_clean():
    # Copy orig to new df
    bike_sharing_df_orig = get_bike_sharing_df()
    bike_sharing_df = bike_sharing_df_orig.copy()

    no_snow = [ 5, 6, 7, 8, 9, 10]
    medium_snow = [3, 4, 11, 12]
    heavy_snow = [1, 2]
    bike_sharing_df['no_snow'] = bike_sharing_df.mnth.apply(lambda x: 1 if x in no_snow else 0)
    bike_sharing_df['medium_snow'] = bike_sharing_df.mnth.apply(lambda x: 1 if x in medium_snow else 0)
    bike_sharing_df['heavy_snow'] = bike_sharing_df.mnth.apply(lambda x: 1 if x in heavy_snow else 0)
    
    #bike_sharing_df['spring'] = bike_sharing_df.season.apply(lambda x: 1 if x == 1 else 0)
    #bike_sharing_df['summer'] = bike_sharing_df.season.apply(lambda x: 1 if x == 2 else 0)
    #bike_sharing_df['fall'] = bike_sharing_df.season.apply(lambda x: 1 if x == 3 else 0)
    #bike_sharing_df['winter'] = bike_sharing_df.season.apply(lambda x: 1 if x == 4 else 0)

    bike_sharing_df.drop(['instant', 'dteday', 'mnth', 'season', 'yr', 'weekday', 'temp', 'casual', 'registered'], axis=1, inplace=True)

    return bike_sharing_df


# In[10]:


get_bike_sharing_df_clean().head(5)

# In[11]:

from sklearn.preprocessing import MinMaxScaler

def get_bike_sharing_df_clean_mod():
    # Copy orig to new df
    bike_sharing_df_orig = get_bike_sharing_df_clean()
    bike_sharing_df = bike_sharing_df_orig.copy()
    scaler = MinMaxScaler()
    
    scaled = scaler.fit_transform(bike_sharing_df)
    
    return pd.DataFrame(scaled, columns=['hr', 'holiday', 'workingday', 'weathersit', 'atemp', 'hum', 'windspeed', 'cnt', 'no_snow','medium_snow','heavy_snow'])

# In[12]:
get_bike_sharing_df_clean_mod().head(5)
