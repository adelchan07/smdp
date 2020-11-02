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
