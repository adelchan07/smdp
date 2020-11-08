"""
Created on Mon Aug 17 18:04:03 2020
@author: adelphachan
testPrimitiveOptionSetUp.py

test on 10x8 grid with outer edge and inner boundaries
primitive actions = {"up": (0,1), "down": (0,-1), "left": (-1,0), "right": (1,0)}
testing merge function and setUpPrimitive class
"""

import sys
sys.path.append('../src/optionSetUp')

import numpy as np
import unittest
from ddt import ddt, data, unpack
import primitiveOptionSetUp as targetCode 

@ddt
class TestMergeFunction(unittest.TestCase):
	def setUp(self):
		self.dictionary1 = {'a': 1}
		self.dictionary2 = {'b': 2, 'c': 3}

		self.result = targetCode.merge(self.dictionary1, self.dictionary2)

	#test that the merge function works correctly
	@data(('a', 1), ('b', 2), ('c', 3))
	@unpack
	def test_Merge(self, key, expectedValue):
		self.assertEqual(self.result[key], expectedValue)
	"""
	@data((3))
	@unpack
	def test_MergeDictContents(self, expectedLength):
		self.assertEqual(len(list(self.result.keys())), expectedLength)
		self.assertEqual(len(list(self.result.values())), expectedLength)
	"""

	def tearDown(self):
		pass

@ddt
class TestPrimitiveOptions(unittest.TestCase):
	def setUp(self): 

		#10x8 grid
		#blockList = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (1, 3), (2, 3), (3, 3), (5, 1), (5, 2), (5, 5), (5, 6), (7, 4), (8, 4)]
		stateSet = [(1, 1), (1, 2), (1, 4), (1, 5), (1, 6), (2, 1), (2, 2), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (5, 3), (5, 4), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (7, 1), (7, 2), (7, 3), (7, 5), (7, 6), (8, 1), (8, 2), (8, 3), (8, 5), (8, 6)]
		primitiveOptions = {"up": (0,1), "down": (0,-1), "left": (-1,0), "right": (1,0)}
		merge = targetCode.merge

		#start with no other existing options for more clarity in testing
		existingOptions = {} 

		setUp = targetCode.SetUpPrimitive(stateSet, primitiveOptions, merge)
		self.primitive = setUp(existingOptions)

	#test case examples for each primitive option; up/down/left/right
	@data(("up", (2,6), (0,1)), ("left", (1,5), (-1,0)), ("down", (2,1), (0,-1)), ("right", (8,1), (1,0)))
	@unpack
	def test_OuterBoundary(self, policy, state, expectedAction):
		self.assertEqual(self.primitive[policy][state], expectedAction)

	@data(("up", (2,2), (0,1)), ("down", (3,4), (0,-1)), ("right", (4,6), (1,0)), ("left", (6,2), (-1,0)))
	@unpack
	def test_InnerHallways(self, policy, state, expectedAction):
		self.assertEqual(self.primitive[policy][state], expectedAction)

	@data(("up", (7,2), (0,1)), ("down", (7,6), (0,-1)), ("left", (2,4), (-1,0)), ("right", (3,2), (1,0)))
	@unpack
	def test_InnerGrid(self, policy, state, expectedAction):
		self.assertEqual(self.primitive[policy][state], expectedAction)

	def tearDown(self):
		pass

if __name__ == '__main__':
	unittest.main(verbosity=2)
