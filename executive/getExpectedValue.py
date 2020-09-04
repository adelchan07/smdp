"""
Created on Wed Sep 2 22:34:50 2020
@author: adelphachan

getExpectedValue.py
helper classes to obtain Q value in the main value iteration class
"""
import numpy as np 
from transition import getNextState

#universal "reward function" that can be modified for different option types
class getExpectedValue(object): 

	def __init__(self, optionType, probability):
		self.optionType = optionType
		self.probability = probability

	def __call__(self, state, option, V):

		expectedValueFunction = self.optionType[option]

		result = expectedValueFunction(state, option)

		sPrime = result[0]
		reward = result[1]

		futureReward = self.gamma * V[sPrime]

		result = self.probability * (reward + futureReward)
		return result

#helper classes to obtain Q value
class getPrimitiveExpectedValue(object):

	def __init__(self, gamma, optionPolicies, getNextState, getPrimitiveReward, stateSet):
		self.gamma = gamma
		self.optionPolicies = optionPolicies

		self.getNextState = getNextState
		self.getPrimitiveReward = getPrimitiveReward
		self.stateSet = stateSet

	def __call__(self, state, option):

		move = self.optionPolicies[option][state]
		sPrime = self.getNextState(state, move, self.stateSet)

		reward = self.getPrimitiveReward(state, self.optionPolicies[option])
		
		return [sPrime, reward]

class getLandmarkExpectedValue(object):

	def __init__(self, gamma, optionPolicies, optionTerminations, getLandmarkReward):
		self.gamma = gamma
		self.optionPolicies = optionPolicies
		self.optionTerminations = optionTerminations

		self.getLandmarkReward = getLandmarkReward

	def __call__(self, state, option):
		sPrime = self.optionTerminations[option]

		reward = self.getLandmarkReward(state, self.optionPolicies[option], sPrime)
		
		return[sPrime, reward]
