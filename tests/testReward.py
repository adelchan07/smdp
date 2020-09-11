"""
Created on Wed Sep 3 12:03:38 2020

@author: adelphachan

testReward.py
"""
import sys
sys.path.append('../executive/')

import numpy as np
import unittest
from ddt import ddt, data, unpack
import rewardFunction as targetCode 

@ddt
class TestPrimitiveReward(unittest.TestCase):
	def setUp(self):
		actionCost = -1
		moveCost = -3
		goalStates = [(0,0)]
		goalReward = 10

		primitivePolicies = {'up': (0,1), 'down': (0,-1), 'right': (1,0), 'left': (-1,0)}
		stateSet = [(i,j) for i in range(2) for j in range(2)]
		getNextState = targetCode.tf.getNextState
		getPrimitiveSPrime = targetCode.tf.GetPrimitiveSPrime(primitivePolicies, stateSet, getNextState)

		self.getReward = targetCode.GetPrimitiveOptionReward(actionCost, moveCost, goalStates, goalReward, getPrimitiveSPrime)

	@data(((0,1), 'down', (0,0)), ((1,0), 'left', (0,0)))
	@unpack
	def test_ToGoal(self, state, option, sPrime):
		self.assertAlmostEqual(self.getReward(state, option, sPrime), 6)
	
	@data(((0,0), 'up', (0,1)), ((0,0), 'right', (1,0)))
	@unpack
	def test_NotGoal(self, state, option, sPrime):
		self.assertAlmostEqual(self.getReward(state, option, sPrime), -4)
	
	@data(((0,1), 'down', (1,0)), ((1,0), 'left', (1,0)))
	@unpack
	def test_WrongSPrime(self, state, option, sPrime):
		self.assertAlmostEqual(self.getReward(state, option, sPrime), 0)

@ddt
class TestLandmarkReward(unittest.TestCase):
	def setUp(self):
		actionCost = -1
		moveCost = -3
		goalStates = [(0,0)]
		goalReward = 10
		
		landmarkPolicies = {'h1': {(0, 0): {(0, -1): 0.5, (-1, 0): 0.5}, (0, 1): {(0, -1): 1.0}, (1, 0): {(-1, 0): 1.0}, (1, 1): {(0, -1): 0.5, (-1, 0): 0.5}}}
		
		getNextState = targetCode.tf.getNextState
		optionTerminations = {"h1": (0,0)}
		landmarkSPrime = targetCode.tf.GetLandmarkSPrime(optionTerminations)
		
		self.getReward = targetCode.GetLandmarkOptionReward(actionCost, moveCost, goalStates, goalReward, landmarkPolicies, landmarkSPrime, getNextState)
		
	@data(((0,0), 'h1', (0,0)))
	@unpack
	def test_AlreadyAtHallway(self, state, option, sPrime):
		self.assertAlmostEqual(self.getReward(state, option, sPrime), 7)
	
	@data(((1,1), 'h1', (0,0), 5), ((0,1), 'h1', (0,0), 6), ((1,0), 'h1', (0,0), 6))
	@unpack
	def test_ValidStates(self, state, option, sPrime, expectedReward):
		self.assertAlmostEqual(self.getReward(state, option, sPrime), expectedReward)
	
	@data(((1,1), 'h1', (1,0)),((1,0), 'h1', (1,1)))
	@unpack
	def test_WrongSPrime(self, state, option, sPrime):
		self.assertAlmostEqual(self.getReward(state, option, sPrime), 0)
	
	def tearDown(self):
		pass
		
		
@ddt
class TestRewardFunction(unittest.TestCase):
	def setUp(self):
		actionCost = -1
		moveCost = -3
		goalStates = [(0,0)]
		goalReward = 10
		
		primitivePolicies = {'up': (0,1), 'down': (0,-1), 'right': (1,0), 'left': (-1,0)}
		stateSet = [(i,j) for i in range(2) for j in range(2)]
		getNextState = targetCode.tf.getNextState
		primitiveSPrime = targetCode.tf.GetPrimitiveSPrime(primitivePolicies, stateSet, getNextState)
		primitiveReward = targetCode.GetPrimitiveOptionReward(actionCost, moveCost, goalStates, goalReward, primitiveSPrime)
		
		landmarkPolicies = {'h1': {(0, 0): {(0, -1): 0.5, (-1, 0): 0.5}, (0, 1): {(0, -1): 1.0}, (1, 0): {(-1, 0): 1.0}, (1, 1): {(0, -1): 0.5, (-1, 0): 0.5}}}
		optionTerminations = {"h1": (0,0)}
		landmarkSPrime = targetCode.tf.GetLandmarkSPrime(optionTerminations)
		landmarkReward = targetCode.GetLandmarkOptionReward(actionCost, moveCost, goalStates, goalReward, landmarkPolicies, landmarkSPrime, getNextState)
		
		optionReward = {'up': primitiveReward, 'down': primitiveReward, 'left': primitiveReward, 'right': primitiveReward,'h1': landmarkReward} 
		self.rewardFunction = targetCode.RewardFunction(optionReward)
	
	@data(((0,0), 'up', (0,1)), ((0,0), 'right', (1,0)))
	@unpack
	def test_PrimitiveNonReward(self, state, option, sPrime):
		self.assertEqual(self.rewardFunction(state, option, sPrime), -4)

	@data(((0,1), 'down', (0,0)), ((1,0), 'left', (0,0)))
	@unpack
	def test_PrimitiveReward(self, state, option, sPrime):
		self.assertEqual(self.rewardFunction(state, option, sPrime), 6)

	@data(((1,1), 'h1', (0,0), 5), ((0,1), 'h1', (0,0), 6), ((1,0), 'h1', (0,0), 6))
	@unpack
	def test_Landmark(self, state, option, sPrime, expectedReward):
		self.assertAlmostEqual(self.rewardFunction(state, option, sPrime), expectedReward)
	
	@data(((1,1), 'h1', (1,0)), ((1,0), 'h1', (1,0)))
	@unpack
	def test_WrongSPrime(self, state, option, sPrime):
	      self.assertEqual(self.rewardFunction(state, option, sPrime), 0)
	      
	def tearDown(self):
		pass
	
		
if __name__ == '__main__':
	unittest.main(verbosity=2)
