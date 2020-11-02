import numpy as np

class CheckCondition(object):
    def __init__(self, optionSpaceFunction):
        self.optionSpaceFunction = optionSpaceFunction
    
    def __call__(self, state, sPrime):
        current = self.optionSpaceFunction(state)
        next = self.optionSpaceFunction(sPrime)

        return !(current == next) #if same, return False

class CompareOptions(object):
    def __init__(self, optionSpaceFunction):
        self.optionSpaceFunction = optionSpaceFunction

    def __call__(self, state, currentOption):
        availableOptions = self.optionSpace[state]

        for option in availableOptions:
            if option != currentOption: return option #favor change

        return currentOption #keep current option if no other ones available
