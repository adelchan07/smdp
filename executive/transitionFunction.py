"""
Created on Wed Sep 2 14:54:03 2020

@author: adelphachan

transition.py

general function:
 - used once for each primitive option
 - used for x amount of steps required to get to termination condition for each landmark option 

optionSPrime = dictionary of format {"option name": corresponding option type's transition function"
"""

def getNextState(state, action, stateSet):

	xCoord = state[0] + action[0]
	yCoord = state[1] + action[1]

	result = (xCoord, yCoord)

	if result in stateSet:
		return result
	else:
		return state

class getPrimitiveSPrime(object):
	def __init__(self, primitiveOptions, stateSet, getNextState):
		self.primitiveOptions = primitiveOptions
		self.stateSet = stateSet
		self.getNextState = getNextState
	
	def __call__(self, state, option, sPrime):
		
		action = self.primitiveOptions[option]
		actual = self.getNextState(state, action, self.stateSet)
		
		if actual != sPrime:
			return 0
		return 1
		

class getLandmarkSPrime(object):
	def __init__(self, optionTerminations):
		self.optionTerminations = optionTerminations
	
	def __call__(self, state, option, sPrime): 
		actual = self.optionTerminations[option]
		
		if actual != sPrime:
			return 0
		return 1

class transitionFunction(object):
	def __init__(self, optionSPrime):
		self.optionSPrime = optionSPrime
	
	def __call__(self, state, option, sPrime):
		
		probability = 0
		
		function = self.optionSPrime[option]
		return function(state, option, sPrime)
		
		
