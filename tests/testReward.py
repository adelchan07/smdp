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
		primitiveSPrime = targetCode.tf.GetPrimitiveSPrime(primitivePolicies, stateSet, getNextState)

		self.primitiveReward = targetCode.GetPrimitiveOptionReward(actionCost, moveCost, goalStates, goalReward, primitiveSPrime)

		self.actionCost = actionCost
		self.moveCost = moveCost
		self.goalReward = goalReward

	@data(((0,0), 'up', (0,1)), ((0,0), 'right', (1,0)))
	@unpack
	def test_NonReward(self, state, option, sPrime):
		self.assertEqual(self.primitiveReward(state, option, sPrime), self.actionCost + self.moveCost)

	@data(((0,1), 'down', (0,0)), ((1,0), 'left', (0,0)))
	@unpack
	def test_Reward(self, state, option, sPrime):
		self.assertEqual(self.primitiveReward(state, option, sPrime), self.actionCost + self.moveCost + self.goalReward)
	
	@data(((0,1), 'down', (1,0)), ((1,0), 'left', (1,0)))
	@unpack
	def test_WrongSPrime(self, state, option, sPrime):
	      self.assertEqual(self.primitiveReward(state, option, sPrime), 0)
	      
	def tearDown(self):
		pass

@ddt
class TestLandmarkReward(unittest.TestCase):
	def setUp(self):

		actionCost = -1
		moveCost = -3
		goalStates = [(0,0)]
		goalReward = 10
		
		landmarkPolicies = {'LL': {(0, 0): (0, -1), (0, 1): (0, -1), (1, 0): (-1, 0), (1, 1): (0, -1)}, 'UL': {(0, 0): (0, 1), (0, 1): (0, 1), (1, 0): (0, 1), (1, 1): (-1, 0)}, 'LR': {(0, 0): (1, 0), (0, 1): (1, 0), (1, 0): (0, -1), (1, 1): (0, -1)}, 'UR': {(0, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, 1), (1, 1): (0, 1)}}

		getNextState = targetCode.tf.getNextState
		
		optionTerminations = {"LL": (0,0), "UL": (0,1), "LR": (1,0), "UR": (1,1)}
		landmarkSPrime = targetCode.tf.GetLandmarkSPrime(optionTerminations)

		self.landmarkReward = targetCode.GetLandmarkOptionReward(actionCost, moveCost, goalStates, goalReward, landmarkPolicies, landmarkSPrime, getNextState)

	@data(((1,0), 'LL', 6, (0,0)), ((0,0), 'LL', 7, (0,0)))
	@unpack
	def test_Reward(self, state, option, sPrime, expectedReward):
		self.assertEqual(self.landmarkReward(state, option, sPrime), expectedReward)

	@data(((0,0), 'UR', -5, (1,1)), ((1,0), 'UR', -4, (1,1)))
	@unpack
	def test_NonReward(self, state, option, sPrime, expectedReward):
		self.assertEqual(self.landmarkReward(state, option, sPrime), expectedReward)
	
	@data(((0,0), 'UR', -5, (0,1)), ((1,0), 'UR', -4, (1,0)))
	@unpack
	def test_WrongSPrime(self, state, option, sPrime):
	      self.assertEqual(self.landmarkReward(state, option, sPrime), 0)
	
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
		
		landmarkPolicies = {'LL': {(0, 0): (0, -1), (0, 1): (0, -1), (1, 0): (-1, 0), (1, 1): (0, -1)}, 'UL': {(0, 0): (0, 1), (0, 1): (0, 1), (1, 0): (0, 1), (1, 1): (-1, 0)}, 'LR': {(0, 0): (1, 0), (0, 1): (1, 0), (1, 0): (0, -1), (1, 1): (0, -1)}, 'UR': {(0, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, 1), (1, 1): (0, 1)}}
		optionTerminations = {"LL": (0,0), "UL": (0,1), "LR": (1,0), "UR": (1,1)}
		landmarkSPrime = targetCode.tf.GetLandmarkSPrime(optionTerminations)
		landmarkReward = targetCode.GetLandmarkOptionReward(actionCost, moveCost, goalStates, goalReward, landmarkPolicies, landmarkSPrime, getNextState)
		
		optionReward = {'up': primitiveReward, 'down': primitiveReward, 'left': primitiveReward, 'right': primitiveReward, 'LL':landmarkReward, 'UL': landmarkReward, 'UR': landmarkReward, 'LR': landmarkReward} 
		self.rewardFunction = targetCode.RewardFunction(optionReward)
		
		self.actionCost = actionCost
		self.moveCost = moveCost
		self.goalReward = goalReward
	
	@data(((0,0), 'up', (0,-1)), ((0,0), 'right', (1,0)))
	@unpack
	def test_PrimitiveNonReward(self, state, option, sPrime):
		self.assertEqual(self.rewardFunction(state, option, sPrime), self.actionCost + self.moveCost)

	@data(((0,1), 'down', (0,0)), ((1,0), 'left', (0,0)))
	@unpack
	def test_PrimitiveReward(self, state, option, sPrime):
		self.assertEqual(self.rewardFunction(state, option, sPrime), self.actionCost + self.moveCost + self.goalReward)

	@data(((1,0), 'LL', (0,0), 6), ((0,0), 'LL', (0,0), 7))
	@unpack
	def test_LandmarkNonReward(self, state, option, sPrime, expectedReward):
		self.assertEqual(self.rewardFunction(state, option, sPrime), expectedReward)

	@data(((0,0), 'UR', (1,1), -5), ((1,0), 'UR', (1,1), -4))
	@unpack
	def test_Reward(self, state, option, sPrime, expectedReward):
		self.assertEqual(self.rewardFunction(state, option, sPrime), expectedReward)
	
	@data(((0,0), 'UR', (1,1), -5), ((1,0), 'UR', (1,1), -4))
	@unpack
	def test_WrongSPrime(self, state, option, sPrime, expectedReward):
	      self.assertEqual(self.rewardFunction(state, option, sPrime), 0)
	      
	def tearDown(self):
		pass
	
		
if __name__ == '__main__':
	unittest.main(verbosity=2)
