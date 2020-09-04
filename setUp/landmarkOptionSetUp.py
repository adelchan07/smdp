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

from transitionTable import createTransitionTable
from rewardTable import createRewardTable
from valueIteration import valueIteration

#general helper functions 
def merge(self, dictionary1, dictionary2):
	
	result = {**dictionary1, **dictionary2}
	return result

class getTransitionTable(object):
	def __init__(self, actionSet):
		self.actionSet = actionSet

	def __call__(self, stateSet):
		setUpTransition = createTransitionTable(self.actionSet)
		transitionTable = setUpTransition(stateSet)

		return transitionTable

class getLandmarkRewardTable(object):

	def __init__(self, actionSet, actionCost, goalReward):

		self. actionSet = actionSet

		self.actionCost = actionCost
		self.goalReward = goalReward

	def __call__(self, transitionTable, goalState):

		setUpReward = createRewardTable(transitionTable, self.actionSet)
		rewardTable = setUpReward(self.actionCost, self.goalReward, [goalState])
		return rewardTable

class getLandmarkPolicy(object): #value iteration code modified for temporal abstraction

	def __init__(self, V, convergenceTolerance, gamma):
		self.V = V
		self.convergenceTolerance = convergenceTolerance
		self.gamma = gamma

	def __call__(self, transitionTable, rewardTable):

		getPolicy = valueIteration(transitionTable, rewardTable, self.V, self.convergenceTolerance, self.gamma)
		result = getPolicy()
		policy = result[1]

		return policy

#main landmark option set up class
class setUpLandmark(object):

	def __init__(self, landmarkLocation, landmarkStateSet, getTransitionTable, getLandmarkRewardTable, getLandmarkPolicy, merge):

		self.landmarkLocation = landmarkLocation
		self.landmarkStateSet = landmarkStateSet #option initiation set

		self.getTransitionTable = getTransitionTable
		self.getRewardTable = getLandmarkRewardTable
		self.getPolicy = getLandmarkPolicy

		self.merge = merge

	def __call__(self, existingOptions):

		landmark = {option: self.getOptionPolicy(option) for option in self.landmarkLocation.keys()}
		
		combination = self.merge(landmark, existingOptions)
		return combination

	def getOptionPolicy(self, option):

		transitionTable = self.getTransitionTable(self.landmarkStateSet[option])

		goalState = self.landmarkLocation[option]
		rewardTable = self.getRewardTable(transitionTable, goalState)

		policy = self.getPolicy(transitionTable, rewardTable)
		
		return policy
