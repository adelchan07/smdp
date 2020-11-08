class GetInterruptedPath(object):
	def __init__(self, checkCondition, landmarkPolicies, interruptedPolicy, optionTerminations, getNextState, goalState, stateSet):
		self.checkCondition = checkCondition
		self.landmarkPolicies = landmarkPolicies
		self.interruptedPolicy = interruptedPolicy
		self.optionTerminations = optionTerminations
		self.getNextState = getNextState
		self.goalState = goalState
		self.stateSet = stateSet

	def __call__(self, state):
		currentState = state
		path = {}

		while currentState != self.goalState:
			currentOption = list(self.interruptedPolicy[state].keys())[0]
			termination = self.optionTerminations[currentOption]

			changeOption = False
			while changeOption == False and currentState != termination:
				action = list(self.landmarkPolicies[currentOption][state].keys())[0]
				path[currentState] = action
				newState = self.getNextState(currentState, action, self.stateSet)

				changeOption = self.checkCondition(currentState, newState)
				currentState = newState

		return path

class GetOptionHistory(object):
	def __init__(self, checkCondition, landmarkPolicies, interruptedPolicy, optionTerminations, getNextState, goalState, stateSet):
		self.checkCondition = checkCondition
		self.landmarkPolicies = landmarkPolicies
		self.interruptedPolicy = interruptedPolicy
		self.optionTerminations = optionTerminations
		self.getNextState = getNextState
		self.goalState = goalState
		self.stateSet = stateSet

	def __call__(self, state):
		currentState = state
		record = {}

		while currentState != self.goalState:
			currentOption = list(self.interruptedPolicy[state].keys())[0]
			termination = self.optionTerminations[currentOption]

			changeOption = False
			while changeOption == False and currentState != termination:
				record[currentState] = currentOption

				action = list(self.landmarkPolicies[currentOption][state].keys())[0]
				newState = self.getNextState(currentState, action, self.stateSet)

				changeOption = self.checkCondition(currentState, newState)
				currentState = newState

		return record
