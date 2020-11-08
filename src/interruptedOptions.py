import numpy as np

class CheckCondition(object):
    def __init__(self, optionSpaceFunction):
        self.optionSpaceFunction = optionSpaceFunction
    
    def __call__(self, state, sPrime):
        current = self.optionSpaceFunction(state)
        next = self.optionSpaceFunction(sPrime)

        return (current != next) #return True --> prompt next step if the options available at both states are different
