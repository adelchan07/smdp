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
class TestPrimitiveOptionReward(unittest.TestCase):
	def setUp(self):
		stateSet = [(i,j) for i in range(2) for j in range(2)]
		actionCost = -1
		moveCost = -3
		goalStates = [(0,0)]
		goalReward = 10
		primitivePolicies = {'up': (0,1), 'down': (0,-1), 'right': (1,0), 'left': (-1,0)}
		
		getNextState = targetCode.tf.getNextState
		primitiveTransition = targetCode.tf.getPrimitiveSPrime(primitivePolicies, stateSet, getNextState)
		
		self.primitiveReward = targetCode.getPrimitiveOptionReward(actionCost, moveCost, goalStates, goalReward, primitivePolicies, primitiveTransition)
		
		self.landOnReward = actionCost + moveCost + goalReward
		self.noReward = actionCost + moveCost
		
	@data(((1,0), 'left'), ((0,1), 'down'), ((0,0), 'down'))
	@unpack
	def test_RewardOption(self, state, option):
		self.assertEqual(self,primitiveReward(state, option), self.landOnReward)
	
	@data(((1,0), 'up'), ((0,1), 'left'), ((0,0), 'right'))
	@unpack
	def test_NonRewardOption(self, state, option):
		self.assertEqual(self.primitiveReward(state, option), self.noReward)
	
	
	def tearDown(self):
		pass

@ddt
class TestLandmarkOptionReward(unittest.TestCase):
	def setUp(self):
		stateSet = [(i,j) for i in range(2) for j in range(2)]
		actionCost = -1
		moveCost = -3
		goalStates = [(0,0)]
		goalReward = 10
		primitivePolicies = {'up': (0,1), 'down': (0,-1), 'right': (1,0), 'left': (-1,0)}
		landmarkPolicies = {'LL': {(0, 0): (0, -1), (0, 1): (0, -1), (1, 0): (-1, 0), (1, 1): (0, -1)}, 'UL': {(0, 0): (0, 1), (0, 1): (0, 1), (1, 0): (0, 1), (1, 1): (-1, 0)}, 'LR': {(0, 0): (1, 0), (0, 1): (1, 0), (1, 0): (0, -1), (1, 1): (0, -1)}, 'UR': {(0, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, 1), (1, 1): (0, 1)}}

		getNextState = targetCode.tf.getNextState
	
		optionTerminations = {"LL": (0,0), "UL": (0,1), "LR": (1,0), "UR": (1,1)}
		landmarkTransition = targetCode.tf.getLandmarkSPrime(optionTerminations)
		
		self.landmarkReward = targetCode.getLandmarkOptionReward(actionCost, moveCost, goalStates, goalReward, landmarkPolicies, landmarkTransition, getNextState)
	
	@data(((1,0), "LL", 6), ((0,0), "LL", 7), ((1,1), "LL", 5))
	@unpack
	def test_RewardOption(self, state, option, expectedReward):
		self.assertEqual(self.landmarkReward(state, option), expectedReward)
	
	@data(((0,0), "UR", -5), ((1,0), "LR", -3), ((1,1), "LR", -4))
	@unpack
	def test_NonRewardOption(self, state, option, expectedReward):
		self.assertEqual(self.landmarkReward(state, option), expectedReward)
	
	def tearDown(self):
		pass

@ddt
class TestRewardFunction(unittest.TestCase):
	def setUp(self):
		stateSet = [(i,j) for i in range(2) for j in range(2)]
		actionCost = -1
		moveCost = -3
		goalStates = [(0,0)]
		goalReward = 10
		primitivePolicies = {'up': (0,1), 'down': (0,-1), 'right': (1,0), 'left': (-1,0)}
		landmarkPolicies = {'LL': {(0, 0): (0, -1), (0, 1): (0, -1), (1, 0): (-1, 0), (1, 1): (0, -1)}, 'UL': {(0, 0): (0, 1), (0, 1): (0, 1), (1, 0): (0, 1), (1, 1): (-1, 0)}, 'LR': {(0, 0): (1, 0), (0, 1): (1, 0), (1, 0): (0, -1), (1, 1): (0, -1)}, 'UR': {(0, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, 1), (1, 1): (0, 1)}}

		getNextState = targetCode.tf.getNextState
		primitiveTransition = targetCode.tf.getPrimitiveSPrime(primitivePolicies, stateSet, getNextState)
		primitiveReward = targetCode.getPrimitiveOptionReward(actionCost, moveCost, goalStates, goalReward, primitivePolicies, primitiveTransition)
	
		optionTerminations = {"LL": (0,0), "UL": (0,1), "LR": (1,0), "UR": (1,1)}
		landmarkTransition = targetCode.tf.getLandmarkSPrime(optionTerminations)
		landmarkReward = targetCode.getLandmarkOptionReward(actionCost, moveCost, goalStates, goalReward, landmarkPolicies, landmarkTransition, getNextState)
		
		optionReward = {}
		self.rewardFunction = targetCode.rewardFunction(optionReward)
		
	@data()
	@unpack
	def test_ValidPrimitiveSPrime(self, state, option, sPrime, expectedReward):
	
	@data()
	@unpack
	def test_InvalidPrimitiveSPrime(self, state, option, sPrime, expectedReward):
	
	@data()
	@unpack
	def test_ValidLandmarkSPrime(self, state, option, sPrime, expectedReward):
	
	@data()
	@unpack
	def test_InvalidLandmarkSPrime(self, state, option, sPrime, expectedReward):
	
	def tearDown(self):
		pass

		
if __name__ == '__main__':
	unittest.main(verbosity=2)
