# -*- coding: utf-8 -*-
"""
Created on Fri May  1 16:19:24 2020

@author: 128dm
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

cars = pd.read_csv('USA_cars_datasets.csv')
cars.head()
print(cars.shape)

cars.isnull().any().any()

str_list = []
for colname, colvalue in cars.iteritems():
    if type(colvalue[2]) == str:
        str_list.append(colname)
print(str_list)        
num_list = cars.columns.difference(str_list)

cars_num = cars[num_list]
cars_num = cars_num.drop("lot", axis=1)
cars_num = cars_num.drop("Unnamed: 0", axis = 1)

f, ax = plt.subplots(figsize=(14, 11))
plt.title('Pearson Correlation of Cars Numerical Features')
sns.heatmap(cars_num.astype(float).corr(), linewidths = 0.25, vmax = 1.0, square = True, cmap = "cubehelix_r", linecolor = 'k', annot = True)

sns.jointplot('mileage', 'price', data = cars, kind='hex', cmap='afmhot', size=11 )
cars.plot(y= 'mileage', x ='price',kind='hexbin',gridsize=20, sharex=False, 
       colormap='cubehelix', title='Hexbin of price and mileage')

plt.style.use('dark_background')

cars_price_year = cars_num.drop('mileage', axis = 1)

yearlySales = cars_price_year.groupby(['year']).sum()
yearlySales.plot(kind = 'bar', colormap = 'Blues', grid = False, figsize = (11,11))
plt.title('Stacked Barplot of Global Yearly Sales')
plt.ylabel('price')  

cars2019 = cars[(cars['year'] == 2019)]

from collections import Counter

models_2019 = cars2019['brand']
count_models = Counter(models_2019)
count_models = pd.DataFrame.from_dict(count_models, orient='index')

count_models.plot(kind = 'bar', colormap = 'Blues', grid = False, figsize = (11,11))
plt.title('Quantity of cars in 2019')
plt.ylabel('Number of sold cars')  
















