"""
Created on Sun Oct 11 13:03:57 2020
@author: adelphachan
normalPath.py

given a state, return the "policy" (path) resulting from sMDP value iteration WITHOUT interruptions
"""

class primitivePolicyPath(object):
	def __init__(self, primitiveOptions):
		self.primitiveOptions = primitiveOptions

	def __call__(self, state, option, path):
		path[state] = self.primitiveOptions[option]

		return path

class landmarkPolicyPath(object):
	def __init__(self, landmarkPolicies, landmarkTermination):
		self.landmarkPolicies = landmarkPolicies
		self.landmarkTermination = landmarkTermination

	def __call__(self, state, option, path):
		currentState = state 
		endGoal = self.landmarkTermination[option]
		policy = self.landmarkPolicies[option]

		while currentState != endGoal:
			action = list(policy[state].keys())[0] #all optimal --> just pick first one
			path[currentState] = action

			currentState = (currentState[0] + action[0], currentState[1] + action[1])

		return path

class policyToPath(object):
	def __init__(self, optionType, primitivePolicyPath, landmarkPolicyPath):
		self.optionType = optionType
		self.primitivePolicyPath = primitivePolicyPath
		self.landmarkPolicyPath = landmarkPolicyPath
		self.result = {option: self.getFunction(option) for option in self.optionType.keys()}
    
    
	def getFunction(self, option):
		if self.optionType[option] == 'landmark':
			return self.landmarkPolicyPath
		return self.primitivePolicyPath
    
	def __call__(self, state, option, path):
		function = self.result[option]
		return function(state, option, path)

class primitiveSPrime(object):
	def __init__(self, stateSet, primitiveOptions):
		self.stateSet = stateSet
		self.primitiveOptions = primitiveOptions 

	def __call__(self, state, option):
		action = self.primitiveOptions[option]
		newState = (state[0] + action[0], state[1] + action[1])
		if newState in self.stateSet:
			return newState
		return state

class landmarkSPrime(object):
	def __init__(self, optionTermination):
		self.optionTermination = optionTermination

	def __call__(self, state, option):
		return self.optionTermination[option]

class getSPrime(object):
	def __init__(self, optionType, landmarkSPrime, primitiveSPrime):
		self.landmarkSPrime = landmarkSPrime
		self.primitiveSPrime = primitiveSPrime
		self.optionType = optionType
		self.optionFunction = {option: self.getFunction(option) for option in optionType.keys()}

	def getFunction(self, option):
		if self.optionType[option] == 'landmark':
			return self.landmarkSPrime
		return self.primitiveSPrime
	def __call__(self, state, option):
		function = self.optionFunction[option]
		return function(state, option)

class GetNormalPath(object):
	def __init__(self, policy, goalState, policyToPath, getSPrime):
		self.policy = policy
		self.goalState = goalState
		self.policyToPath = policyToPath
		self.getSPrime = getSPrime

	def __call__(self, state):
		path = {}
		currentState = state
        
		while currentState != self.goalState:
			option = list(self.policy[currentState].keys())[0] #since all are "optimal", pick randomly
			path = self.policyToPath(currentState, option, path)
			currentState = self.getSPrime(currentState, option)

		return path 
