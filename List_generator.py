# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 13:37:23 2025

@author: felix
"""

import random
import pandas as pd


# create set of lists

N = 10000

randomlist_x = []
for i in range(0,N):
    n = random.random()
    randomlist_x.append(n)


randomlist_y = []
for i in range(0,N):
    n = random.gauss(mu=0.5, sigma=.1)
    randomlist_y.append(n)
    
randomlist_hue = []
for i in range(0,N):
    n = random.gauss(mu=0.0, sigma=1.0)
    randomlist_hue.append(n)
    
randomlist_alphas = []
for i in range(0,N):
    n = random.random()
    randomlist_alphas.append(n)
    
    


#safe lists in files

# Creating a dictionary
data_x = {'X': randomlist_x}

# Creating DataFrame
randomDF_x = pd.DataFrame(data_x)

# Saving to CSV
randomDF_x.to_csv('Randomlists/Randomlist_x.csv', index=False)

#the same for the other lists


""" Y-axis coordinates"""
# Creating a dictionary
data_y = {'Y': randomlist_y}

# Creating DataFrame
randomDF_y = pd.DataFrame(data_y)

# Saving to CSV
randomDF_y.to_csv('Randomlists/Randomlist_y.csv', index=False)


""" hue lists """
# Creating a dictionary
data_hue = {'HUE': randomlist_hue}

# Creating DataFrame
randomDF_hue = pd.DataFrame(data_hue)

# Saving to CSV
randomDF_hue.to_csv('Randomlists/Randomlist_hue.csv', index=False)


""" alphas list """
# Creating a dictionary
data_alphas = {'ALPHAS': randomlist_alphas}

# Creating DataFrame
randomDF_alphas = pd.DataFrame(data_alphas)

# Saving to CSV
randomDF_alphas.to_csv('Randomlists/Randomlist_alphas.csv', index=False)

