"""
Created on Sun Sep 13 16:23:43 2020
@author: adelphachan

drawHeatMap.py

visualization of smdp implementation
"""

import numpy as np
import seaborn as sb 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import colors
import matplotlib

def drawHeatMap(width, height, V, vmin, vmax):
    data = np.ones((width, height)) * np.nan
    # fill in some fake data
    for state in V.keys():
        data[state] = V[state]
    # make a figure + axes
    fig, ax = plt.subplots(1, 1, tight_layout=True)
    # make color map
    my_cmap = sb.heatmap(data, cmap='RdYlGn', linewidths=0.1, vmin=vmin, vmax=vmax)
    for x in range(N + 1):
        ax.axhline(x, lw=0.3, color='k', zorder=5)
        ax.axvline(x, lw=0.3, color='k', zorder=5) 

"""
def drawFinalMap(V, policy, width, height):
	vmin = min(list(V.values()))
    vmax = max(list(V.values()))

    fig, ax = plt.subplots(figsize=(12,7))
    title = "semi-MDP Heat Map"
    plt.title(title, fontsize = 15)
    ttl = ac.title
  	ttl.set_position([0.5, 1.05])
  	drawHeatMap(width, height, V, vmin, vmax)
  	plt.savefig(f'semi-mdpHeatMap.jpg')
"""
