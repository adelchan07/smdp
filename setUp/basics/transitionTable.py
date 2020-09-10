"""
Created on Mon Jun 29 22:54:16 2020
@author: adelphachan
transitionTable.py
"""
import numpy as np

"""
Create transition table
Constructor:
    state set (grid dimensions)
    action set (list of actions as tuples)
    
Callable:
        list of transition barriers, list of tuples
            {(state, action)}
Output:
    nested dictionary
        {state:{action:{nextState:probability}}}
"""

class CreateTransitionTable(object):
  
  #constructor
    def __init__(self, actionSet):
        self.actionSet = actionSet
      
  #callable: output = list ONLY with barriers
    def __call__(self, stateSet): #input = list of barriers
        self.stateSet = stateSet
        transitionTable = {state: self.getStateTransitionTable(state) for state in self.stateSet} #set up initial transitionTable
        
        return(transitionTable)
      

  #helper functions for callable
    def getStateTransitionTable(self, state):
        actionTransitionDistribution = {action: self.getStateActionTransitionTable(state,action) for action in self.actionSet}
        return(actionTransitionDistribution)
  
    def getStateActionTransitionTable(self, currentState, action):
        nextState = self.getNextState(currentState, action)
        transitionDistribution = {nextState: 1}
        return(transitionDistribution)
  
    def getNextState(self, state, action):

        xCoord = state[0] + action[0]
        yCoord = state[1] + action[1]
     
        potentialNextState = (xCoord,yCoord)
     
        if potentialNextState in self.stateSet:
            state = potentialNextState
        return(state)
    
class TransitionFunction(object):
    def __init__(self, transitionTable):
        self.transitionTable = transitionTable
    
    def __call__(self, state, action, sPrime):
        return self.transitionTable.get(state).get(action).get(sPrime, 0)
 
