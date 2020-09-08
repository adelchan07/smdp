"""
Created on Wed Sep 3 13:25:45 2020

@author: adelphachan

optionSpaceSetUp.py

set up dictionary of corresponding options available at each state
"""

import numpy as np 

class optionSpaceSetUp(object):
	def __init__(self, stateSet, optionsDictionary):
		self.stateSet = stateSet
		self.optionsDictionary = optionsDictionary

	def __call__(self):

		available = {state: self.getAvailableOptions(state) for state in self.stateSet}
		return available

	def getAvailableOptions(self, state):

		validOptions = []

		for option in self.optionsDictionary.keys():

			#relevant states = option's policy.keys()
			relevantStates = list(self.optionsDictionary[option].keys()) 

			if state in relevantStates:
				validOptions.append(option)

		return validOptions
