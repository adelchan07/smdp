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
		landmarkLocation = {"h1": (3,3), "h2": (5,2), "h3": (5,6), "h4": (9,4)}
		landmarkStateSet = {'h1': [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2), (4, 1), (4, 2), (1, 4), (1, 5), (1, 6), (1, 7), (2, 4), (2, 5), (2, 6), (2, 7), (3, 4), (3, 5), (3, 6), (3, 7), (4, 4), (4, 5), (4, 6), (4, 7), (3, 3)], 'h2': [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2), (4, 1), (4, 2), (6, 1), (6, 2), (6, 3), (7, 1), (7, 2), (7, 3), (8, 1), (8, 2), (8, 3), (9, 1), (9, 2), (9, 3), (10, 1), (10, 2), (10, 3), (11, 1), (11, 2), (11, 3), (5, 2)], 'h3': [(1, 4), (1, 5), (1, 6), (1, 7), (2, 4), (2, 5), (2, 6), (2, 7), (3, 4), (3, 5), (3, 6), (3, 7), (4, 4), (4, 5), (4, 6), (4, 7), (6, 5), (6, 6), (6, 7), (7, 5), (7, 6), (7, 7), (8, 5), (8, 6), (8, 7), (9, 5), (9, 6), (9, 7), (10, 5), (10, 6), (10, 7), (11, 5), (11, 6), (11, 7), (5, 6)], 'h4': [(6, 5), (6, 6), (6, 7), (7, 5), (7, 6), (7, 7), (8, 5), (8, 6), (8, 7), (9, 5), (9, 6), (9, 7), (10, 5), (10, 6), (10, 7), (11, 5), (11, 6), (11, 7), (6, 1), (6, 2), (6, 3), (7, 1), (7, 2), (7, 3), (8, 1), (8, 2), (8, 3), (9, 1), (9, 2), (9, 3), (10, 1), (10, 2), (10, 3), (11, 1), (11, 2), (11, 3), (9, 4)]}
		
		actionSet = [(0,1), (0,-1), (1,0), (-1,0)]
		getTransitionTable = targetCode.tt.CreateTransitionTable(actionSet)
		
		actionCost = -1
		goalReward = 10
		getRewardTable = targetCode.rt.CreateRewardTable(actionSet, actionCost, goalReward)
		
		gamma = 0.9
		convergenceTolerance = .000001
		getLandmarkPolicy = targetCode.GetLandmarkPolicy(gamma, convergenceTolerance)
		
		merge = targetCode.merge
		
		existingOptions = {}
		setUp = targetCode.SetUpLandmark(landmarkLocation, landmarkStateSet, actionSet, getTransitionTable, getRewardTable, getLandmarkPolicy, merge)
		self.landmarkPolicies = setUp(existingOptions)
	
	def assertNumericDictAlmostEqual(self, calculatedDictionary, expectedDictionary, places=7):
		self.assertEqual(calculatedDictionary.keys(), expectedDictionary.keys())
		for key in calculatedDictionary.keys():
		    self.assertAlmostEqual(calculatedDictionary[key], expectedDictionary[key], places=places)
	
	#testing landmark policies --> make sure locations surrounding location of interest AND at location of interestare correct
	@data(((3,2), (0,1)), ((3,4), (0,-1)), ((3,3), (1,0)))
	@unpack
	def test_LandmarkHallway1(self, state, expectedAction):
		self.assertEqual(self.landmarkPolicies["h1"][state], expectedAction)

	@data(((4,2), (1,0)), ((5,2), (0,1)), ((6,2), (-1,0)))
	@unpack
	def test_LandmarkHallway2(self, state, expectedAction):
		self.assertEqual(self.landmarkPolicies["h2"][state], expectedAction)

	@data(((4,6), (1,0)), ((5,6), (0,1)), ((6,6), (-1,0)))
	@unpack
	def test_LandmarkHallway3(self, state, expectedAction):
		self.assertEqual(self.landmarkPolicies["h3"][state], expectedAction)

	@data(((9,3), (0,1)), ((9,4), (1,0)), ((9,5), (0,-1)))
	@unpack
	def test_LandmarkHallway4(self, state, expectedAction):
		self.assertEqual(self.landmarkPolicies["h4"][state], expectedAction)

	#testing boundary locations don't go off the specified grid
	@data(("h1", (3,1), (0,1)), ("h2", (6,1), (0,1)), ("h3", (4,7), (0,-1)), ("h4", (10,7), (0,-1)))
	@unpack
	def testLandmarkBoundaries(self, policy, state, expectedAction):
		self.assertEqual(self.landmarkPolicies[policy][state], expectedAction)

	def tearDown(self):
		pass
 
if __name__ == '__main__':
	unittest.main(verbosity=2)
