"""
Created on Mon Aug 17 13:54:03 2020

@author: adelphachan

reward.py

optionReward = dictionary of format {"option name": corresponding option type's reward function"
"""

import numpy as numpy
import transitionFunction as tf

class GetPrimitiveOptionReward(object):
	def __init__(self, actionCost, moveCost, goalStates, goalReward, getPrimitiveSPrime):
		self.actionCost = actionCost
		self.moveCost = moveCost
		self.goalStates = goalStates
		self.goalReward = goalReward
		self.getPrimitiveSPrime = getPrimitiveSPrime
	
	def __call__(self, state, option, sPrime):
		
		reward = self.actionCost + self.moveCost
		
		if sPrime in self.goalStates:
			reward += self.goalReward
			
		return reward*self.getPrimitiveSPrime(state, option, sPrime)

class GetLandmarkOptionReward(object):
	def __init__(self, actionCost, moveCost, goalStates, goalReward, landmarkPolicies, getLandmarkSPrime, getNextState):
		self.actionCost = actionCost
		self.moveCost = moveCost
		self.goalStates = goalStates
		self.goalReward = goalReward
		
		self.optionPolicies = landmarkPolicies
		
		self.getLandmarkSPrime = getLandmarkSPrime
		
		self.getNextState = getNextState
	
	def __call__(self, state, option, sPrime):
		#the restricted initiation set of an option is reflected in the stateSet represented in the optionPolicy
		
		reward = self.moveCost + self.getCumulativeCost(state, option, sPrime)
		
		if sPrime in self.goalStates:
			reward += self.goalReward

		return reward*self.getLandmarkSPrime(state, option, sPrime)

	def getCumulativeCost(self, state, option, sPrime):

		stepsTaken = 0
		currentState = state
		
		optionPolicy = self.optionPolicies[option]
		stateSet = list(optionPolicy.keys())

		while currentState != sPrime:
			stepsTaken += 1
			availableActions = list(optionPolicy[currentState].keys())
			action = availableActions[0] 
			nextState = self.getNextState(currentState, action, stateSet)
			currentState = nextState

		cumulativeCost = stepsTaken*self.actionCost
		return cumulativeCost
	
class RewardFunction(object):
	def __init__(self, optionReward):
		self.optionReward = optionReward
	
	def __call__(self, state, option, sPrime):
		rewardFunction = self.optionReward[option]
		reward = rewardFunction(state, option, sPrime)
		
		return reward
