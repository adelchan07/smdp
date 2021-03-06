import sys

sys.path.append('../exec/original/')
import transitionFunction as tf

sys.path.append('../exec/interrupted/')

import numpy as np
import unittest
from ddt import ddt, data, unpack
import normalPath as targetCode 

@ddt
class TestNormalPath(unittest.TestCase):

	def setUp(self):
	    landmarkPolicies = {'l':{(0,0): {(1,0):1.0}, (1,0): {(0,1):1.0}, (0,1): {(1,0):1.0}, (1,1): {(0,1):1.0}}}
	    interruptionPolicy = {(0,0): {'l':1.0}, (1,0): {'l':1.0}, (0,1): {'l':1.0}, (1,1): {'l':1.0}}
	    optionTerminations = {'l': (1,1)}
	    getNextState = tf.getNextState
	    goalStates = [(1,1)]
	    stateSet = [(i,j) for i in range(2) for j in range(2)]

	    self.setUp = targetCode.GetNormalPath(landmarkPolicies, interruptionPolicy, optionTerminations, getNextState, goalStates, stateSet)
	
	def assertNumericDictAlmostEqual(self, calculatedDictionary, expectedDictionary, places=7):
    		self.assertEqual(calculatedDictionary.keys(), expectedDictionary.keys())
    		for key in calculatedDictionary.keys():
       	 		self.assertAlmostEqual(calculatedDictionary[key], expectedDictionary[key], places=places)
	
	@data(((1,1), 'l', (1,1), {}), ((0,0), 'l', (1,1), {(0,0): (1,0), (1,0): (0,1)}))
	@unpack
	def test_GetPath(self, state, currentOption, termination, expectedPath):
   		currentState, path = self.setUp.getPath(state, currentOption, termination, {})
   		self.assertNumericDictAlmostEqual(path, expectedPath)
		
	def tearDown(self):
		pass
	
if __name__ == '__main__':
	unittest.main(verbosity=2)
