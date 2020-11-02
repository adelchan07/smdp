class getOption(object):
	def __init__(self, optionType, policy):
		self.optionType = optionType
		self.policy = policy

	def __call__(self, state):
		options = self.policy[state]

		for option in options:
			if self.optionType[option] == 'landmark': return option

class singleStep(object):
	def __init__(self, optionPolicies, getNextState, stateSet):
		self.optionPolicies = optionPolicies
		self.getNextState = getNextState #getNextState from executive --> transition.py
		self.stateSet = stateSet

	def __call__(self, state, option):
		action = list(self.optionPolicies[option][state].keys())[0]
		return self.getNextState(state, action, self.stateSet)
