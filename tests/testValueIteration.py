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
    getNextState = tt.getNextState
    primitiveSPrime = tt.getPrimitiveSPrime(primitiveOptions, stateSet, getNextState)

    optionTerminations = {"LL": (0,0), "UL": (0,1), "LR": (1,0), "UR": (1,1)}
    landmarkSPrime = tt.getLandmarkSPrime(optionTerminations)

    optionSPrime = {'up': primitiveSPrime, 'down':primitiveSPrime, 'left': primitiveSPrime, 'right': primitiveSPrime,'LL': landmarkSPrime, 'UL': landmarkSPrime, 'LR': landmarkSPrime, 'UR': landmarkSPrime} 

    transition = tt.transitionFunction(optionSPrime)

    actionCost = -1
    moveCost = -3
    goalStates = [(0,0)]
    goalReward = 10
    landmarkPolicies = {'LL': {(0, 0): (0, -1), (0, 1): (0, -1), (1, 0): (-1, 0), (1, 1): (0, -1)}, 'UL': {(0, 0): (0, 1), (0, 1): (0, 1), (1, 0): (0, 1), (1, 1): (-1, 0)}, 'LR': {(0, 0): (1, 0), (0, 1): (1, 0), (1, 0): (0, -1), (1, 1): (0, -1)}, 'UR': {(0, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, 1), (1, 1): (0, 1)}}
    primitiveReward = rr.getPrimitiveOptionReward(actionCost, moveCost, goalStates, goalReward, primitivePolicies, primitiveSPrime)
    landmarkReward = rr.getLandmarkOptionReward(actionCost, moveCost, goalStates, goalReward, landmarkPolicies, landmarkSPrime, getNextState)

    optionReward = {'up': primitiveReward, 'down': primitiveReward, 'left': primitiveReward, 'right': primitiveReward, 'LL':landmarkReward, 'UL': landmarkReward, 'UR': landmarkReward, 'LR': landmarkReward} 
    reward = rr.rewardFunction(optionReward)

    optionSpace = {(0, 0): ['LL', 'UL', 'LR', 'UR', 'up', 'down', 'left', 'right'], (0, 1): ['LL', 'UL', 'LR', 'UR', 'up', 'down', 'left', 'right'], (1, 0): ['LL', 'UL', 'LR', 'UR', 'up', 'down', 'left', 'right'], (1, 1): ['LL', 'UL', 'LR', 'UR', 'up', 'down', 'left', 'right']}
    optionSpace = os.optionSpaceFunction(optionSpace)

    V = {s:0 for s in stateSet}
    gamma = 0.9
    convergence = 0.0001

    setUp = GetPolicy(stateSet, optionSpace, transition, reward, gamma, V, convergence)
    policy = {s:setUp(s) for s in stateSet}
