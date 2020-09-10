import sys
sys.path.append('..') 

import numpy as np
import unittest
from ddt import ddt, data, unpack
import valueIteration as targetCode 

@ddt
class TestSimpleValueIteration(unittest.TestCase):
  def setUp(self):
    primitiveOptions = {'up': (0,1), 'down': (0,-1), 'right': (1,0), 'left': (-1,0)}
    stateSet = [(i,j) for i in range(2) for j in range(2)]
    getNextState = targetCode.tf.getNextState
    primitiveSPrime = targetCode.tf.GetPrimitiveSPrime(primitiveOptions, stateSet, getNextState)

    optionTerminations = {"LL": (0,0), "UL": (0,1), "LR": (1,0), "UR": (1,1)}
    landmarkSPrime = targetCode.tf.GetLandmarkSPrime(optionTerminations)

    optionSPrime = {'up': primitiveSPrime, 'down':primitiveSPrime, 'left': primitiveSPrime, 'right': primitiveSPrime,'LL': landmarkSPrime, 'UL': landmarkSPrime, 'LR': landmarkSPrime, 'UR': landmarkSPrime} 

    transition = targetCode.tf.TransitionFunction(optionSPrime)

    actionCost = -1
    moveCost = -3
    goalStates = [(0,0)]
    goalReward = 10
    landmarkPolicies = {'LL': {(0, 0): (0, -1), (0, 1): (0, -1), (1, 0): (-1, 0), (1, 1): (0, -1)}, 'UL': {(0, 0): (0, 1), (0, 1): (0, 1), (1, 0): (0, 1), (1, 1): (-1, 0)}, 'LR': {(0, 0): (1, 0), (0, 1): (1, 0), (1, 0): (0, -1), (1, 1): (0, -1)}, 'UR': {(0, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, 1), (1, 1): (0, 1)}}
    primitiveReward = targetCode.rf.GetPrimitiveOptionReward(actionCost, moveCost, goalStates, goalReward, primitiveSPrime)
    landmarkReward = targetCode.rf.GetLandmarkOptionReward(actionCost, moveCost, goalStates, goalReward, landmarkPolicies, landmarkSPrime, getNextState)

    optionReward = {'up': primitiveReward, 'down': primitiveReward, 'left': primitiveReward, 'right': primitiveReward, 'LL':landmarkReward, 'UL': landmarkReward, 'UR': landmarkReward, 'LR': landmarkReward} 
    reward = targetCode.rf.RewardFunction(optionReward)

    optionSpace = {(0, 0): ['LL', 'UL', 'LR', 'UR', 'up', 'down', 'left', 'right'], (0, 1): ['LL', 'UL', 'LR', 'UR', 'up', 'down', 'left', 'right'], (1, 0): ['LL', 'UL', 'LR', 'UR', 'up', 'down', 'left', 'right'], (1, 1): ['LL', 'UL', 'LR', 'UR', 'up', 'down', 'left', 'right']}
    optionSpace = targetCode.osf.OptionSpaceFunction(optionSpace)

    V = {s:0 for s in stateSet}
    gamma = 0.9
    convergence = 0.0001

    setUp = targetCode.GetPolicy(stateSet, optionSpace, transition, reward, gamma, V, convergence)
    self.policy = {s:setUp(s) for s in stateSet}

  def assertNumericDictAlmostEqual(self, calculatedDictionary, expectedDictionary, places=7):
    self.assertEqual(calculatedDictionary.keys(), expectedDictionary.keys())
    for key in calculatedDictionary.keys():
        self.assertAlmostEqual(calculatedDictionary[key], expectedDictionary[key], places=places)
	
  @data(((0,0), {'LL': 1.0}))
  @unpack
  def test_AtGoal(self, state, expectedResult):
    self.assertNumericDictAlmostEqual(self.policy[state], expectedResult)
  
  @data(((1,1), {'LL': 1.0}), ((0,1), {'LL': 0.5, 'down': 0.5}), ((1, 0), {'LL': 0.5, 'left': 0.5}))
  @unpack
  def test_OutsideGoal(self, state, expectedResult):
    self.assertNumericDictAlmostEqual(self.policy[state], expectedResult)

  def tearDown(self):
    pass
  
if __name__ == '__main__':
	unittest.main(verbosity=2)

