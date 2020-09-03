"""
Created on Mon Aug 17 13:54:03 2020

@author: adelphachan

reward.py
"""

import numpy as numpy
from transition import getNextState

class getPrimitiveOptionReward(object):
	def __init__(self, stateSet, actionCost, moveCost, goalStates, goalReward, getNextState):
		self.stateSet = stateSet #stateset for all primitive actions = full stateSet

		self.actionCost = actionCost
		self.moveCost = moveCost
		self.goalStates = goalStates
		self.goalReward = goalReward

		self.getNextState = getNextState


	def __call__(self, state, optionPolicy):

		reward = self.actionCost + self.moveCost

		action = optionPolicy[state]
		nextState = self.getNextState(state, action, self.stateSet)

		if nextState in self.goalStates:
			reward += self.goalReward

		return reward
	
class getLandmarkOptionReward(object):
	def __init__(self, stateSet, actionCost,moveCost, goalStates, goalReward, getNextState):
		self.stateSet = stateSet

		self.actionCost = actionCost
		self.moveCost = moveCost
		self.goalStates = goalStates
		self.goalReward = goalReward

		self.getNextState = getNextState

	def __call__(self, state, optionPolicy, terminationCondition):

		reward = self.moveCost + self.getCumulativeCost(state, optionPolicy, terminationCondition)

		if terminationCondition in self.goalStates:
			reward += self.goalReward

		return reward

	def getCumulativeCost(self, state, optionPolicy, terminationCondition):

		stepsTaken = 0
		currentState = state

		while currentState != terminationCondition:
			stepsTaken += 1
			action = optionPolicy[currentState]
			nextState = self.getNextState(currentState, action, self.stateSet)
			currentState = nextState

		cumulativeCost = stepsTaken*self.actionCost
		return cumulativeCost
