"""
Created on Mon Aug 17 13:54:03 2020
@author: adelphachan
optionSpaceFunction.py

optionSpace = dictionary in the format {(state): [list of names of options valid at this state]}
"""

class optionSpaceFunction(object):
  def __init__(self, optionSpace):
    self.optionSpace = optionSpace
   
  def __call__(self, state):
    availableOptions = self.optionSpace[state]
    return availableOptions
