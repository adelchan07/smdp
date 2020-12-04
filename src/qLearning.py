import numpy as np
import random as rd

def createQTable(stateSpace, availableOptions):
       Q = {state: {option : 0 for option in availableOptions} for state in stateSpace}
       return Q
      
class GetSPrime(object):
    def __init__(self, transitionFunction, stateSpace):
        self.transitionFunction = transitionFunction
        self.stateSpace = stateSpace
    
    def __call__(state, option):
        for possibleSPrime in self.stateSpace:
            if self.transitionFunction(state, option, possibleSPrime) == 1:
                return possibleSPrime

class GetOption(object):
    def __init__(self, epsilon, optionSpaceFunction):
        self.epsilon = epsilon
        self.optionSpaceFunction = optionSpaceFunction
    
    def __call__(state, QTable):
        e = rd.uniform(0,1)

        if e > self.epsilon:
            availableOptions = self.optionSpaceFunction(state)
            return np.random.choice(availableOptions)

        else:
            availableOptions = self.optionSpaceFunction(state)
            return max(availableOptions, key = lambda x: QTable[state][x])

class GetQValue(object):
    def __init__(self, alpha, gamma):
        self.alpha = alpha
        self.gamma = gamma
    
    def __call__(self, state, option, sPrime, reward, QTable):
        qSPrime = max(QTable[sPrime].values())
        currentVal = QTable[state][option]
        
        qValue = currentVal + self.alpha * (reward + (self.gamma * qSPrime) - currentVal)
        return qValue

class QLearning(object):

    def __init__(self, transitionFunction, rewardFunction, optionSpaceFunction, getSPrime, getOption, getQValue, QTable, episodes, goalStates):
        self.transitionFunction = transitionFunction
        self.rewardFunction = rewardFunction
        self.optionSpaceFunction = optionSpaceFunction
        
        self.getSPrime = getSPrime
        self.getOption = getOption
        self.getQValue = getQValue

        self.QTable = QTable
        self.numEpisodes = episodes
        self.goalStates = goalStates

    def __call__(self, stateSpace):

        for i in range(self.numEpisodes):
            state = rd.choice(stateSpace)
            reward = 0

            while state not in self.goalStates:
                option = self.getOption(state, QTable)

                sPrime = self.getSPrime(state, option)
                reward += self.rewardFunction(state, option, sPrime)
                newQValue = self.getQValue(state, option, sPrime, reward, QTable)
                
                self.QTable[state][option] = newQValue
                
                state = sPrime
                
        return self.QTable

class GetPolicy(object):

    def __init__(self, roundingTolerance, optionSpaceFunction):
        self.roundingTolerance = roundingTolerance
        self.optionSpaceFunction = optionSpaceFunction

    def __call__(self, qTable): 
        self.QTable = qTable

        policy = {state: self.getOptimalOptions(state) for state in self.QTable.keys()}
        return policy

    def getOptimalOptions(self, state):
        Qs = {option: self.QTable[state][option] for option in self.optionSpaceFunction(state)}
        optimalOptionsList = [o for o in Qs.keys() if abs(Qs[o] - max(Qs.values())) < self.roundingTolerance]
        optionPolicy = {o: 1/(len(optimalOptionsList)) for o in optimalOptionsList}
        return optionPolicy


