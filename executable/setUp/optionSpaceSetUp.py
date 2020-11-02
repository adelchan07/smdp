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
	def __init__(self, stateSet, landmarkStateSet, primitive):
		self.stateSet = stateSet
		self.landmarks = landmarkStateSet
		self.primitive = primitive

	def __call__(self):

		available = {state: self.getAvailableOptions(state) for state in self.stateSet}
		return available

	def getAvailableOptions(self, state):
		validOptions = []
		for option in self.landmarks.keys():
            
			if state in self.landmarks[option]:
				validOptions.append(option)
                
		validOptions = list(dict.fromkeys(validOptions))

		return self.primitive + validOptions
