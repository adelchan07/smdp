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
	
	def __call__(self, state, option):
		
		action = self.primitiveOptions[option]
		sPrime = self.getNextState(state, action, self.stateSet)
		return sPrime

class getLandmarkSPrime(object):
	def __init__(self, optionTerminations):
		self.optionTerminations = optionTerminations
	
	def __call__(self, state, option): #state not used but still keep as an input to maintain structure
		sPrime = self.optionTerminations[option]
		return sPrime

class transitionFunction(object):
	def __init__(self, optionSPrime):
		self.optionSPrime = optionSPrime
	
	def __call__(self, state, option, sPrime):
		probability = 0
		
		transitionFunction = self.optionSPrime[option]
		actualSPrime = transitionFunction(state, option)
		
		if sPrime == actualSPrime:
			probability = 1
		
		return probability
		
