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
sys.path.append(os.path.join(dirName, '..'))
sys.path.append('./basics/')  

from rewardTable import createRewardTable
from valueIteration import valueIteration

#general helper functions 
def merge(dictionary1, dictionary2):
	
	result = {**dictionary1, **dictionary2}
	return result

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

class getLandmarkRewardTable(object):

	def __init__(self, transitionTable, actionSet, actionCost, goalReward):
		self.transitionTable = transitionTable
		self. actionSet = actionSet

		self.actionCost = actionCost
		self.goalReward = goalReward

	def __call__(self, goalState):

		setUpReward = createRewardTable(self.transitionTable, self.actionSet)
		rewardTable = setUpReward(self.actionCost, self.goalReward, [goalState])
		return rewardTable

class setUpLandmark(object):

	def __init__(self, transitionTable, landmarks, getLandmarkRewardTable, getLandmarkPolicy, merge):

		self.transitionTable = transitionTable
		self.landmarks = landmarks

		#both will already be initiated in the main file (just need to run callable)
		self.getRewardTable = getLandmarkRewardTable
		self.getPolicy = getLandmarkPolicy

		self.merge = merge

	def __call__(self, existingOptions):

		landmark = {option: self.getOptionPolicy(option) for option in self.landmarks.keys()}
		combination = self.merge(landmark, existingOptions)

		return combination

	#helper functions
	def getOptionPolicy(self, option):

		goalState = self.landmarks[option]
		rewardTable = self.getRewardTable(goalState)

		policy = self.getPolicy(self.transitionTable, rewardTable)
		return policy
