"""
note: "PL" means primitive-landmark to symbolize the smdp option setUP
"""
import numpy as np 
import qLearning as ql

class QLearningSMDP(object):
	def __init__(self, episodes, convergenceTolerance):
		self.episodes = episodes
		self.convergenceTolerance = convergenceTolerance
    
	def __call__(self, stateSet, PLtransition, PLreward, optionSpaceFunction, getSPrime, getOption, getQValue, QTable, goalStates):

		qLearning = ql.QLearning(PLtransition, PLreward, optionSpaceFunction, getSPrime, getOption, getQValue, QTable, self.episodes, goalStates)
		QTable = qLearning(stateSet)

		getPolicy = ql.GetPolicy(self.convergenceTolerance, optionSpaceFunction) 
		policy = getPolicy(QTable)

		return (QTable, policy)

