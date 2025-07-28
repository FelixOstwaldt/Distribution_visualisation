# -*- coding: utf-8 -*-
"""
Created on Mon Jul 

@author: felix
 """
 
# import dependencies

import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt



from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas



randomlist_x = pd.read_csv('Randomlists/Randomlist_x.csv')
randomlist_y = pd.read_csv('Randomlists/Randomlist_y.csv')
randomlist_hue = pd.read_csv('Randomlists/Randomlist_hue.csv')
randomlist_alphas = pd.read_csv('Randomlists/Randomlist_alphas.csv')


#plot the histogram of the set of y-axis values. Should be normal distributed
plt.hist(randomlist_alphas, bins = 50)



#create pandas dataframe
"""plot_df = pd.DataFrame({'X' : randomlist_x, 'Y' : randomlist_y, 'HUE' : randomlist_hue
                        #, 'ALPHAS' : randomlist_alphas
                       })
"""

plot_df = pd.DataFrame(pd.concat([randomlist_x , randomlist_y,  randomlist_hue, randomlist_alphas], axis = 1))


plot_df['SIZE'] = plot_df['Y'] - .5
randomlist_SIZE = []
for i in plot_df.transpose():
    if plot_df.loc[i]['SIZE'] < 0:
        n = plot_df.loc[i]['SIZE'] * -1
        randomlist_SIZE.append(n)
    else:
        n = plot_df.loc[i]['SIZE']
        randomlist_SIZE.append(n) 
plot_df['SIZE'] = randomlist_SIZE



#size_list = []
#for i in plot_df.transpose():
#    n = 
plot_df['A'] = plot_df['X'] - .5
plot_df['A'] = plot_df['A']**2
plot_df['B'] = plot_df['Y'] - .5
plot_df['B'] = plot_df['B']**2
plot_df['SIZE'] = plot_df['A'] + plot_df['B']
plot_df['SIZE'] = np.sqrt(plot_df['SIZE'])


plt.figure(figsize=(10, 8))
sns.scatterplot(plot_df, x = 'X', y = 'Y', hue = 'HUE', palette = 'Oranges', legend = False
               ,size = 'SIZE', sizes=(1, 1000)
               )
plt.savefig("picture_1.png", dpi = 600, bbox_inches = "tight")
plot_df.to_csv('Randomlists/plot_df_pic1.csv', index=False)