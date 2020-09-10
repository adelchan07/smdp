"""
Created on Tue Sep 8 13:14:45 2020
@author: adelphachan
rewardFunctionSetUp.py

set up dictionary of corresponding reward function for each type of option
"""

class SetUpRewardFunction(object):
  
  def __init__(self, optionType, getPrimitiveOptionReward, getLandmarkOptionReward):
    self.optionType = optionType
    
    self.primitiveReward = getPrimitiveOptionReward
    self.landmarkReward = getLandmarkOptionReward
   
  def __call__(self):
    rewards = {option: self.getRewardFunction(option) for option in self.optionType.keys()}
    return rewards
  
  def getRewardFunction(self, option):
    type = self.optionType[option]
    
    if type == "primitive":
      return self.primitiveReward
    
    if type == "landmark":
      return self.landmarkReward
