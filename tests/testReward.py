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
		primitiveSPrime = targetCode.tf.getPrimitiveSPrime(primitivePolicies, stateSet, getNextState)

		self.primitiveReward = targetCode.getPrimitiveOptionReward(actionCost, moveCost, goalStates, goalReward, primitivePolicies, primitiveSPrime)

		self.actionCost = actionCost
		self.moveCost = moveCost
		self.goalReward = goalReward

	@data(((0,0), 'up'), ((0,0), 'right'))
	@unpack
	def test_NonReward(self, state, option):
		self.assertEqual(self.primitiveReward(state, option), self.actionCost + self.moveCost)

	@data(((0,1), 'down'), ((1,0), 'left'))
	@unpack
	def test_Reward(self, state, option):
		self.assertEqual(self.primitiveReward(state, option), self.actionCost + self.moveCost + self.goalReward)

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
		landmarkSPrime = targetCode.tf.getLandmarkSPrime(optionTerminations)

		self.landmarkReward = targetCode.(actionCost, moveCost, goalStates, goalReward, landmarkPolicies, landmarkSPrime, getNextState)

	@data(((1,0), 'LL', 6), ((0,0), 'LL', 7))
	@unpack
	def test_NonReward(self, state, option, expectedReward):
		self.assertEqual(self.landmarkReward(state, option), expectedReward)

	@data(((0,0), 'UR', -5), ((1,0), 'UR', -4))
	@unpack
	def test_Reward(self, state, option, expectedReward):
		self.assertEqual(self.landmarkReward(state, option), expectedReward)

	def tearDown(self):
		pass
"""
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
		
		optionReward = {'up': primitiveReward, 'down': primitiveReward, 'left': primitiveReward, 'right': primitiveReward, 'LL':landmarkReward, 'UL': landmarkReward, 'UR': landmarkReward, 'LR': landmarkReward}
		self.rewardFunction = targetCode.rewardFunction(optionReward)
		
	@data(((0,0), 'up', (0,1), -4), ((1,0), 'left', (0,0), 6))
	@unpack
	def test_Primitive(self, state, option, sPrime, expectedReward):
		self.assertEqual(self.rewardFunction(state, option, sPrime), expectedReward)
	
	@data(((0,0), "UR", (1,1), -5), ((1,1), "LL", (0,0), 5))
	@unpack
	def test_Landmark(self, state, option, sPrime, expectedReward):
		self.assertEqual(self.rewardFunction(state, option, sPrime), expectedReward)
	
	def tearDown(self):
		pass
"""
		
if __name__ == '__main__':
	unittest.main(verbosity=2)
