"""
Created on Tues Oct 20 20:13:34 2020
@author: adelphachan
interruptedPath.py

given a state, return the new "policy" including changes caused by interruption
"""
import numpy as np 
from interruptOption import CheckCondition
from interruptOption import CompareOptions

class getOption(object):
	def __init__(self, optionType, policy):
		self.optionType = optionType
		self.policy = policy

	def __call__(self, state):
		options = self.policy[state]

		for option in options:
			if self.optionType[option] == 'landmark':
				return option

class singleStep(object):
	def __init__(self, optionPolicies, getNextState, stateSet):
		self.optionPolicies = optionPolicies
		self.getNextState #getNextState from regular transition function
		self.stateSet = stateSet

	def __call__(self, state, option):
		action = list(self.optionPolicies[option][state].keys())[0]
		return self.getNextState(state, action, self.stateSet)


class GetInterruptedPath(object):
	def __init__(self, optionPolicies, goalState, getOption, singleStep, CheckCondition, CompareOptions):
		
		self.optionPolicies = optionPolicies
		self.goalState = goalState

		self.getOption = getOption
		self.singleStep = singleStep

		self.checkCondition = CheckCondition
		self.compareOptions = CompareOptions

	def __call__(self, state):
		path = {}
		currentState = state
		currentOption = self.getOption(state)

		while currentState != self.goalState:
			specificStep = list(self.optionPolicies[currentOption][state].keys())[0]
			path[currentState] = specificStep

			sPrime = self.singleStep(currentState, currentOption)

			if self.checkCondition(currentState, sPrime):
				currentOption = self.compareOptions(sPrime, currentOption)
			currentState = sPrime

		return path

class GetOptionHistory(object):
	def __init__(self, optionPolicies, goalState, getOption, singleStep, CheckCondition, CompareOptions):
		
		self.optionPolicies = optionPolicies
		self.goalState = goalState

		self.getOption = getOption
		self.singleStep = singleStep

		self.checkCondition = CheckCondition
		self.compareOptions = CompareOptions

	def __call__(self, state):
		optionHistory = {}
		currentState = state
		currentOption = self.getOption(state)

		while currentState != self.goalState:
			path[currentOption] = currentOption

			sPrime = self.singleStep(currentState, currentOption)

			if self.checkCondition(currentState, sPrime):
				currentOption = self.compareOptions(sPrime, currentOption)
			currentState = sPrime

		return optionHistory
