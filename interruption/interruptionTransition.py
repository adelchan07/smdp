"""
Created on Sun Oct 11 13:03:57 2020
@author: adelphachan
interruptedTransition.py

given a state, return the new "policy" including changes caused by interruption
"""
import numpy as np
from interruptedOptions import checkCondition
from interruptedOptions import compareOptions

#function for single step
class primitiveStep(object):
	def __init__(self, stateSet):
		self.stateSet = stateSet

	def __call__(self, state, action):
		x, y = state[0], state[1]
		xChange, yChange = action[0], action[1]

		newLocation = (x + xChange, y + yChange)
		if newLocation in self.stateSet:
			return newLocation
		else:
			return state

class getNextState(object):
	def __init__(self, landmarkTerminations, primitivePolicies, stateSet):
		self.landmarkTerminations = landmarkTerminations
		self.primitivePolicies = primitivePolicies
		self.stateSet = stateSet

	def __call__(self, state, option):

		if option in self.landmarkTerminations.keys():
			return self.landmarkTerminations[option]

		else:
			action = self.primitivePolicies[option]
			newState = (state[0] + action[0], state[1] + action[1])

			if newState in stateSet:
				return newState
			else:
				return state


#adds appropriate steps given a state and option (works for primitive and landmark options)
class getStatePath(object):
	def __init__(self, landmarkPolicies, primitiveOptions, landmarkTerminations, primitiveStep):
		self.landmarkPolicies = landmarkPolicies
		self.primitiveOptions = primitiveOptions
		self.landmarkTerminations = landmarkTerminations
		self.primitiveStep = primitiveStep
	
	def __call__(self, state, option, path):
		currentState = state
		
		if option in self.landmarkPolices.keys():
			terminationCondition = self.landmarkTerminations[option]

			while currentState != terminationCondition:
				action = self.landmarkPolicies[currentState][0]
				path[state] = action
				currentState = self.primitiveStep(state, action)
		else:
			action = primitiveOptions[currentState]
			path[state] = action

		return path

class getOption(object):
	def __init___(self, policy, optionType):
		self.policy = policy
		self.optionType = optionType

	def __call__(self, state):
		possibleOptions = self.policy[state]

		for option in possibleOptions:
			if self.optionType[state] = 'landmark': return option 

		return possibleOptions[0]


class normalPath(object):
	def __init__(self, policy, optionType, goalState, getStatePath, getNextState, getOption:
		self.policy = policy
		self.optionType = optionType
		self.goalState = goalState
		self.getStatePath = getStatePath
		self.getNextState = getNextState
		self.getOption = getOption

	def __call__(self, state):
		path = {}
		currentState = state

		while currentState != self.goalState:
			currentOption = self.getOption(currentState)
			path = self.getStatePath(state, currentOption, path)

			currentState = self.getNextState(state, option)

		return path

class interruptedPath(object):
	def __init__(self, policy, primitiveStep, optionPolicies, checkCondition, compareOptions, goalState):
		self.policy = policy
		self.primitiveStep = primitiveStep
		self.optionPolicies = optionPolicies
		self.getOption = getOption
		self.checkCondition = checkCondition
		self.compareOptions = compareOptions
		self.goalState = goalState

	def __call__(self, state):
		path = {}
		optionRecord = {}

		currentState = stateSet
		currentOption = self.getOption(state)

		while currentOption != self.goalState:
			action = self.optionPolicies[currentOption][currentState][0]
			path[currentState] = action
			optionRecord[currentState] = currentOption

			sPrime = self.primitiveStep(currentState, action)

			if self.checkCondition(currentState, sPrime):
				currentOption = self.compareOptions(currentState, currentOption)

			currentState = sPrime

		return path, currentOption




