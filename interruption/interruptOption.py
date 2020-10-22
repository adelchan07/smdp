"""
Created on Fri Oct 2 12:04:49 2020
@author: adelphachan
interruptOption.py

1. CheckCondition: return True if new options available, return False if not
2. CompareOptions: return new option choice 
optionSpaceFunction and getValidOption functions return landmark options relevant at that specific state (only returning landmark options because those are the only ones relevant in interruption)
"""

class optionSpaceFuction(object):
	def__init__(self, optionSpace, optionType):
		self.optionSpace = optionSpace
		self.optionType = optionType

	def __call__(self, state):
		choices = self.optionSpace[state]
		availableLandmarks = []

		for choice in choices:
			if optionType[choice] == 'landmark': availableLandmarks.append(choice)

		return availableLandmarks


class CheckCondition(object):
	def __init__(self, optionSpaceFunction):
		self.optionSpaceFunction = optionSpaceFunction

	def __call__(self, state, sPrime):
		return self.optionSpaceFunction(state) != self.optionSpaceFunction(sPrime)

class getValidOptions(object):
	def __init__(self, optionSpace, optionType):
		self.optionSpace = optionSpace
		self.optionType = optionType

	def __call__(self, state):
		choices = self.optionSpace[state]
		validOptions = []

		for choice in choices:
			if self.optionType[choice] == 'landmark': validOptions.append(choice)

		return validOptions

class CompareOptions(object):
	def __init__(self, getValidOptions):
		self.getValidOptions = getValidOptions

	def __call__(self, state, currentOption):
		available = self.getValidOptions(state)

		if currentOption in available: return currentOption #favor current option

		return available[0] #else case
