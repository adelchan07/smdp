"""
Created on Wed Sep 2 14:54:03 2020

@author: adelphachan

transition.py

general function:
 - used once for each primitive option
 - used for x amount of steps required to get to termination condition for each landmark option 
"""

def getNextState(state, action, stateSet):

	xCoord = state[0] + action[0]
	yCoord = state[1] + action[1]

	result = (xCoord, yCoord)

	if result in stateSet:
		return result
	else:
		return state
