"""
Created on Wed Sep 3 13:25:45 2020

@author: adelphachan

availableOptionsSetUp.py

set up of the availableOptionsAtState dictionary used in optionValueIteration.py
"""

import numpy as np 

class availbleOptionsSetUp(object):
	def __init__(self, stateSet, optionsDictionary):
		self.stateSet = stateSet
		self.optionsDictionary = optionsDictionary

	def __call__(self):

		available = {state: self.getAvailableOptions(state) for state in self.stateSet}

	def getAvailableOptions(self, state):

		validOptions = []

		for option in self.optionsDictionary.keys():

			#relevant states = option's policy.keys()
			relevantStates = list(self.optionsDictionary[option].keys()) 

			if state in relevantStates:
				validOptions.append(option)

		return validOptions