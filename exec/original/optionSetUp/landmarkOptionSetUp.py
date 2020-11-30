"""
Created on Sun Aug 9 12:04:03 2020
@author: adelphachan
landmarkOptionSetUp.py
return = dictionary of landmark options
--> append values onto a dictionary that already exists
	(allows us to be able to add any type of option necessary to the same general option dictionary)
constants for all dictionaries:
- transition table / stateSet (already updated with blockList)
- actionCost 
- goalReward
- getLandmarkReward callable
- getLandmarkPolicy callable
landmarks = {"name": location}
"""
import numpy as np
import sys
sys.path.append('../src/') #path appended according to testLandmarkOptionSetUp.py file
import valueIteration as vi

#general helper functions 
def merge(dictionary1, dictionary2):
	
	result = {**dictionary1, **dictionary2}
	return result

#valueIteration helper classes
class GetLandmarkPolicy(object):
	def __init__(self, gamma, convergenceTolerance):
		self.gamma = gamma
		self.convergenceTolerance = convergenceTolerance
	
	def __call__(self, transitionFunction, rewardFunction, stateSpace, actionSpaceFunction):
		
		bellmanUpdate = vi.BellmanUpdate(stateSpace, actionSpaceFunction, transitionFunction, rewardFunction, self.gamma)
		valueItSetUp = vi.ValueIteration(stateSpace, actionSpaceFunction, self.convergenceTolerance, bellmanUpdate)
		V = valueItSetUp()
		policySetUp = vi.GetPolicy(stateSpace, actionSpaceFunction, transitionFunction, rewardFunction, self.gamma, V, self.convergenceTolerance)
		
		return {s: policySetUp(s) for s in stateSpace}
		
#main landmark option set up class
class SetUpLandmark(object): 
	def __init__(self, landmarkLocation, landmarkStateSet, primitiveOptions, transitionFunction, rewardFunction, getLandmarkPolicy, merge):
		self.landmarkLocation = landmarkLocation
		self.landmarkStateSet = landmarkStateSet
		
		self.options = primitiveOptions
		
		self.transitionFunction = transitionFunction
		self.rewardFunction = rewardFunction
		self.getLandmarkPolicy = getLandmarkPolicy
		
		self.merge = merge
	def __call__(self, existingOptions):
		landmark = {option: self.getOptionPolicy(option) for option in self.landmarkLocation.keys()}
		
		return self.merge(landmark, existingOptions)
	
	def getOptionPolicy(self, option):
		stateSpace = self.landmarkStateSet[option]
		actionSet = list(self.options.keys())
		actionSpace = {state: actionSet for state in stateSpace}
		actionSpaceFunction = lambda s: actionSpace[s]
		
		return self.getLandmarkPolicy(self.transitionFunction, self.rewardFunction, stateSpace, actionSpaceFunction)
