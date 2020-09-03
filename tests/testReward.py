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
import reward as targetCode 

@ddt
class TestPrimitiveOptionReward(unittest.TestCase):
	def setUp(self):

		stateSet = [(i,j) for i in range(2) for j in range(2)]
		actionCost = -1
		moveCost = -3
		goalReward = 10
		goalStates = [(0,0)]
		getNextState = targetCode.getNextState

		self.getPrimitiveReward = targetCode.getPrimitiveOptionReward(stateSet, actionCost, moveCost, goalStates, goalReward, getNextState)

		upPolicy = {(0, 0): (0, 1), (0, 1): (0, 1), (1, 0): (0, 1), (1, 1): (0, 1)}
		downPolicy = {(0, 0): (0, -1), (0, 1): (0, -1), (1, 0): (0, -1), (1, 1): (0, -1)}
		leftPolicy = {(0, 0): (-1, 0), (0, 1): (-1, 0), (1, 0): (-1, 0), (1, 1): (-1, 0)}
		rightPolicy = {(0, 0): (1, 0), (0, 1): (1, 0), (1, 0): (1, 0), (1, 1): (1, 0)}

		self.landOnReward = actionCost + moveCost + goalReward
		self.noReward = actionCost + moveCost

	@data(((1,0), {(0, 0): (-1, 0), (0, 1): (-1, 0), (1, 0): (-1, 0), (1, 1): (-1, 0)}), ((0,0), {(0, 0): (0, -1), (0, 1): (0, -1), (1, 0): (0, -1), (1, 1): (0, -1)}), ((0,1), {(0, 0): (0, -1), (0, 1): (0, -1), (1, 0): (0, -1), (1, 1): (0, -1)}))
	@unpack
	def test_RewardPrimitiveOption(self, state, optionPolicy):
		self.assertEqual(self.getPrimitiveReward(state, optionPolicy), self.landOnReward)

	@data(((1,0), {(0, 0): (0, 1), (0, 1): (0, 1), (1, 0): (0, 1), (1, 1): (0, 1)}), ((0,0), {(0, 0): (1, 0), (0, 1): (1, 0), (1, 0): (1, 0), (1, 1): (1, 0)}), ((0,1), {(0, 0): (-1, 0), (0, 1): (-1, 0), (1, 0): (-1, 0), (1, 1): (-1, 0)}))
	@unpack
	def test_NonRewardPrimitiveOption(self, state, optionPolicy):
		self.assertEqual(self.getPrimitiveReward(state, optionPolicy), self.noReward)

	def tearDown(self):
		pass

@ddt
class TestLandmarkOptionReward(unittest.TestCase):
	def setUp(self):

		stateSet = [(i,j) for i in range(2) for j in range(2)]
		actionCost = -1
		moveCost = -3
		goalReward = 10
		goalStates = [(0,0)]
		getNextState = targetCode.getNextState

		self.getLandmarkReward = targetCode.getLandmarkOptionReward(stateSet, actionCost, moveCost, goalStates, goalReward, getNextState)

		landmarks = {"LL": (0,0), "UL": (0,1), "LR": (1,0), "UR": (1,1)}

		self.LL = {(0, 0): (0, -1), (0, 1): (0, -1), (1, 0): (-1, 0), (1, 1): (0, -1)}
		self.LLtermination = (0,0)

		self.UL = {(0, 0): (0, 1), (0, 1): (0, 1), (1, 0): (0, 1), (1, 1): (-1, 0)}
		self.ULtermination = (0,1)

		self.LR = {(0, 0): (1, 0), (0, 1): (1, 0), (1, 0): (0, -1), (1, 1): (0, -1)}
		self.LRtermination = (1,0)

		self.UR = {(0, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, 1), (1, 1): (0, 1)}
		self.URtermination = (1,1)

	#location w/ reward == LL landmark (terminationCondition = goalstate)
	@data(((0,0), 7), ((1,0), 6), ((1,1), 5))
	@unpack
	def test_RewardLandmarkOption(self, state, expectedReward):
		self.assertEqual(self.getLandmarkReward(state, self.LL, self.LLtermination), expectedReward)

	#testing UL, LR, and UR policies (not testing LL which is the goalstate)
	@data(((1,1), {(0, 0): (0, 1), (0, 1): (0, 1), (1, 0): (0, 1), (1, 1): (-1, 0)}, (0,1), -4), ((0,0), {(0, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, 1), (1, 1): (0, 1)}, (1,1), -5), ((0,1), {(0, 0): (0, 1), (0, 1): (0, 1), (1, 0): (0, 1), (1, 1): (-1, 0)}, (0,1), -3))
	@unpack
	def test_NonRewardLandmarkOption(self, state, optionPolicy, terminationCondition, expectedReward):
		self.assertEqual(self.getLandmarkReward(state, optionPolicy, terminationCondition), expectedReward)

	def tearDown(self):
		pass
		
if __name__ == '__main__':
	unittest.main(verbosity=2)