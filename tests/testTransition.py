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
	
	@data(((0,0), 'left', (0,0)), ((1,1), 'up, (1,1)), ((1,0), 'down', (1,0)))
	@unpack
	def test_Boundary(self, state, option, expectedSPrime):
		self.assertEqual(self.getSPrime(state, option), expectedSPrime)
	
	@data(((0,0), 'right', (1,0)), ((1,1), 'left', (0,1)), ((0,1), 'down', (0,0)))
	@unpack
	def test_Inner(self, state, option, expectedSPrime):
		self.assertEqual(self.getSPrime(state, option), expectedSPrime)
	
	def tearDown(self):
		pass
		
@ddt
class TestLandmarkSPrime(unittest.TestCase):
	optionTerminations = {"LL": (0,0), "UL": (0,1), "LR": (1,0), "UR": (1,1)}
	self.getSPrime = targetCode.getLandmarkSPrime(optionTerminations)
	
	@data(((0,0), "LL", (0,0)), ((0,1), "UL", (0,1)), ((1,0), "LR", (1,0)), ((1,1), "UR", (1,1)))
	@unpack
	def test_AtLandmark(self, state, option, expectedSPrime):
		self.assertEqual(self.getSPrime(state, option), expectedSPrime)
		
	@data(((1,1), "LL", (0,0)), ((0,0), "UL", (0,1)), ((0,0), "LR", (1,0)), ((1,0), "UR", (1,1)))
	@unpack
	def test_NeedToMove(self, state, option, expectedSPrime):
	
	def tearDown(self):
		pass
	
	
@ddt
class TestTransitionFunction(unittest.TestCase):
	
	@data(((1,1), "LL", (1,0)), ((1,1), "up", (0,0)), ((0,0), "right", (1,1)))
	@unpack
	def test_InvalidSPrime(self, state, option, sPrime):
		self.assertEqual(self.transitionFunction(state, option, sPrime), 0)
	
	@data(((1,1), "LL", (0,0)), ((1,1), "up", (1,1)), ((1,0), "left", (0,0)))
	@unpack
	def test_ValidSPrime(self, state, option, sPrime):
		self.assertEqual(self.transitionFunction(state, option, sPrime), 1)

if __name__ == '__main__':
	unittest.main(verbosity=2)
