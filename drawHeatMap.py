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

def drawHeatMap(width, height, V, goalState):
	vmin = min(list(V.values()))
	vmax = max(list(V.values()))

	V.pop(goalState)
	data = np.ones((width, height)) * np.nan

	for state in V.keys():
		data[state] = V[state]

	return sb.heatmap(data, cmap='RdYlGn', linewidths=0.1, vmin=vmin, vmax=vmax)


def drawFinalMap(V, width, height, goalState):
    
    fig, ax=plt.subplots(figsize=(12,7))
    title=f"semi MDP"
    plt.title(title, fontsize=18)
    ttl=ax.title
    ttl.set_position([0.5, 1.05])
    
    for x in range(width + 1):
        ax.axhline(x, lw=0.3, color='k', zorder=5)
        ax.axvline(x, lw=0.3, color='k', zorder=5) 
    
    drawHeatMap(width, height, V, goalState)

def drawArrows(V, mainPolicy, optionPolicies):
	"""
		a. primitive option: plt arrow with the single action
		b. landmark option: follow landmark policy and plot all arrows until landmark is reached
			--> give each landmark a distinct color and plot arrow with that color

		**need additional function brnaching between drawing a single arrow and drawing landmark arrows (which builds off drawing the single arrow)
	
	optionPolicies = {"up": (0,1)... "h1": {policy}}
	optionColors = {"all primitive options": 'k','h1': 'r', 'h2': 'g'...}

	"""

