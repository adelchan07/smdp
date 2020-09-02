"""
Created on Sun Aug 9 10:04:03 2020

@author: adelphachan

primitiveOptionSetUp.py

return = dictionary of primitive options
--> append values onto a dictionary that already exists
	(allows us to be able to add any type of option necessary to the same general option dictionary)

constants for all dictionaries:
- transition table / stateSet (already updated with blockList)
- actionCost 
- goalReward

primtiveOptions = {"direction": primitive action}

primtiveOptions = {"up": (0,1), "down": (0,-1), "left": (-1,0), "right": (1,0)}

"""

#general helper functions 
def merge(dictionary1, dictionary2):
	
	result = {**dictionary1, **dictionary2}
	return result
	

class setUpPrimitive(object):

	def __init__(self, stateSet, primitiveOptions, merge):

		self.stateSet = stateSet
		self.primitiveOptions = primitiveOptions

		self.merge = merge

	def __call__(self, existingOptions):

		primitive = {option: self.getPrimitivePolicy(option) for option in self.primitiveOptions.keys()}
		
		combination = self.merge(primitive, existingOptions)
		return combination

	#helper functions for primitive policy
	def getPrimitivePolicy(self, option):
		
		suggestedOption = self.primitiveOptions[option] #suggested primitive option = same for all states

		stateTransitionDistribution = {state: suggestedOption for state in self.stateSet}
		return stateTransitionDistribution
