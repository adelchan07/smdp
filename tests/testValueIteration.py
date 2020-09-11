import sys
sys.path.append('..') 

import numpy as np
import unittest
from ddt import ddt, data, unpack
import valueIteration as targetCode 

@ddt
class TestValueIteration(unittest.TestCase):
	def setUp(self):
		stateSet = [(i,j) for i in range(2) for j in range(2)]
		getNextState = targetCode.tf.getNextState
		primitivePolicies = {'up': (0,1), 'down': (0,-1), 'right': (1,0), 'left': (-1,0)}
		primitiveSPrime = targetCode.tf.GetPrimitiveSPrime(primitivePolicies, stateSet, getNextState)
		
		optionTerminations = {"h1": (0,0)}
		landmarkSPrime = targetCode.tf.GetLandmarkSPrime(optionTerminations)
		
		actionCost = -1
		moveCost = -3
		goalStates = [(0,0)]
		goalReward = 10
		primitiveReward = targetCode.rf.GetPrimitiveOptionReward(actionCost, moveCost, goalStates, goalReward, primitiveSPrime)
		
		landmarkPolicies = {'h1': {(0, 0): {(0, -1): 0.5, (-1, 0): 0.5}, (0, 1): {(0, -1): 1.0}, (1, 0): {(-1, 0): 1.0}, (1, 1): {(0, -1): 0.5, (-1, 0): 0.5}}}
		landmarkReward = targetCode.rf.GetLandmarkOptionReward(actionCost, moveCost, goalStates, goalReward, landmarkPolicies, landmarkSPrime, getNextState)
		
		optionSPrime = {'up': primitiveSPrime, 'down':primitiveSPrime, 'left': primitiveSPrime, 'right': primitiveSPrime,'h1': landmarkSPrime} 
		transitionFunction = targetCode.tf.TransitionFunction(optionSPrime)
		
		optionReward = {'up': primitiveReward, 'down': primitiveReward, 'left': primitiveReward, 'right': primitiveReward, 'h1':landmarkReward}
		rewardFunction = targetCode.rf.RewardFunction(optionReward)
		
		universal = ['up','down','left','right','h1']
		optionSpace = {state: universal for state in stateSet}
		optionSpaceFunction = targetCode.osf.OptionSpaceFunction(optionSpace)
		
		gamma = 0.9
		convergenceTolerance = 0.00001
		
		bellmanUpdate = targetCode.BellmanUpdate(stateSet, optionSpaceFunction, transitionFunction, rewardFunction, gamma)
		valueItSetUp = targetCode.ValueIteration(stateSet, optionSpaceFunction, convergenceTolerance, bellmanUpdate)
		V = valueItSetUp()
		
		policySetUp = targetCode.GetPolicy(stateSet, optionSpaceFunction, transitionFunction, rewardFunction, gamma, V, convergenceTolerance)
		self.policy = {s:policySetUp(s) for s in stateSet}
		
	def assertNumericDictAlmostEqual(self, calculatedDictionary, expectedDictionary, places=7):
    		self.assertEqual(calculatedDictionary.keys(), expectedDictionary.keys())
    		for key in calculatedDictionary.keys():
        		self.assertAlmostEqual(calculatedDictionary[key], expectedDictionary[key], places=places)
	
	@data(((0,0), {'h1': 1.0})) #only move cost
	@unpack
	def test_AtGoal(self, state, expectedResult):
		self.assertNumericDictAlmostEqual(self.policy[state], expectedResult)

	@data(((1,0), {'left': 0.5, 'h1': 0.5}), ((0,1), {'down': 0.5, 'h1': 0.5})) #both options = -4 cost
	@unpack
	def test_TwoOptions(self, state, expectedResult):
		self.assertNumericDictAlmostEqual(self.policy[state], expectedResult)
	
	@data(((1,1), {'h1': 1.0})) #primitive actions = additional penalty of move cost
	@unpack
	def test_GoToGoal(self, state, expectedResult):
		self.assertNumericDictAlmostEqual(self.policy[state], expectedResult)
	
	def tearDown(self):
		pass
  
if __name__ == '__main__':
	unittest.main(verbosity=2)

