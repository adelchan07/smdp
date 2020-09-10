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
import sys
import os
dirName = os.path.dirname(__file__)
sys.path.append(os.path.join(dirName, 'basics', ""))

import numpy as np
import transitionTable as tt
import rewardTable as rt
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
	
	def __call__(self, transitionTable, rewardTable):
		transitionFunction = tt.TransitionFunction(transitionTable)
		rewardFunction = rt.RewardFunction(rewardTable)
		stateSpace = list(transitionTable.keys())
		actionSpaceFunction = lambda s: list(transitionTable.get(s).keys())
		
		bellmanUpdate = vi.BellmanUpdate(stateSpace, actionSpaceFunction, transitionFunction, rewardFunction, self.gamma)
		valueItSetUp = vi.ValueIteration(stateSpace, actionSpaceFunction, self.convergenceTolerance, bellmanUpdate)
		V = valueItSetUp()
		policySetUp = vi.GetPolicy(stateSpace, actionSpaceFunction, transitionFunction, rewardFunction, self.gamma, V, self.convergenceTolerance)
		
		return {s: policySetUp(s) for state in stateSpace}
		
#main landmark option set up class
class SetUpLandmark(object): 
	def __init__(self, landmarkLocation, landmarkStateSet, actionSet, getTransitionTable, getRewardTable, getLandmarkPolicy, merge):
		self.landmarkLocation = landmarkLocation
		self.landmarkStateSet = landmarkStateSet
		
		self.actionSet = actionSet
		
		self.getTransitionTable = getTransitionTable
		self.getRewardTable = getRewardTable
		self.getLandmarkPolicy = getLandmarkPolicy
		self.merge = merge
	def __call__(self, existingOptions):
		landmark = {option: self.getOptionPolicy(option) for option in self.landmarkLocation.keys()}
		
		return self.merge(landmark, existingOptions)
	
	def getOptionPolicy(self, option):
		stateSet = self.landmarkStateSet[option]
		transitionTable = self.getTransitionTable(stateSet)
		
		goalStates = list(self.landmarkLocation[option])
		rewardTable = self.getRewardTable(transitionTable, goalStates)
		
		return self.getLandmarkPolicy(transitionTable, rewardTable)
