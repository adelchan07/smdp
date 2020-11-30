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
            #print("on episode ", i)
            state = rd.choice(stateSpace) #randomly pick starting point
            reward = 0 #keeping track of cumulative reward of the episode

            while state not in self.goalStates:
                option = self.getOption(state)

                sPrime = self.getSPrime(state, option, stateSpace)
                #print("got sPrime")
                
                reward += self.rewardFunction(state, option, sPrime) #check if these inputs are correct
                #print("got reward")

                newQValue = self.getQValue(state, option, sPrime, reward)
                #print("got new Q value")
                
                self.QTable[state][option] = newQValue
                #print("updated Q table")
                
                state = sPrime
                #print("update state to become sPrime")
        
        #print("finished")
        return self.QTable

    def getSPrime(self, state, option, stateSpace):
        for possibleSPrime in stateSpace:
            if self.transitionFunction(state, option, possibleSPrime) == 1:
                return possibleSPrime
    
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
            availableOptions = self.optionSpaceFunction(state)
            return max(availableOptions, key = lambda x: self.QTable[state][x])

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
        Qs = {option: self.QTable[state][option] for option in self.optionSpaceFunction(state)}
        optimalOptionsList = [o for o in Qs.keys() if abs(Qs[o] - max(Qs.values())) < self.roundingTolerance]
        optionPolicy = {o: 1/(len(optimalOptionsList)) for o in optimalOptionsList}
        return optionPolicy


