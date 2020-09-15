"""
Created on Sun Sep 13 16:23:43 2020
@author: adelphachan

drawHeatMap.py

visualization of smdp implementation

for grid in Figure 2. (using G2)
V = {(1, 1): -15.518461348732007, (1, 2): -14.518461348732007, (1, 3): -13.518461348732007, (1, 4): -12.518461348732007, (1, 5): -11.518461348732007, (1, 7): -4.368453692472926, (1, 8): -3.368453692472926, (1, 9): -2.368453692472926, (1, 10): -3.368453692472926, (1, 11): -4.368453692472926, (2, 1): -14.518461348732007, (2, 2): -13.518461348732007, (2, 3): -12.518461348732007, (2, 4): -11.518461348732007, (2, 5): -10.518461348732007, (2, 7): -3.368453692472926, (2, 8): -2.368453692472926, (2, 9): -1.3684536924729258, (2, 10): -2.368453692472926, (2, 11): -3.368453692472926, (3, 1): -13.518461348732007, (3, 2): -12.518461348732007, (3, 3): -11.518461348732007, (3, 4): -10.518461348732007, (3, 5): -9.518461348732007, (3, 6): -6.131615213858806, (3, 7): -2.368453692472926, (3, 8): -1.3684536924729258, (3, 9): -0.3684536924729258, (3, 10): -1.3684536924729258, (3, 11): -2.368453692472926, (4, 1): -14.518453692472926, (4, 2): -13.518453692472926, (4, 3): -12.518453692472926, (4, 4): -11.518453692472926, (4, 5): -10.518453692472926, (4, 7): -1.3684536924729258, (4, 8): -0.3684536924729258, (4, 9): 0.6315463075270742, (4, 10): -0.3684536924729258, (4, 11): -1.3684536924729258, (5, 1): -15.518453692472926, (5, 2): -14.518453692472926, (5, 3): -13.518453692472926, (5, 4): -12.518453692472926, (5, 5): -11.518453692472926, (5, 7): -0.3684536924729258, (5, 8): 0.6315463075270742, (5, 9): 1.6315463075270742, (5, 10): 0.6315463075270742, (5, 11): -0.3684536924729258, (6, 2): -14.321615213858806, (6, 7): 0.6315463075270742, (6, 8): 1.6315463075270742, (6, 9): 2.631546307527074, (6, 10): 1.6315463075270742, (6, 11): 0.6315463075270742, (7, 1): -12.468453692472925, (7, 2): -11.468453692472925, (7, 3): -10.468453692472925, (7, 4): -9.468453692472925, (7, 5): -8.468453692472925, (7, 9): 7.368391676774367, (8, 1): -11.468453692472925, (8, 2): -10.468453692472925, (8, 3): -9.468453692472925, (8, 4): -8.468453692472925, (8, 5): -7.4684536924729255, (8, 7): 2.631546307527074, (8, 8): 7.368391676774367, (8, 9): 12.631552509096931, (8, 10): 7.368397258187239, (8, 11): 2.6315575323685145, (9, 1): -10.468453692472925, (9, 2): -9.468453692472925, (9, 3): -8.468453692472925, (9, 4): -7.4684536924729255, (9, 5): -6.4684536924729255, (9, 7): 7.368391676774367, (9, 8): 12.631552509096931, (9, 9): 7.368397258187239, (9, 10): 12.631557532368515, (9, 11): 7.368401779131663, (10, 1): -9.468453692472925, (10, 2): -8.468453692472925, (10, 3): -7.4684536924729255, (10, 4): -6.4684536924729255, (10, 5): -5.4684536924729255, (10, 6): -1.6316083232256333, (10, 7): 2.631552509096931, (10, 8): 7.368397258187239, (10, 9): 12.631557532368515, (10, 10): 7.368401779131663, (10, 11): 2.631561601218497, (11, 1): -10.46844749090307, (11, 2): -9.46844749090307, (11, 3): -8.46844749090307, (11, 4): -7.4684474909030705, (11, 5): -6.4684474909030705, (11, 7): -1.6316027418127619, (11, 8): 2.6315575323685145, (11, 9): 7.368401779131663, (11, 10): 2.631561601218497, (11, 11): -1.6315945589033527}
policy = {(1, 1): {'h3': 1.0}, (1, 2): {'h3': 1.0}, (1, 3): {'h3': 1.0}, (1, 4): {'h3': 1.0}, (1, 5): {'h3': 1.0}, (1, 7): {'h4': 1.0}, (1, 8): {'h4': 1.0}, (1, 9): {'h4': 1.0}, (1, 10): {'h4': 1.0}, (1, 11): {'h4': 1.0}, (2, 1): {'h3': 1.0}, (2, 2): {'h3': 1.0}, (2, 3): {'h3': 1.0}, (2, 4): {'h3': 1.0}, (2, 5): {'h3': 1.0}, (2, 7): {'h4': 1.0}, (2, 8): {'h4': 1.0}, (2, 9): {'h4': 1.0}, (2, 10): {'h4': 1.0}, (2, 11): {'h4': 1.0}, (3, 1): {'h3': 1.0}, (3, 2): {'h3': 1.0}, (3, 3): {'h3': 1.0}, (3, 4): {'h3': 1.0}, (3, 5): {'up': 0.5, 'h3': 0.5}, (3, 6): {'up': 1.0}, (3, 7): {'h4': 1.0}, (3, 8): {'h4': 1.0}, (3, 9): {'h4': 1.0}, (3, 10): {'h4': 1.0}, (3, 11): {'h4': 1.0}, (4, 1): {'h3': 1.0}, (4, 2): {'h3': 1.0}, (4, 3): {'h3': 1.0}, (4, 4): {'h3': 1.0}, (4, 5): {'h3': 1.0}, (4, 7): {'h4': 1.0}, (4, 8): {'h4': 1.0}, (4, 9): {'h4': 1.0}, (4, 10): {'h4': 1.0}, (4, 11): {'h4': 1.0}, (5, 1): {'h3': 1.0}, (5, 2): {'h3': 1.0}, (5, 3): {'h3': 1.0}, (5, 4): {'h3': 1.0}, (5, 5): {'h3': 1.0}, (5, 7): {'h4': 1.0}, (5, 8): {'h4': 1.0}, (5, 9): {'h4': 1.0}, (5, 10): {'h4': 1.0}, (5, 11): {'h4': 1.0}, (6, 2): {'right': 1.0}, (6, 7): {'h4': 1.0}, (6, 8): {'h4': 1.0}, (6, 9): {'right': 0.5, 'h4': 0.5}, (6, 10): {'h4': 1.0}, (6, 11): {'h4': 1.0}, (7, 1): {'h2': 1.0}, (7, 2): {'h2': 1.0}, (7, 3): {'h2': 1.0}, (7, 4): {'h2': 1.0}, (7, 5): {'h2': 1.0}, (7, 9): {'right': 1.0}, (8, 1): {'h2': 1.0}, (8, 2): {'h2': 1.0}, (8, 3): {'h2': 1.0}, (8, 4): {'h2': 1.0}, (8, 5): {'h2': 1.0}, (8, 7): {'up': 0.5, 'right': 0.5}, (8, 8): {'up': 0.5, 'right': 0.5}, (8, 9): {'right': 1.0}, (8, 10): {'down': 0.5, 'right': 0.5}, (8, 11): {'down': 0.5, 'right': 0.5}, (9, 1): {'h2': 1.0}, (9, 2): {'h2': 1.0}, (9, 3): {'h2': 1.0}, (9, 4): {'h2': 1.0}, (9, 5): {'h2': 1.0}, (9, 7): {'up': 1.0}, (9, 8): {'up': 1.0}, (9, 9): {'up': 0.25, 'down': 0.25, 'left': 0.25, 'right': 0.25}, (9, 10): {'down': 1.0}, (9, 11): {'down': 1.0}, (10, 1): {'h2': 1.0}, (10, 2): {'h2': 1.0}, (10, 3): {'h2': 1.0}, (10, 4): {'h2': 1.0}, (10, 5): {'up': 0.5, 'h2': 0.5}, (10, 6): {'up': 1.0}, (10, 7): {'up': 0.5, 'left': 0.5}, (10, 8): {'up': 0.5, 'left': 0.5}, (10, 9): {'left': 1.0}, (10, 10): {'down': 0.5, 'left': 0.5}, (10, 11): {'down': 0.5, 'left': 0.5}, (11, 1): {'h2': 1.0}, (11, 2): {'h2': 1.0}, (11, 3): {'h2': 1.0}, (11, 4): {'h2': 1.0}, (11, 5): {'h2': 1.0}, (11, 7): {'up': 0.5, 'left': 0.5}, (11, 8): {'up': 0.5, 'left': 0.5}, (11, 9): {'left': 1.0}, (11, 10): {'down': 0.5, 'left': 0.5}, (11, 11): {'down': 0.5, 'left': 0.5}}

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

	heatMap = sb.heatmap(data, cmap='RdYlGn', linewidths=0.1, vmin=vmin, vmax=vmax)
	
	#draw arrows
    	primitive = {'up':(0,1), 'down':(0,-1), 'left':(-1,0), 'right':(1,0)}
   	for state in V.keys():
        	options = policy[state].keys()
        	x,y = state
        	for option in options:
            	if option in primitive.keys():
                	action = primitive[option]
                	plt.arrow(y+.5, x+.5, action[1]/7, action[0]/7, fc="k", ec="k", head_width=0.1, head_length=0.1)       
	
	return heatMap


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

