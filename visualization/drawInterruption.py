"""
Created on Wed Oct 21 10:43:39 2020
@author: adelphachan
drawInterruption.py

visualization of normal path vs interrupted path
"""
import numpy as np
import seaborn as sb 
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import colors
import matplotlib

def drawPaths(fig, ax, width, height, agentLocation, normalPath, interruptedPath, goalState, goalStateDomain):
    data = np.ones((width, height)) * np.nan
    
    for state in goalStateDomain: 
        data[state] = 1
        
    baseGrid = sb.heatmap(data, linewidths=0.1,vmin = 0, vmax = 1, cbar = False)
    
    for state in normalPath.keys():
        x,y = state
        action = normalPath[state]
        plt.arrow(y+.4, x+.2, action[1]/7, action[0]/7, fc="b", ec="b", head_width=0.1, head_length=0.1) 
    
        action = normalPath[state]
        plt.arrow(y+.4, x+.7, action[1]/7, action[0]/7, fc="m", ec="m", head_width=0.1, head_length=0.1) 
    
    goalX, goalY = goalState[0], goalState[1]
    ax.text(y+.5,x + .5, "R", color = 'k', fontsize = 17 )
    
    x,y = agentLocation[0], agentLocation[1]
    ax.text(y+.4,x + .5, "Agent", color = 'k', fontsize = 17 )
    
    return baseGrid

def drawFinalMap(width, height, state, normalPath, interruptedPath, goalState, goalStateDomain):
    
    fig, ax=plt.subplots(figsize=(12,7))
    title=f"interruption at state {state}"
    plt.title(title, fontsize=18)
    ttl=ax.title
    ttl.set_position([0.5, 1.05])
    
    for x in range(width + 1):
        ax.axhline(x, lw=0.3, color='k', zorder=5)
        ax.axvline(x, lw=0.3, color='k', zorder=5) 
    
    normal = mpatches.Patch(color = 'b', label = 'Normal Path')
    interrupt = mpatches.Patch(color = 'm', label = 'Interrupted Path')
    
    plt.legend(handles = [normal, interrupt], bbox_to_anchor=(1.2, 1), loc = 'upper right')
        
    drawPaths(fig, ax, width, height, state, normalPath, interruptedPath, goalState, goalStateDomain)
