"""
Created on Wed Sep 3 12:03:38 2020

@author: adelphachan

testTransition.py
"""

import sys
sys.path.append('../executive/')

import numpy as np
import unittest
from ddt import ddt, data, unpack
import transition as targetCode 

@ddt
class TestTransitionFunction(unittest.TestCase):
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

if __name__ == '__main__':
	unittest.main(verbosity=2)
