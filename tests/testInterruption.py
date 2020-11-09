import sys
sys.path.append('../src/')

import numpy as np
import unittest
from ddt import ddt, data, unpack
import interruptedOptions as targetCode

@ddt
class testCheckCondition(unittest.TestCase):
    def setUp(self):
		
        stateSet = [(i,j) for i in range(3) for j in range(3)]
        optionStateSet = {"A": [(i,j) for i in range(3) for j in range(3)], "B": [(i,j) for i in range(1) for j in range(3)]}
        optionSpace = {(0, 0): ['A', 'B'], (0, 1): ['A', 'B'], (0, 2): ['A', 'B'], (1, 0): ['A'], (1, 1): ['A'], (1, 2): ['A'], (2, 0): ['A'], (2, 1): ['A'], (2, 2): ['A']}

        optionSpaceFunction = lambda x: optionSpace[x]
        self.CheckCondition = targetCode.CheckCondition(optionSpaceFunction)

    @data(((2,0), (2,1)), ((0,0), (0,1)))
    @unpack
    def test_NoNewOptions(self, state, sPrime):
        self.assertEqual(self.CheckCondition(state, sPrime), False)
    
    @data(((1,0), (0,0)), ((0,1), (1,1)))
    @unpack
    def test_YesNewOptions(self, state, sPrime):
        self.assertEqual(self.CheckCondition(state, sPrime), True)
    
    @data(((1,2), (1,2)), ((0,1), (0,1))) #boundary = bounce back = same state = same optionSet
    @unpack
    def test_BoundaryOptions(self, state, sPrime):
        self.assertEqual(self.CheckCondition(state, sPrime), False)

    def tearDown(self):
        pass

if __name__ == '__main__':
	unittest.main(verbosity=2)
