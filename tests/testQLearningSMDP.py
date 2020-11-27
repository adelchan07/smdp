import numpy as np
import unittest
from ddt import ddt, data, unpack

import sys
sys.path.append('../exec/original/')
import transitionFunction as tf
import rewardFunction as rf

sys.path.append('../src/')
import qLearningSMDP as targetCode

@ddt
class TestValueIteration(unittest.TestCase):
	def setUp(self):
		stateSet = [(i,j) for i in range(2) for j in range(2)]
		getNextState = tf.getNextState
		primitivePolicies = {'up': (0,1), 'down': (0,-1), 'right': (1,0), 'left': (-1,0)}
		primitiveSPrime = tf.GetPrimitiveSPrime(primitivePolicies, stateSet, getNextState)
		
		optionTerminations = {"h1": (0,0)}
		landmarkSPrime = tf.GetLandmarkSPrime(optionTerminations)
		
		actionCost = -1
		moveCost = -3
		goalStates = [(0,0)]
		goalReward = 10
		primitiveReward = rf.GetPrimitiveOptionReward(actionCost, moveCost, goalStates, goalReward, primitiveSPrime)
		
		landmarkPolicies = {'h1': {(0, 0): {(0, -1): 0.5, (-1, 0): 0.5}, (0, 1): {(0, -1): 1.0}, (1, 0): {(-1, 0): 1.0}, (1, 1): {(0, -1): 0.5, (-1, 0): 0.5}}}
		landmarkReward = rf.GetLandmarkOptionReward(actionCost, moveCost, goalStates, goalReward, landmarkPolicies, landmarkSPrime, getNextState)
		
		optionSPrime = {'up': primitiveSPrime, 'down':primitiveSPrime, 'left': primitiveSPrime, 'right': primitiveSPrime,'h1': landmarkSPrime} 
		transitionFunction = tf.TransitionFunction(optionSPrime)
		
		optionReward = {'up': primitiveReward, 'down': primitiveReward, 'left': primitiveReward, 'right': primitiveReward, 'h1':landmarkReward}
		rewardFunction = rf.RewardFunction(optionReward)
		
		universal = ['up','down','left','right','h1']
		optionSpace = {state: universal for state in stateSet}
		optionSpaceFunction = lambda x: optionSpace[x]
		
		episodes = 500
    alpha = 0.5
    epsilon = 0.9
    gamma = 0.9
		convergenceTolerance = 0.00001
		
		QLearningSetUp = targetCode.QLearningSMDP(episodes, alpha, gamma, epsilon, convergenceTolerance)
    QTable, self.policy = QLearningSetUp(stateSet, transitionFunction, rewardFunction, optionSpaceFunction, goalStates, universal)
    
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
