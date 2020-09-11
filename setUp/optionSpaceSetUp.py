"""
Created on Wed Sep 3 13:25:45 2020

@author: adelphachan

optionSpaceSetUp.py

set up dictionary of corresponding options available at each state

primitiveOptions = list of primitive options (as they apply to the entire state space)
	ie. ['up', 'down', ...]
landmarkPolicies = {landmark: (policy)}
"""

import numpy as np 

class OptionSpaceSetUp(object):
	def __init__(self, stateSet, landmarkPolicies, primitiveOptions):
		self.stateSet = stateSet
		self.primitiveOptions = primitiveOptions
		self.landmarkPolicies = landmarkPolicies

	def __call__(self):

		available = {state: self.getAvailableOptions(state) for state in self.stateSet}
		return available

	def getAvailableOptions(self, state):

		validOptions = self.primitiveOptions

		for option in self.optionsDictionary.keys():

			relevantStates = list(self.landmarkPolicies[option].keys()) 

			if state in relevantStates:
				validOptions.append(option)

		return validOptions
