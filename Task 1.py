# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 00:25:11 2021

@author: HP
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
dataset=pd.read_csv("Wuzzuf_Jobs.csv")
dataset.describe()
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values =np.nan, strategy = 'most_frequent')
dataset.drop_duplicates(subset=["Title","Company", "Location", "Type" ,"Level","YearsExp","Country","Skills" ],keep="first",inplace=True)
y=dataset['Company'].value_counts()
print('The most demanding 3 companies for jobs are:', y.index[0:3])
plt.pie(y)
plt.show()
x=dataset['Title'].value_counts()
print ('The most popular 3 job titles are: ', x.index[0:3] )
fig = plt.figure(figsize = (5, 5))
plt.bar(x.index[0:3], x[0:3], color ='maroon',width = 0.2)
plt.xlabel("Job titles")
plt.ylabel("Number of job titles")
plt.title("The most popular 3 job titles")
plt.show()
areas=dataset['Location'].value_counts()
print ('The Most popular areas are: ', areas.index[0:5] )
fig = plt.figure(figsize = (8, 8))
plt.bar(areas.index[0:5], areas[0:5], color ='red',width = 0.2)
plt.xlabel("Areas")
plt.ylabel("Number of frequency")
plt.title("The Most popular areas")
plt.show()
Skills=dataset['Skills'].value_counts()
print(Skills[:], Skills.index[:])


