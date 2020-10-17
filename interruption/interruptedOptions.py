"""
Created on Fri Oct 2 12:04:49 2020
@author: adelphachan

interruptedOptions.py

early termination of options + choosing which option to pick up
**addition of a landmark option that takes you directly to the ultimate goal state

two functions used to initiate the need for options to be interrupted

purpose of funcitions:
1. checkCondition: 
	a. True = needs to check for a possible new option
	b. False = no need to check, can stay with the current option you are following
"""

class checkCondition(object):
	def __init__(self, optionSpace):
		self.optionSpace = optionSpace

	def __call__(self, state, sPrime):
		return !(self.optionSpace[state] == self.optionSpace[sPrime]) 

class compareOptions(object):
	def __init__(self, policy, landmarkOptions):
		self.policy = policy
		self.landmarkOptions = landmarkOptions

	def __call__(self, state, currentOption):
		options = list(self.policy[state].keys())

		if currentOption in options: #preferable to stick to where you currently are
			return option

		else:
			for option in options:
				if option in self.landmarkOptions:
					return option

			


