"""
note: "PL" means primitive-landmark to symbolize the smdp option setUP
"""
import numpy as np 
import qLearning as ql

class SemiMDP(object):
	def __init__(self, episodes, alpha, gamma, epsilon, convergenceTolerance):
		self.episodes = episodes
    self.alpha = alpha
    self.gamma = gamma
    self.epsilon = epsilon
    self.convergenceTolerance = convergenceTolerance
    
	def __call__(self, stateSet, PLtransition, PLreward, optionSpaceFuncion, goalStates, availableOptions):
    
    qLearning = ql.QLearning(PLtransition, PLreward, optionSpaceFunction, self.episodes, self.alpha, self.gamma, self.epsilon, goalStates)
    QTable = qLearning(stateSet, availableOptions)

    getPolicy = ql.GetPolicy(self.convergenceTolerance, optionSpaceFunction) 
    policy = getPolicy(QTable)
  
		return (QTable, policy)
		
