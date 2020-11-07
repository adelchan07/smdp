import numpy as np

class CheckCondition(object):
    def __init__(self, optionSpaceFunction):
        self.optionSpaceFunction = optionSpaceFunction
    
    def __call__(self, state, sPrime):
        current = self.optionSpaceFunction(state)
        next = self.optionSpaceFunction(sPrime)

        return (current != next) #return True --> prompt next step if the options available at both states are different

class CompareOptions(object):
    def __init__(self, optionSpaceFunction):
        self.optionSpaceFunction = optionSpaceFunction

    def __call__(self, state):
        availableOptions = self.optionSpace[state]

        return availableOptions[0] #since they are all optimal, can choose any
