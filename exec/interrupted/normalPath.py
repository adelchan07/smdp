class GetNormalPath(object):
	def __init__(self, landmarkPolicies, interruptionPolicy, optionTerminations, getNextState, goalStates, stateSet):
		self.landmarkPolicies = landmarkPolicies
		self.interruptionPolicy = interruptionPolicy
		self.optionTerminations = optionTerminations
		self.getNextState = getNextState
		self.goalStates = goalStates
		self.stateSet = stateSet

	def __call__(self, state):
		currentState = state
		path = {}

		while currentState not in self.goalStates:

			currentOption = list(self.interruptionPolicy[state].keys())[0]
			termination = self.optionTerminations[currentOption]
			currentState, path = self.getPath(currentState, currentOption, termination, path)	
		return path
	
	def getPath(self, state, currentOption, termination, path):
		currentState = state
		
		while currentState != termination:
			action = list(self.landmarkPolicies[currentOption][state].keys())[0]
			path[currentState] = action
			currentState = self.getNextState(currentState, action, self.stateSet)
		return (currentState, path)

