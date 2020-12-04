import numpy as np
import unittest
from ddt import ddt, data, unpack

import sys
sys.path.append('../exec/original/')
import transitionFunction as tf
import rewardFunction as rf

sys.path.append('../src/')
import qLearning as targetCode

@ddt
class TestCreateQTable(unittest.TestCase):
    def setUp(self):
    
        stateSpace = [(i,j) for i in range(3) for j in range(3)]
        availableOptions = ['a', 'b']
        
        self.QTable = targetCode.createQTable(stateSpace, availableOptions)
    
    @data(((0,0), 'a'), ((0,0), 'b'), ((2,2), 'a'), ((0,2), 'b'))
    @unpack
    def test_OuterCells(self, state, option):
        self.assertEqual(self.QTable[state][option], 0)
        
    @data(((1,1), 'a'), ((1,1), 'b'))
    @unpack
    def test_InnerCells(self, state, option):
        self.assertEqual(self.QTable[state][option], 0)
        
    def tearDown(self):
        pass

@ddt
class TestGetSPrime(unittest.TestCase):
    def __init__(self):
        stateSpace = [(i,j) for i in range(2) for j in range(2)]
        
        getNextState = tf.getNextState
        primitivePolicies = {'up': (0,1), 'down': (0,-1), 'right': (1,0), 'left': (-1,0)}
        primitiveSPrime = tf.GetPrimitiveSPrime(primitivePolicies, stateSet, getNextState)
        
        optionTerminations = {"h1": (0,0)}
        landmarkSPrime = tf.GetLandmarkSPrime(optionTerminations)
        
        optionSPrime = {'up': primitiveSPrime, 'down':primitiveSPrime, 'left': primitiveSPrime, 'right': primitiveSPrime,'h1': landmarkSPrime}
        transitionFunction = tf.TransitionFunction(optionSPrime)
        
        self.getSPrime = targetCode.GetSPrime(transitionFunction, stateSpace)
    
    @data(((0,0), 'up', (0,1)), ((1,1), 'down', (0,1)), ((0,0), 'right', (0,1)))
    @unpack
    def test_Primitive(self, state, option, expectedSPrime):
        self.assertEqual(self.getSPrime(state, option), expectedSPrime)
    
    @data(((0,0), (0,0)), ((1,0), (0,0)), ((1,1), (0,0)))
    @unpack
    def test_Landmark(self, state, expectedSPrime):
        self.assertEqual(self.getSPrime(state, 'h1'), expectedSPrime)
    
    def tearDown(self):
        pass

@ddt
class TestGetOption(unittest.TestCase):
    def setUp(self):
        stateSet = [(i,j) for i in range(2) for j in range(2)]

        universal = ['up','down','left','right','h1']
        optionSpace = {state: universal for state in stateSet}
        optionSpaceFunction = lambda x: optionSpace[x]
        
        self.always_random = targetCode.GetOption(0, optionSpaceFunction)
        self.never_random = targetCode.GetOption(1, optionSpaceFunction)
        
        self.QTable = {(0, 0): {'up': 3, 'down': 0, 'left': 0, 'right': 0, 'h1': 0}, (0, 1): {'up': 0, 'down': 0, 'left': 0, 'right': 0, 'h1': 0}, (1, 0): {'up': 0, 'down': 0, 'left': 0, 'right': 3, 'h1': 0}, (1, 1): {'up': 0, 'down': 0, 'left': 3, 'right': 0, 'h1': 0}}
        self.universal = universal
    
    @data((0,0), (1,1))
    @unpack
    def test_AlwaysRandom(self, state):
        option = self.always_random(state, self.QTable)
        self.assertEqual(option in self.universal, True)
        
    @data(((0,0), "up"), ((1,0), "right"), ((1,1), "left"))
    @unpack
    def test_NeverRandom(self, state, expectedOption):
        self.assertEqual(self.never_random(state, self.QTable), expectedOption)
        
    
    def tearDown(self):
        pass

@ddt
class TestGetQValue(unittest.TestCase):
    def setUp(self):
        alpha = 1
        gamma = 1
        
        self.reward = 0
        self.QTable = {(0, 0): {'up': 3, 'down': 0, 'left': 0, 'right': 0, 'h1': 0}, (0, 1): {'up': 0, 'down': 0, 'left': 0, 'right': 0, 'h1': 0}, (1, 0): {'up': 0, 'down': 0, 'left': 0, 'right': 3, 'h1': 0}, (1, 1): {'up': 0, 'down': 0, 'left': 3, 'right': 0, 'h1': 0}}
        
        self.getQVal = targetCode.GetQValue(alpha, gamma)
    
    @data(((0,0), 'up', (0,1), 0), ((0,0), 'right', (1,0), 3))
    @unpack
    def test_QVal(self, state, option, sPrime, expectedReward):
        self.assertEqual(self.getQVal(state, option, sPrime, self.reward, self.QTable), expectedReward)
        
    def tearDown(self):
        pass


@ddt
class TestGetPolicy(unittest.TestCase):
    def.setUp(self):
        QTable ={(0, 0): {'up': 3, 'down': 0, 'left': 0, 'right': 0, 'h1': 0}, (0, 1): {'up': 0, 'down': 3, 'left': 0, 'right': 0, 'h1': 0}, (1, 0): {'up': 0, 'down': 0, 'left': 3, 'right': 0, 'h1': 0}, (1, 1): {'up': 0, 'down': 0, 'left': 0, 'right': 3, 'h1': 0}}
        
        roundingTolerance = 0.0001
        
        stateSet = [(i,j) for i in range(2) for j in range(2)]

        universal = ['up','down','left','right','h1']
        optionSpace = {state: universal for state in stateSet}
        optionSpaceFunction = lambda x: optionSpace[x]
        
        getPolicy = targetCode.GetPolicy(roundingTolerance, optionSpaceFunction)
        self.policy = getPolicy(QTable)
        
    def assertNumericDictAlmostEqual(self, calculatedDictionary, expectedDictionary, places=7):
        self.assertEqual(calculatedDictionary.keys(), expectedDictionary.keys())
        for key in calculatedDictionary.keys():
            self.assertAlmostEqual(calculatedDictionary[key], expectedDictionary[key], places=places)
    
    @data(((0,0), {'up':1.0}), ((0,1), {'down':1.0}), ((1,0), {'left':1.0}), ((1,1), {'right':1.0}))
    @unpack
    def test_Policy(self, state, expectedResult):
        self.assertNumericDictAlmostEqual(self.policy[state], expectedResult)
    
    def tearDown(self):
        pass
 
