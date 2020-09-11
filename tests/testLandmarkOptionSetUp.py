"""
Created on Thu Sep 3 9:14:23 2020

@author: adelphachan

testLandmarkOptionSetUp.py

getLandmarkPolicy and getLandmarkReward classes tested on a simple 2x2 grid
setUpLandmark class tested on 13x9 grid with hallways and outer border

class of test cases for each class present in landmarkOptionSetUp.py
merge function tested in testPrimitiveOptions.py
"""

import sys
sys.path.append('../setUp/')

import numpy as np
import unittest
from ddt import ddt, data, unpack
import landmarkOptionSetUp as targetCode 

@ddt
class TestGetLandmarkPolicy(unittest.TestCase):
	def setUp(self):
		gamma = 0.9
		convergenceTolerance = 0.001
		
		stateSet = [(i,j) for i in range(2) for j in range(2)]
		actionSet = [(0,1), (0,-1), (1,0), (-1,0)]
		actionCost = -1
		goalReward = 10
		goalStates = [(0,0)]
		
		setUp = targetCode.tt.CreateTransitionTable(actionSet)
		transitionTable = setUp(stateSet)
		
		setUp = targetCode.rt.CreateRewardTable(actionSet, actionCost, goalReward)
		rewardTable = setUp(transitionTable, goalStates)
		
		setUp = targetCode.GetLandmarkPolicy(gamma, convergenceTolerance)
		self.policy = setUp(transitionTable, rewardTable)
	
	def assertNumericDictAlmostEqual(self, calculatedDictionary, expectedDictionary, places=7):
    		self.assertEqual(calculatedDictionary.keys(), expectedDictionary.keys())
    		for key in calculatedDictionary.keys():
       	 		self.assertAlmostEqual(calculatedDictionary[key], expectedDictionary[key], places=places)
	
	@data(((0, 0), {(0, -1): 0.5, (-1, 0): 0.5}))
	@unpack
	def test_AtGoal(self, state, expectedResult):
		self.assertNumericDictAlmostEqual(self.policy[state], expectedResult}
	
	@data(((0, 1), {(0, -1): 1.0}),((1, 1), {(0, -1): 0.5, (-1, 0): 0.5}))
	@unpack
	def test_NotAtGoal(self, state, expectedResult):
		self.assertNumericDictAlmostEqual(self.policy[state], expectedResult}
	
	def tearDown(self):
		pass
				       
@ddt
class TestSetUpLandmark(unittest.TestCase):
	def setUp(self):
		gamma = 0.9
		convergenceTolerance = 0.00001

		stateSet = [(i,j) for i in range(2) for j in range(2)]
		landmarkLocation = {"h1": (0,0)}
		landmarkStateSet = {"h1": stateSet}
		actionSet = [(0,1), (0,-1), (1,0), (-1,0)]

		getTransitionTable = targetCode.tt.CreateTransitionTable(actionSet)

		actionCost = -1
		goalReward = 10
		getRewardTable = targetCode.rt.CreateRewardTable(actionSet, actionCost, goalReward)

		getLandmarkPolicy = targetCode.GetLandmarkPolicy(gamma, convergenceTolerance)
		merge = targetCode.merge

		setup = SetUpLandmark(landmarkLocation, landmarkStateSet, actionSet, getTransitionTable, getRewardTable, getLandmarkPolicy, merge)
		existingOptions = {}
		self.result = setup(existingOptions)			  
						  
	def assertNumericDictAlmostEqual(self, calculatedDictionary, expectedDictionary, places=7):
		self.assertEqual(calculatedDictionary.keys(), expectedDictionary.keys())
		for key in calculatedDictionary.keys():
		    self.assertAlmostEqual(calculatedDictionary[key], expectedDictionary[key], places=places)
	
	@data(('h1', (0, 0), {(0, -1): 0.5, (-1, 0): 0.5}))
	@unpack
	def test_AtLandmark(self, policy, state, expectedResult):
		self.assertNumericDictAlmostEqual(self.result[policy][state], expectedResult)
		
	@data(('h1', (0, 1), {(0, -1): 1.0}),('h1', (1, 1), {(0, -1): 0.5, (-1, 0): 0.5}))
	@unpack
	def test_NotAtLandmark(self, policy, state, expectedResult):
		self.assertNumericDictAlmostEqual(self.result[policy][state], expectedResult)
	
	def tearDown(self):
		pass
 
if __name__ == '__main__':
	unittest.main(verbosity=2)
