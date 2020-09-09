"""
Created on Wed Sep 3 12:03:38 2020

@author: adelphachan

testTransition.py

testing for a deterministic transition table
"""

import sys
sys.path.append('../executive/')

import numpy as np
import unittest
from ddt import ddt, data, unpack
import transitionFunction as targetCode 

@ddt
class TestGetNextState(unittest.TestCase):
	def setUp(self):
		self.stateSet = [(i,j) for i in range(2) for j in range(2)]
		self.getNextState = targetCode.getNextState

	@data(((0,0), (-1,0), (0,0)), ((1,1), (0,1), (1,1)), ((1,0), (0,-1), (1,0)))
	@unpack
	def test_BoundaryLocations(self, state, action, expectedNextState):
		self.assertEqual(self.getNextState(state, action, self.stateSet), expectedNextState)

	@data(((0,0), (1,0), (1,0)), ((1,1), (-1,0), (0,1)), ((0,1), (0,-1), (0,0)))
	@unpack
	def test_InnerLocations(self, state, action, expectedNextState):
		self.assertEqual(self.getNextState(state, action, self.stateSet), expectedNextState)

	def tearDown(self):
		pass

@ddt
class TestPrimitiveSPrime(unittest.TestCase):
	def setUp(self):
		primitivePolices = {'up': {(0, 0): (0, 1), (0, 1): (0, 1), (1, 0): (0, 1), (1, 1): (0, 1)}, 'down': {(0, 0): (0, -1), (0, 1): (0, -1), (1, 0): (0, -1), (1, 1): (0, -1)}, 'left': {(0, 0): (-1, 0), (0, 1): (-1, 0), (1, 0): (-1, 0), (1, 1): (-1, 0)}, 'right': {(0, 0): (1, 0), (0, 1): (1, 0), (1, 0): (1, 0), (1, 1): (1, 0)}}
		stateSet = [(i,j) for i in range(2) for j in range(2)]
		getNextState = targetCode.getNextState

		self.getSPrime = targetCode.getPrimitiveSPrime(primitivePolicies, stateSet, getNextState)
	
	@data(((0,0), (-1,0), (0,0)), ((1,1), (0,1), (1,1)), ((1,0), (0,-1), (1,0)))
	@unpack
	def test_Boundary(self, state, option, expectedSPrime):
		self.assertEqual(self.getSPrime(state, option), expectedSPrime)
	
	@data(((0,0), (1,0), (1,0)), ((1,1), (-1,0), (0,1)), ((0,1), (0,-1), (0,0)))
	@unpack
	def testInner(self, state, option, expectedSPrime):
		self.assertEqual(self.getSPrime(state, option), expectedSPrime)
	
	def tearDown(self):
		pass
		
@ddt
class TestLandmarkSPrime(unittest.TestCase):
	
@ddt
class TestTransitionFunction(unittest.TestCase):
	
	@data()
	@unpack
	def test_ValidSPrime(self, state, option, sPrime, expectedProbability):
		self.assertEqual(self.transitionFunction(state, option, sPrime), expectedProbability)
	
	@data()
	@unpack
	def test_InvalidSPrime(self, state, option, sPrime, expectedProbability):
		self.assertEqual(self.transitionFunction(state, option, sPrime), expectedProbability)

if __name__ == '__main__':
	unittest.main(verbosity=2)
