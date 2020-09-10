"""
Created on Mon Aug 17 13:54:03 2020

@author: adelphachan

reward.py

optionReward = dictionary of format {"option name": corresponding option type's reward function"
"""

import numpy as numpy
import transitionFunction as tf

class GetPrimitiveOptionReward(object):
	def __init__(self, actionCost, moveCost, goalStates, goalReward, primitivePolicies, getPrimitiveSPrime):
		self.actionCost = actionCost
		self.moveCost = moveCost
		self.goalStates = goalStates
		self.goalReward = goalReward
		self.optionPolicies = primitivePolicies
		self.getPrimitiveSPrime = getPrimitiveSPrime
	
	def __call__(self, state, option, sPrime):
		
		reward = self.actionCost + self.moveCost
		
		if sPrime in self.goalStates:
			reward += self.goalReward
			
		return reward

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
		
		reward = self.moveCost + self.getCumulativeCost(state, option)
		terminationCondition = sPrime

		if terminationCondition in self.goalStates:
			reward += self.goalReward

		return reward

	def getCumulativeCost(self, state, option):

		stepsTaken = 0
		currentState = state
		
		terminationCondition = self.getLandmarkSPrime(state, option)
		optionPolicy = self.optionPolicies[option]
		stateSet = list(optionPolicy.keys())

		while currentState != terminationCondition:
			stepsTaken += 1
			action = optionPolicy[currentState]
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
