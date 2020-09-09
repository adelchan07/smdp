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
		
		action = self.optionPolicies[option]
		sPrime = self.getPrimitiveSPrime(state, action)
		
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
		
		sPrime = self.getLandmarkSPrime(state, option)
		reward = self.moveCost + (self.actionCost * self.stepsTaken(state, option, sPrime))
		
		if sPrime in self.goalStates:
			reward += self.goalReward
		
		return reward
	
	def stepsTaken(self, state, option, sPrime):
		
		policy = self.optionPolicies[option]
		stateSet = list(policy.keys())
		
		stepsTaken = 0
		current = state
		
		while current != sPrime:
			stepsTaken += 1
			action = policy[current]
			nextState = self.getNextState(state, action, stateSet)
			currentState = nextState

		return stepsTaken
	
class rewardFunction(object):
	def __init__(self, optionReward):
		self.optionReward = optionReward
	
	def __call__(self, state, option, sPrime):
		rewardFunction = self.optionReward[option]
		reward = rewardFunction(state, option)
		
		return reward
