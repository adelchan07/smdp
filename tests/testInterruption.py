import sys
sys.path.append('../src/')

import numpy as np
import unittest
from ddt import ddt, data, unpack
import interruptedOptions as targetCode

@ddt
class testCheckCondition(unittest.TestCase):
    def setUp(self):

        class optionSpaceFuction(object):
            def__init__(self, optionSpace):
                self.optionSpace = optionSpace #no optionType bc only landmark options relevant/ exist in optionSpace

            def __call__(self, state):
                optionSet = self.optionSpace[state]
                return optionSet
        
        optionSpace = {"A": [(i,j) for i in range(3) for j in range(3)], "B": [(i,j) for i in range(1) for j in range(3)]}
        
        optionSpaceFunction = optionSpaceFunction(optionSpace, optionType)
        self.CheckCondition = targetCode.CheckCondition(optionSpaceFuction)

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
