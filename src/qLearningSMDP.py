"""
note: "PL" means primitive-landmark to symbolize the smdp option setUP
"""
import numpy as np 
import qLearning as ql

class QLearningSMDP(object):
	def __init__(self, episodes, convergenceTolerance):
		self.episodes = episodes
		self.convergenceTolerance = convergenceTolerance
    
	def __call__(self, stateSpace, PLreward, getSPrime, getOption, getQValue, QTable, goalStates, optionSpaceFunction):

		qLearning = ql.QLearning(PLreward, getSPrime, getOption, getQValue, stateSpace, self.episodes, goalStates)
		QTable = qLearning(QTable)

		getPolicy = ql.GetPolicy(self.convergenceTolerance, optionSpaceFunction) 
		policy = getPolicy(QTable)

		return (QTable, policy)

