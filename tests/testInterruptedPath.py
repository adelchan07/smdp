import sys
sys.path.append('../exec/interrupted/')

import numpy as np
import unittest
from ddt import ddt, data, unpack
import interruptedPath as targetCode 

@ddt
class TestInterruptedPath(unittest.TestCase):

	def setUp(self):
	    
	    checkCondition = targetCode.io.checkCondition
	    landmarkPolicies = {'l': {(0,0): (1,0), (1,0): (0,1), (0,1): (1,0), (1,1): (0,1)}, 'b': {(0,0): (1,0), (1,0): (1,0), (0,1): (1,0), (1,1): (-1,0)}}
	    interruptionPolicy = {(0,0): 'b', (1,0): 'b', (0,1): 'l', (1,1): 'l'}
	    optionTerminations = {'l': (1,1)}
	    getNextState = targetCode.tf.getNextState
	    goalStates = [(1,1)]
	    stateSet = [(i,j) for i in range(2) for j in range(2)]

	    self.setUp = targetCode.GetInterruptedPath(checkCondition, landmarkPolicies, interruptionPolicy, optionTerminations, getNextState, goalStates, stateSet)
	
	def assertNumericDictAlmostEqual(self, calculatedDictionary, expectedDictionary, places=7):
    		self.assertEqual(calculatedDictionary.keys(), expectedDictionary.keys())
    		for key in calculatedDictionary.keys():
       	 		self.assertAlmostEqual(calculatedDictionary[key], expectedDictionary[key], places=places)
	
	@data(((1,1), 'l', (1,1), {}), ((0,0), {(0,0): (1,0), (1,0): (0,1)}))
	@unpack
	def test_GetPath00(self, state, currentOption, termination, expectedPath):
   		currentState, path = self.setUp.getPath(state, currentOption, termination, {})
   		self.assertNumericDictAlmostEqual(path, expectedPath)

   	def tearDown(self):
   		pass

if __name__ == '__main__':
	unittest.main(verbosity=2)
