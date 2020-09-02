"""
Created on Sun Jul  5 12:55:42 2020

@author: adelphachan

valueIteration.py
"""
import numpy as np
import transitionTable as createTransitionTable
import rewardTable as createRewardTable

class valueIteration(object):

    def __init__(self, transitionTable, rewardTable, V, convergenceTolerance, gamma):
        self. transitionTable = transitionTable
        self.rewardTable = rewardTable
        self.V = V
        self.convergenceTolerance = convergenceTolerance
        self.gamma = gamma


    def __call__(self):
        delta = self.convergenceTolerance * 100 #arbitrary number to intiate entrance into the while loop

        while delta > self.convergenceTolerance:
            delta = 0

            for state in self.transitionTable.keys():

                expectedValues = self.getExpectedValues(state)
                bestAction = self.getMaxValue(expectedValues)
                diffVal = abs(expectedValues[bestAction] - self.V[state])
                delta = max(delta, diffVal) #update delta value

                self.V[state] = expectedValues[bestAction]

        policyTable = {state: self.getPolicy(state) for state in self.transitionTable.keys()}
        self.policy = policyTable
        
        return([self.V, policyTable])

    #helper functions
    
    def getExpectedValues(self,state):
        expVals = {action : 0 for action in self.transitionTable[state].keys()}

        for action in self.transitionTable[state].keys():
            for sPrime in self.rewardTable[state][action].keys():
                prob = self.transitionTable[state][action][sPrime]
                reward = self.rewardTable[state][action][sPrime]
                futureReward = self.gamma * self.V[sPrime]

                expVals[action] += prob * (reward + futureReward)

        return expVals

    def getMaxValue(self, dictionary):
        keysList = list(dictionary.keys())
        maxValue = keysList[np.argmax(list(dictionary.values()))]
        return maxValue #returns location of the KEY with the max value

    def getPolicy(self, state):
        expectedValues = self.getExpectedValues(state)
        bestAction = self.getMaxValue(expectedValues)
        #return({bestAction: 1/len(expectedValues)})
        return(bestAction) #no need to include probability in policy because this is deterministic
        
