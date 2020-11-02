"""
Created on Tue Sep 8 13:25:45 2020
@author: adelphachan
transitionFunctionSetUp.py

set up dictionary of corresponding transition function for each type of option
"""

class SetUpTransitionFunction(object):
  
  def __init__(self, optionType, getPrimitiveSPrime, getLandmarkSPrime):
    self.optionType = optionType
    
    self.primitiveTransition = getPrimitiveSPrime
    self.landmarkTransition = getLandmarkSPrime
   
  def __call__(self):
    transitions = {option: self.getTransitionFunction(option) for option in self.optionType.keys()}
    return transitions
  
  def getTransitionFunction(self, option):
    type = self.optionType[option]
    
    if type == "primitive":
      return self.getPrimitiveSPrime
    
    if type == "landmark":
      return self.getLandmarkSPrime
