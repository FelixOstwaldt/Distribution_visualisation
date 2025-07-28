# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 17:58:51 2025

@author: felix
"""

import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

import random

from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

# Import math Library
import math 

plot_df = pd.read_csv('Randomlists/plot_df_pic1.csv')


""" ---------------- """
sigma = .4**2
plot_df['ALPHAS'] =  (1/(sigma * math.sqrt(2*math.pi)))* np.exp(-1/2*((plot_df['Y']-.5) / sigma)**2)
plot_df['ALPHAS'] = plot_df['ALPHAS']/plot_df['ALPHAS'].max()
sns.scatterplot(data = plot_df, x = 'Y', y = 'ALPHAS')

""" ----------------- """

sigma = .1
plot_df['SIZE'] =  (1/(sigma * math.sqrt(2*math.pi)))* np.exp(-1/2*((plot_df['Y']-.5) / sigma)**2)
plot_df['SIZE'] = plot_df['SIZE'] * -1
plot_df['SIZE'] = plot_df['SIZE'] + 4
#plot_df['SIZE'] = plot_df['SIZE'] *100
#plot_df['SIZE'] = plot_df['SIZE']**3
sns.scatterplot(data = plot_df, x = 'Y', y = 'SIZE')

"""--------------------"""

plot_df['SIZE'] = .5 + (plot_df['Y'] ** 2)
sns.scatterplot(data = plot_df, x = 'Y', y = 'SIZE')


"""-------------------"""

sns.scatterplot(data = plot_df, x = 'Y', y = 'SIZE')

"""----------------"""

plot_df['SIZE'] = plot_df['SIZE'] *25
plot_df['SIZE'] = plot_df['SIZE']**2
plot_df['SIZE'] = plot_df['SIZE'] + 1

"""-----------------"""

plt.style.use('dark_background')

plot = plt.figure(figsize=(20, 20))

#alphas = plot_df['SIZE'] / plot_df['SIZE'].max()
#alphas = alphas - 1
#alphas = alphas * (-1)

plt.scatter(data = plot_df, x = 'X', y = 'Y'
            , marker = '.'
            , c = 'HUE', s = 'SIZE', alpha = plot_df['ALPHAS'], cmap = 'Greens')

#plot = plt.scatter(data = plot_df, x = 'X', y = 'Y', marker = '.', c = 'HUE', s = 1, cmap = 'Oranges', alpha = plot_df['ALPHAS'])

#canvas = FigureCanvas(plot)

plt.savefig("picture_2.png", dpi = 600, bbox_inches = "tight")