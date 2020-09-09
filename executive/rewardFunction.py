"""
Created on Mon Aug 17 13:54:03 2020

@author: adelphachan

reward.py

optionReward = dictionary of format {"option name": corresponding option type's reward function"
"""

import numpy as numpy
import transitionFunction as tf

class getPrimitiveOptionReward(object):
	def __init__(self, actionCost, moveCost, goalStates, goalReward, primitivePolicies, getPrimitiveSPrime):
		self.actionCost = actionCost
		self.moveCost = moveCost
		self.goalStates = goalStates
		self.goalReward = goalReward
		self.optionPolicies = primitivePolicies
		self.getPrimitiveSPrime = getPrimitiveSPrime
	
	def __call__(self, state, option):
		
		reward = self.actionCost + self.moveCost
		
		sPrime = self.getPrimitiveSPrime(state, option)
		
		if sPrime in self.goalStates:
			reward += self.goalReward
			
		return reward

class getLandmarkOptionReward(object):
	def __init__(self, actionCost, moveCost, goalStates, goalReward, landmarkPolicies, getLandmarkSPrime, getNextState):
		self.actionCost = actionCost
		self.moveCost = moveCost
		self.goalStates = goalStates
		self.goalReward = goalReward
		
		self.optionPolicies = landmarkPolicies
		
		self.getLandmarkSPrime = getLandmarkSPrime
		
		self.getNextState = getNextState
	
	def __call__(self, state, option):
		#the restricted initiation set of an option is reflected in the stateSet represented in the optionPolicy
		
		reward = self.moveCost + self.getCumulativeCost(state, option)

		if terminationCondition in self.goalStates:
			reward += self.goalReward

		return reward

	def getCumulativeCost(self, state, option):

		stepsTaken = 0
		currentState = state
		
		terminationCondition = self.getLandmarkSPrime(state, option)

		while currentState != terminationCondition:
			stepsTaken += 1
			action = optionPolicy[currentState]
			nextState = self.getNextState(currentState, action, self.stateSet)
			currentState = nextState

		cumulativeCost = stepsTaken*self.actionCost
		return cumulativeCost
	
class rewardFunction(object):
	def __init__(self, optionReward):
		self.optionReward = optionReward
	
	def __call__(self, state, option, sPrime):
		rewardFunction = self.optionReward[option]
		reward = rewardFunction(state, option)
		
		return reward
