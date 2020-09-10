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
		convergenceTolerance = .000001
		
		transitionTable = {(0, 0): {(0, 1): {(0, 1): 1}, (0, -1): {(0, 0): 1}, (1, 0): {(1, 0): 1}, (-1, 0): {(0, 0): 1}}, (0, 1): {(0, 1): {(0, 1): 1}, (0, -1): {(0, 0): 1}, (1, 0): {(1, 1): 1}, (-1, 0): {(0, 1): 1}}, (1, 0): {(0, 1): {(1, 1): 1}, (0, -1): {(1, 0): 1}, (1, 0): {(1, 0): 1}, (-1, 0): {(0, 0): 1}}, (1, 1): {(0, 1): {(1, 1): 1}, (0, -1): {(1, 0): 1}, (1, 0): {(1, 1): 1}, (-1, 0): {(0, 1): 1}}}
		
		#LL = (0,0), UR = (1,1)
		rewardTableLL =  {(0, 0): {(0, 1): {(0, 1): -1}, (0, -1): {(0, 0): 10}, (1, 0): {(1, 0): -1}, (-1, 0): {(0, 0): 10}}, (0, 1): {(0, 1): {(0, 1): -1}, (0, -1): {(0, 0): 10}, (1, 0): {(1, 1): -1}, (-1, 0): {(0, 1): -1}}, (1, 0): {(0, 1): {(1, 1): -1}, (0, -1): {(1, 0): -1}, (1, 0): {(1, 0): -1}, (-1, 0): {(0, 0): 10}}, (1, 1): {(0, 1): {(1, 1): -1}, (0, -1): {(1, 0): -1}, (1, 0): {(1, 1): -1}, (-1, 0): {(0, 1): -1}}}
		rewardTableUR = {(0, 0): {(0, 1): {(0, 1): -1}, (0, -1): {(0, 0): -1}, (1, 0): {(1, 0): -1}, (-1, 0): {(0, 0): -1}}, (0, 1): {(0, 1): {(0, 1): -1}, (0, -1): {(0, 0): -1}, (1, 0): {(1, 1): 10}, (-1, 0): {(0, 1): -1}}, (1, 0): {(0, 1): {(1, 1): 10}, (0, -1): {(1, 0): -1}, (1, 0): {(1, 0): -1}, (-1, 0): {(0, 0): -1}}, (1, 1): {(0, 1): {(1, 1): 10}, (0, -1): {(1, 0): -1}, (1, 0): {(1, 1): 10}, (-1, 0): {(0, 1): -1}}}
		
		setUp = targetCode.GetLandmarkPolicy(gamma, convergenceTolerance)
		self.policyLL = setUp(transitionTable, rewardTableLL)
		self.policyUR = setUp(transitionTable, rewardTableUR)
	
	def assertNumericDictAlmostEqual(self, calculatedDictionary, expectedDictionary, places=7):
		self.assertEqual(calculatedDictionary.keys(), expectedDictionary.keys())
		for key in calculatedDictionary.keys():
		    self.assertAlmostEqual(calculatedDictionary[key], expectedDictionary[key], places=places)
	
	@data(((0,0), {(0, -1): 0.5, (-1, 0): 0.5}), ((1,1), {(0, -1): 0.5, (-1, 0): 0.5}), ((1,0), {(0, -1): 1.0}))
	@unpack
	def test_LandmarkRewardLL(self, state, expectedResult):
		self.assertNumericDictAlmostEqual(self.policyLL[state], expectedResult)

	@data(((0,0), {(0, 1): 0.5, (1, 0): 0.5}), ((1,1), {(0, 1): 0.5, (1, 0): 0.5}), ((1,0), {(1, 1): 1.0}))
	@unpack
	def test_LandmarkRewardUR(self, state, expectedResult):
		self.assertNumericDictAlmostEqual(self.policyUR[state], expectedResult)

	def tearDown(self):
		pass
	
@ddt
class TestSetUpLandmark(unittest.TestCase):
	def setUp(self):
		landmarkLocation = {"hall": (1,1)}
		landmarkStateSet = {"hall":[(0, 0), (0, 1), (0, 2), (1, 1), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2)]}

		actionSet = [(0,1), (0,-1), (1,0), (-1,0)]
		getTransitionTable = targetCode.tt.CreateTransitionTable(actionSet)

		actionCost = -1
		goalReward = 10
		getRewardTable = targetCode.rt.CreateRewardTable(actionSet, actionCost, goalReward)

		gamma = 0.9
		convergenceTolerance = 0.00001
		getLandmarkPolicy = targetCode.GetLandmarkPolicy(gamma, convergenceTolerance)

		merge = targetCode.merge

		existingOptions = {}
		setUp = targetCode.SetUpLandmark(landmarkLocation, landmarkStateSet, actionSet, getTransitionTable, getRewardTable, getLandmarkPolicy, merge)
		self.policies = setUp(existingOptions)
	
	def assertNumericDictAlmostEqual(self, calculatedDictionary, expectedDictionary, places=7):
		self.assertEqual(calculatedDictionary.keys(), expectedDictionary.keys())
		for key in calculatedDictionary.keys():
		    self.assertAlmostEqual(calculatedDictionary[key], expectedDictionary[key], places=places)
	
	@data(((1,1), {(0,1): 0.5, (0,-1): 0,5}))
	@unpack
	def test_AtLandmark(self, state, expectedResult):
		self.assertNumericDictAlmostEqual(self.policies[state], expectedResult)
		
	@data(((3,0), {(-1,0): 0.5, (0,1): 0,5}), ((3,2), {(-1,0): 0.5, (0,-1): 0,5}))
	@unpack
	def test_Boundary(self, state, expectedResult):
		self.assertNumericDictAlmostEqual(self.policies[state], expectedResult)
		
	@data(((0,1), {(1,0): 1.0}), ((2,1), {(-1,0): 1.0}))
	@unpack
	def test_Inner(self, state, expectedResult):
		self.assertNumericDictAlmostEqual(self.policies[state], expectedResult)
		
	def tearDown(self):
		pass
 
if __name__ == '__main__':
	unittest.main(verbosity=2)
