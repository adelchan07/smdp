"""
Created on Wed Sep 2 22:34:50 2020

@author: adelphachan

optionValueIteration.py

optionsDictionary = optionPolicies = {"option name": {policy}}
option = "option name"
optionTerminations = {"landmark option name": (landmark location)}
optionType = {"option name": "option type"}
availableOptionsAtState = {(state): [list of names of options whos initiation set includes this state]}

return from callable = [V, policy]

outsourced functions from executive folder:
1. transition function = getNextState in transition.py 
2. reward function = primitive and landmark reward in reward.py
	--> all calculations of reward and Q value condensed into getExpectedValue class in this file

"""
import sys
sys.path.append('./executive/')

import numpy as np 
import reward 
import transition 

#general functions
def getMaxValue(dictionary):
	keysList = list(dictionary.keys())
	valuesList = list(dictionary.values())
	maxVal = keysList[np.argmax(valuesList)]
	return maxVal

#helper classes to obtain Q value
class getPrimitiveExpectedValue(object):

	def __init__(self, gamma, optionPolicies, getNextState, getPrimitiveReward, stateSet):
		self.gamma = gamma
		self.optionPolicies = optionPolicies

		self.getNextState = getNextState
		self.getPrimitiveReward = getPrimitiveReward
		self.stateSet = stateSet

	def __call__(self, state, option, V):

		move = self.optionPolicies[option][state]
		sPrime = self.getNextState(state, move, self.stateSet)
		probability = 1

		reward = self.getPrimitiveReward(state, self.optionPolicies[option])
		futureReward = self.gamma * V[sPrime]

		result = probability * (reward + futureReward)
		return result

class getLandmarkExpectedValue(object):

	def __init__(self, gamma, optionPolicies, optionTerminations, getLandmarkReward):
		self.gamma = gamma
		self.optionPolicies = optionPolicies
		self.optionTerminations = optionTerminations

		self.getLandmarkReward = getLandmarkReward

	def __call__(self, state, option, V):
		sPrime = self.optionTerminations[option]
		probability = 1

		reward = self.getLandmarkReward(state, self.optionPolicies[option], sPrime)
		futureReward = self.gamma * V[sPrime]

		result = probability * (reward + futureReward)
		return result

class getExpectedValue(object): #universal "reward function" that can be modified for different option types

	def __init__(self, optionType, getPrimitiveExpectedValue, getLandmarkExpectedValue):
		self.optionType = optionType
		self.getPrimitiveExpectedValue = getPrimitiveExpectedValue
		self.getLandmarkExpectedValue = getLandmarkExpectedValue

	def __call__(self, state, option, V):

		type = self.optionType[option]

		if type == "primitive":
			value = self.getPrimitiveExpectedValue(state, option, V)

		if type == "landmark":
			value = self.getLandmarkExpectedValue(state, option, V)

		return value

#main value iteration class
class optionValueIteration(object):

	def __init__(self, stateSet, optionsDictionary, availableOptionsAtState, V, convergenceTolerance, gamma, getMaxValue, getNextState, getExpectedValue):
		self.stateSet = stateSet

		self.optionPolicies = optionsDictionary
		self.availableOptions = availableOptionsAtState

		self.V = V
		self.convergenceTolerance = convergenceTolerance
		self.gamma = gamma

		#callables for reward values
		self.computeExpectedValue = getExpectedValue
		self.getMaxValue = getMaxValue
		self.getNextState = getNextState


	def __call__(self): 

		valueIterationResult = self.runValueIteration()
		return valueIterationResult

	def runValueIteration(self):

		self.updateV()
		policy = {state: self.getPolicy(state) for state in self.stateSet}

		return [self.V, policy]

	#value iteration helper functions
	def updateV(self):
		delta = self.convergenceTolerance * 100

		while delta > self.convergenceTolerance:
			delta = 0

			for state in self.stateSet:

				expectedValues = self.getExpectedValues(state)
				bestOption = self.getMaxValue(expectedValues)
				diffVal = abs(expectedValues[bestOption] - self.V[state])
				self.V[state] = expectedValues[bestOption]

				delta = max(delta, diffVal)

	def getExpectedValues(self, state): 

		expectedValues = {option: self.computeExpectedValue(state, option, self.V) for option in self.availableOptions[state]}

		return expectedValues

	def getPolicy(self, state):
		expectedValues = self.getExpectedValues(state)
		bestOption = self.getMaxValue(expectedValues)

		return bestOption
