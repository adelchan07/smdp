"""
Created on Wed Sep 3 12:03:38 2020

@author: adelphachan

testTransition.py

testing for a deterministic transition table
"""

import sys
sys.path.append('../exec/original/')

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
		primitivePolicies = {'up': (0,1), 'down': (0,-1), 'right': (1,0), 'left': (-1,0)}
		stateSet = [(i,j) for i in range(2) for j in range(2)]
		getNextState = targetCode.getNextState

		self.getSPrime = targetCode.GetPrimitiveSPrime(primitivePolicies, stateSet, getNextState)
	
	@data(((0,0), 'left', (0,0)), ((1,1), 'up', (1,1)), ((1,0), 'down', (1,0)))
	@unpack
	def test_Boundary(self, state, option, sPrime):
		self.assertEqual(self.getSPrime(state, option, sPrime), 1)
	
	@data(((0,0), 'right', (1,0)), ((1,1), 'left', (0,1)), ((0,1), 'down', (0,0)))
	@unpack
	def test_Inner(self, state, option, sPrime):
		self.assertEqual(self.getSPrime(state, option, sPrime), 1)
	
	@data(((0,0), 'left', (1,0)), ((1,1), 'up', (0,1)), ((1,0), 'down', (1,1)))
	@unpack
	def test_WrongSPrime(self, state, option, sPrime):
		self.assertEqual(self.getSPrime(state, option, sPrime), 0)
	
	def tearDown(self):
		pass
		
@ddt
class TestLandmarkSPrime(unittest.TestCase):
	def setUp(self):
		optionTerminations = {"LL": (0,0), "UL": (0,1), "LR": (1,0), "UR": (1,1)}
		self.getSPrime = targetCode.GetLandmarkSPrime(optionTerminations)
	
	@data(((0,0), "LL", (0,0)), ((0,1), "UL", (0,1)), ((1,0), "LR", (1,0)), ((1,1), "UR", (1,1)))
	@unpack
	def test_AtLandmark(self, state, option, sPrime):
		self.assertEqual(self.getSPrime(state, option, sPrime), 1)
		
	@data(((1,1), "LL", (0,0)), ((0,0), "UL", (0,1)), ((0,0), "LR", (1,0)), ((1,0), "UR", (1,1)))
	@unpack
	def test_NeedToMove(self, state, option, sPrime):
		self.assertEqual(self.getSPrime(state, option, sPrime), 1)
	
	@data(((0,0), "LL", (1,0)), ((0,1), "UL", (1,1)), ((1,0), "LR", (1,1)), ((1,1), "UR", (1,0)))
	@unpack
	def test_WrongSPrime(self, state, option, sPrime):
		self.assertEqual(self.getSPrime(state, option, sPrime), 0)
	
	def tearDown(self):
		pass
	
	
@ddt
class TestTransitionFunction(unittest.TestCase):
	def setUp(self):
		primitivePolicies = {'up': (0,1), 'down': (0,-1), 'right': (1,0), 'left': (-1,0)}
		stateSet = [(i,j) for i in range(2) for j in range(2)]
		getNextState = targetCode.getNextState
		primitiveSPrime = targetCode.GetPrimitiveSPrime(primitivePolicies, stateSet, getNextState)
		
		optionTerminations = {"LL": (0,0), "UL": (0,1), "LR": (1,0), "UR": (1,1)}
		landmarkSPrime = targetCode.GetLandmarkSPrime(optionTerminations)
		
		optionSPrime = {'up': primitiveSPrime, 'down':primitiveSPrime, 'left': primitiveSPrime, 'right': primitiveSPrime,'LL': landmarkSPrime, 'UL': landmarkSPrime, 'LR': landmarkSPrime, 'UR': landmarkSPrime} 
		
		self.transitionFunction = targetCode.TransitionFunction(optionSPrime)
	
	@data(((1,1), "LL", (1,0)), ((1,1), "up", (0,0)), ((0,0), "right", (1,1)))
	@unpack
	def test_InvalidSPrime(self, state, option, sPrime):
		self.assertEqual(self.transitionFunction(state, option, sPrime), 0)
	
	@data(((1,1), "LL", (0,0)), ((1,1), "up", (1,1)), ((1,0), "left", (0,0)))
	@unpack
	def test_ValidSPrime(self, state, option, sPrime):
		self.assertEqual(self.transitionFunction(state, option, sPrime), 1)
	
	def tearDown(self):
		pass

if __name__ == '__main__':
	unittest.main(verbosity=2)
