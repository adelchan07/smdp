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
sys.path.append('../exec/original/optionSetUp/')

import numpy as np
import unittest
from ddt import ddt, data, unpack
import landmarkOptionSetUp as targetCode 

sys.path.append('../exec/original/')
import transitionFunction as tf
import rewardFunction as rf

@ddt
class TestGetLandmarkPolicy(unittest.TestCase):
	def setUp(self):
		gamma = 0.9
		convergenceTolerance = 0.001
		
		stateSet = [(i,j) for i in range(2) for j in range(2)]
		actionCost = -1
		moveCost = -3
		goalReward = 10
		goalStates = [(0,0)]
		
		getNextState = tf.getNextState
		primitiveOptions = {"up": (0,1), "down": (0,-1), "left": (-1,0), "right":(1,0)}
		primitiveSPrime = tf.GetPrimitiveSPrime(primitiveOptions, stateSet, getNextState)
		optionSPrime = {option: primitiveSPrime for option in primitiveOptions.keys()}
		
		transitionFunction = tf.TransitionFunction(optionSPrime)
		
		primitiveReward = rf.GetPrimitiveOptionReward(actionCost, moveCost, goalStates, goalReward, primitiveSPrime)
		optionReward = {option: primitiveReward for option in primitiveOptions.keys()}
		rewardFunction = rf.RewardFunction(optionReward)
		
		actions = list(primitiveOptions.keys())
		actionSpace = {state: actions for state in stateSet}
		actionSpaceFunction = lambda x: actionSpace[x]
		
		setUp = targetCode.GetLandmarkPolicy(gamma, convergenceTolerance) 
		self.policy = setUp(transitionFunction, rewardFunction, stateSet, actionSpaceFunction)
	
	def assertNumericDictAlmostEqual(self, calculatedDictionary, expectedDictionary, places=7):
    		self.assertEqual(calculatedDictionary.keys(), expectedDictionary.keys())
    		for key in calculatedDictionary.keys():
       	 		self.assertAlmostEqual(calculatedDictionary[key], expectedDictionary[key], places=places)
	
	@data(((0, 0), {(0, -1): 0.5, (-1, 0): 0.5}))
	@unpack
	def test_AtGoal(self, state, expectedResult):
		self.assertNumericDictAlmostEqual(self.policy[state], expectedResult)
	
	@data(((0, 1), {(0, -1): 1.0}),((1, 1), {(0, -1): 0.5, (-1, 0): 0.5}))
	@unpack
	def test_NotAtGoal(self, state, expectedResult):
		self.assertNumericDictAlmostEqual(self.policy[state], expectedResult)
	
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
		
		getNextState = targetCode.tf.getNextState
		primitiveOptions = {"up": (0,1), "down": (0,-1), "left": (-1,0), "right":(1,0)}
		primitiveSPrime = targetCode.tf.GetPrimitiveSPrime(primitiveOptions, stateSet, getNextState)
		optionSPrime = {option: primitiveSPrime for option in primitiveOptions.keys()}
		
		transitionFunction = targetCode.tf.TransitionFunction(optionSPrime)
		
		actionCost = -1
		moveCost = -3
		goalStates = [(0,0)]
		goalReward = 10
		
		primitiveReward = targetCode.rf.GetPrimitiveOptionReward(actionCost, moveCost, goalStates, goalReward, primitiveSPrime)
		optionReward = {option: primitiveReward for option in primitiveOptions.keys()}
		rewardFunction = targetCode.rf.RewardFunction(optionReward)
		
		getLandmarkPolicy = targetCode.GetLandmarkPolicy(gamma, convergenceTolerance) 		
		merge = targetCode.merge

		landmarkSetUp = targetCode.SetUpLandmark(landmarkLocation, landmarkStateSet, primitiveOptions, transitionFunction, rewardFunction, getLandmarkPolicy, merge)
		existingOptions = {}
		self.result = landmarkSetUp(existingOptions)			  
						  
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
