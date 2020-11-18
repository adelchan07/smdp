import sys
sys.path.append('../../src')
import interruptedOptions as io

class GetInterruptedPath(object):
	def __init__(self, checkCondition, landmarkPolicies, interruptedPolicy, optionTerminations, getNextState, goalStates, stateSet):
		self.checkCondition = checkCondition
		self.landmarkPolicies = landmarkPolicies
		self.interruptedPolicy = interruptedPolicy
		self.optionTerminations = optionTerminations
		self.getNextState = getNextState
		self.goalStates = goalStates
		self.stateSet = stateSet

	def __call__(self, state):
		currentState = state
		path = {}

		while currentState not in self.goalStates:
			currentOption = list(self.interruptedPolicy[currentState].keys())[0]
			termination = self.optionTerminations[currentOption]
			currentState, path = self.getPath(currentState, currentOption, termination, path)
		
		return path

	
	def getPath(self, state, option, termination, path):
		currentState = state
		changeOption = False
		
		while changeOption == False and currentState != termination:
			action = list(self.landmarkPolicies[currentOption][currentState].keys())[0]
			path[currentState] = action
			newState = self.getNextState(currentState, action, self.stateSet)

			changeOption = self.checkCondition(currentState, newState)
			currentState = newState
		return (currentState, path)

class GetOptionHistory(object):
	def __init__(self, checkCondition, landmarkPolicies, interruptedPolicy, optionTerminations, getNextState, goalStates, stateSet):
		self.checkCondition = checkCondition
		self.landmarkPolicies = landmarkPolicies
		self.interruptedPolicy = interruptedPolicy
		self.optionTerminations = optionTerminations
		self.getNextState = getNextState
		self.goalStates = goalStates
		self.stateSet = stateSet

	def __call__(self, state):
		currentState = state
		record = {}

		while currentState not in self.goalStates:
			currentOption = list(self.interruptedPolicy[currentState].keys())[0]
			termination = self.optionTerminations[currentOption]
			currentState, record = self.getRecord(currentState, currentOption, termination, record)

		return record
	
	def getRecord(self, state, option, termination, record):
		currentState = state
		changeOption = False

		while changeOption == False and currentState != termination:
			record[currentState] = currentOption

			action = list(self.landmarkPolicies[currentOption][currentState].keys())[0]
			newState = self.getNextState(currentState, action, self.stateSet)

			changeOption = self.checkCondition(currentState, newState)
			currentState = newState
		return (currentState, record)
