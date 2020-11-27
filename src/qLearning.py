import numpy as np
import random as rd

class QLearning(object):

 	def __init__(self, transitionFunction, rewardFunction, optionSpaceFunction, episodes, alpha, gamma, epsilon, goalStates):
		self.transitionFunction = transitionFunction
		self.rewardFunction = rewardFunction
		self.optionSpaceFunction = optionSpaceFunction

		self.numEpisodes = episodes
		self.alpha = alpha
		self.gamma = gamma
		self.goalStates = goalStates
		self.epsilon = epsilon

	def __call__(self, stateSpace, availableOptions):

		self.QTable = self.createQTable(stateSpace, availableOptions)

		for i in range(self.numEpisodes):
			state = np.random.choice(self.stateSet) #randomly pick starting point
			reward = 0 #keeping track of cumulative reward of the episode

			while state not in self.goalStates:
				option = self.getOption(state)

				sPrime = sum([self.transitionFunction(state, option, possibleSPrime) for possibleSPrime in self.stateSet]) #not sure if this is the best way but this is what is done in the valueIteration code
				reward += self.rewardFunction(state, option, sPrime) #check if these inputs are correct

				newQValue = self.getQValue(state, option, sPrime, reward)
				self.QTable[state][option] = newQValue

		return self.QTable

	def createQTable(self, stateSpace, availableOptions): #not sure if this should be created outside and passed into the callable
		Q = {}

		for state in stateSpace:
			stateDict = {}

			for option in availableOptions:
				stateDict[option] = 0

			Q[state] = stateDict

		return Q

	def getOption(self, state): #action obtained through an e-greedy policy
		e = rd.uniform(0,1)

		if e > self.epsilon:
			availableOptions = self.optionSpaceFunction(state)
			return np.random.choice(availableOptions)

		else:
			availableOptions = self.QTable[state]
			return max(availableOptions.keys(), key = lambda x: availableOptions[x])

	def getQValue(self, state, option, sPrime, reward):

		qSPrime = self.getQValueSPrime(sPrime)
		currentVal = self.QTable[state][option]

		qValue = ((1-self.alpha) * currentVal) + (self.alpha * (reward + (self.gamma * qSPrime)))
		return qValue

	def getQValueSPrime(self, sPrime):
		availableOptions = self.QTable[sPrime]
		return max(availableOptions.values()) #return maximum Q value coming from sPrime


class GetPolicy(object):

	def __init__(self, roundingTolerance, optionSpaceFunction):
		self.roundingTolerance = roundingTolerance
		self.optionSpaceFunction = optionSpaceFunction

	def __call__(self, qTable): #can either plug in qTable OR plug in each individual state into the q table
		self.QTable = qTable

		policy = {state: self.getOptimalOptions(state) for state in self.QTable.keys()}
		return policy

	def getOptimalOptions(self, state):
		Qs = {option: self.QTable[state][option] for option in self.QTable[state].keys()}
		optimalOptionsList = [o for o in self.optionSpaceFunction(state) if abs(Qs[o] - max(Qs.values())) < self.roundingTolerance]

		optionPolicy = {o: 1/(len(optimalOptionsList)) for o in optimalOptionsList}
		return optionPolicy

