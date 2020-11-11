"""
note: "PL" means primitive-landmark to symbolize the smdp option setUP
"""
import numpy as np 
import valueIteration as vi 

class SemiMDP(object):
	def __init__(self, gamma, convergenceTolerance):
		self.gamma = gamma
		self.convergenceTolerance = convergenceTolerance

	def __init__(self, stateSet, PLtransition, PLreward, optionSpaceFuncion):

		bellmanUpdate = vi.BellmanUpdate(stateSet, optionSpaceFuncion, PLtransition, PLreward, self.gamma)
		valueItSetUp = vi.ValueIteration(stateSet, optionSpaceFuncion, self.convergenceTolerance. bellmanUpdate)
		V = valueItSetUp()

		policySetUp = vi.GetPolicy(stateSet, optionSpaceFuncion, PLtransition, PLreward, self.gamma, V, self.convergenceTolerance)
		policy = {state: policySetUp(state) for state in stateSet}

		return (V, policy)
		
