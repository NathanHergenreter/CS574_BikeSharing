#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# In[ ]:


def get_contest_train_df():
    return pd.read_csv('train.csv')

def get_contest_test_df():
    return pd.read_csv('test.csv')

def get_bike_sharing_df():
    return pd.read_csv('hour.csv')

