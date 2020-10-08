"""
Created on Mon Oct 5 10:23:50 2020
@author: adelphachan

interruptionTransition.py

alter transition function to explore new options whenever new options are available
pulling from the two functions found in interruptedOptions.py

primitive options and single step getNextState remain the same --> only change is in if landmark options go to completion
"""
import numpy as np
from interruptedOptions import checkCondition
from interruptedOptions import compareOptions

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
		
		
