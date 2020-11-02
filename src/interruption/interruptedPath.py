class GetInterruptedPath(object):
	def __init__(self, optionPolicies, goalState, getOption, singleStep, CheckCondition, CompareOptions):
		
		self.optionPolicies = optionPolicies
		self.goalState = goalState

		self.getOption = getOption
		self.singleStep = singleStep

		self.checkCondition = CheckCondition
		self.compareOptions = CompareOptions

	def __call__(self, state):
		path = {}
		currentState = state
		currentOption = self.getOption(state)

		while currentState != self.goalState:
			specificStep = list(self.optionPolicies[currentOption][currentState].keys())[0]
			path[currentState] = specificStep

			sPrime = self.singleStep(currentState, currentOption)

			if self.checkCondition(currentState, sPrime):
				currentOption = self.compareOptions(sPrime, currentOption)
			currentState = sPrime

		return path

class GetOptionHistory(object):
	def __init__(self, optionPolicies, goalState, getOption, singleStep, CheckCondition, CompareOptions):
		
		self.optionPolicies = optionPolicies
		self.goalState = goalState

		self.getOption = getOption
		self.singleStep = singleStep

		self.checkCondition = CheckCondition
		self.compareOptions = CompareOptions

	def __call__(self, state):
		optionHistory = {}
		currentState = state
		currentOption = self.getOption(state)

		while currentState != self.goalState:
			path[currentOption] = currentOption

			sPrime = self.singleStep(currentState, currentOption)

			if self.checkCondition(currentState, sPrime):
				currentOption = self.compareOptions(sPrime, currentOption)
			currentState = sPrime

		return optionHistory
