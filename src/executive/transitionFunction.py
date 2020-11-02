"""
Created on Wed Sep 2 14:54:03 2020

@author: adelphachan

transition.py

GetPrimitiveSPrime and GetLandmarkSPrime are deterministic transition functions

TransitionFunction = universal transition function with dictionary input optionSPrime

optionSPrime = dictionary of format {"option name": corresponding option type's transition function"}
primitiveOptions = {"name": action}, ie. {"up": (0,1), "down":(0,-1)...}
optionTerminations = {"name": (landmark location)} ie. {"h1": (3,2)}
"""

def getNextState(state, action, stateSet):

	xCoord = state[0] + action[0]
	yCoord = state[1] + action[1]

	result = (xCoord, yCoord)

	if result in stateSet:
		return result
	else:
		return state

class GetPrimitiveSPrime(object):
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
		

class GetLandmarkSPrime(object):
	def __init__(self, optionTerminations):
		self.optionTerminations = optionTerminations
	
	def __call__(self, state, option, sPrime): 
		actual = self.optionTerminations[option]
		
		if actual != sPrime:
			return 0
		return 1

class TransitionFunction(object):
	def __init__(self, optionSPrime):
		self.optionSPrime = optionSPrime
	
	def __call__(self, state, option, sPrime):
		
		function = self.optionSPrime[option]
		return function(state, option, sPrime)
		
		
