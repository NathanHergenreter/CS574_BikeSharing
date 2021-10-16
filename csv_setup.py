#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

from csv_reader import *


# In[32]:


def get_bike_sharing_df_clean():
    # Copy orig to new df
    bike_sharing_df_orig = get_bike_sharing_df()
    bike_sharing_df = bike_sharing_df_orig.copy()

    bike_sharing_df['spring'] = bike_sharing_df.season.apply(lambda x: 1 if x == 1 else 0)
    bike_sharing_df['summer'] = bike_sharing_df.season.apply(lambda x: 1 if x == 2 else 0)
    bike_sharing_df['fall'] = bike_sharing_df.season.apply(lambda x: 1 if x == 3 else 0)
    bike_sharing_df['winter'] = bike_sharing_df.season.apply(lambda x: 1 if x == 4 else 0)

    bike_sharing_df.drop(['instant', 'dteday', 'season', 'yr', 'temp', 'casual', 'registered'], axis=1, inplace=True)

    return bike_sharing_df

