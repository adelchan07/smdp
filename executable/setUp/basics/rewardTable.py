"""
Created on Mon Jun 29 22:54:58 2020

@author: adelphachan

rewardTable.py
"""

import numpy as np

"""
Create reward table

Constructor:
    state set (grid dimensions)
    action set (list of actions as tuples)
    
Callable:
        goal state
        action cost
        goal reward

Output: 
    nested dictionary 
        {state:{action:{nextState:reward}}}
        
Note: will need to modify value iteration in order to pass in a terminal state
      current code for an environment with a single goalState --> can be modified for a list of goal states
    
"""

class CreateRewardTable(object):

#constructor
    def __init__(self, actionSet, actionCost, goalReward): #question: is actionSet still necessary if we pass in the transitionTable
        
        self.actionSet = actionSet
        self.actionCost = actionCost
        self.goalReward = goalReward
    
    
#callable: goal state, action cost, and goal reward
    def __call__(self, transitionTable, goalStates): #actionCost and goalReward can be easily modified for different scenarios
    
    #set basics of the rewardTable
        rewardTable = {state:{action:{nextState: self.actionCost for nextState in possibleNextStates.keys() } \
                          for action, possibleNextStates in possibleActions.items()} \
                   for state, possibleActions in transitionTable.items()}
    
    #update rewardTable for the goalStates
        for state in rewardTable.keys():
            for action in rewardTable[state].keys():
                for nextState in rewardTable[state][action]:
                    for goalNext in goalStates:
                        if nextState == goalNext:
                            rewardTable[state][action] = {nextState:self.goalReward}
              
        return(rewardTable)

class RewardFunction(object):
    
    def __init__(self, rewardTable):
        self.rewardTable = rewardTable
        
    def __call__(self, state, action, sPrime):
        return self.rewardTable.get(state).get(action).get(sPrime, 0)
        