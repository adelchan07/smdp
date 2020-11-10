"""
Created on Sun Oct 11 13:03:57 2020
@author: adelphachan
interruptedMain.py
interrupted options with 5x10 grid
change in trajectory from L to S to better get to R
only using landmark options to better illustrate interruption
*note: goal state IS R so there is a way for a single landmark option to be interrupted to go to the goal in one "shot"
"""
import numpy as np

from normalPath import GetNormalPath
from interruptedPath import GetInterruptedPath

import sys
sys.path.append('../original/')
import transitionFunction as tf
import rewardFunction as rf

sys.path.append('../../src/')
import valueIteration as vi
import interruptedOptions as io

stateSet = [(i,j) for i in range(5) for j in range(10)]

getNextState = tf.getNextState
primitivePolicies = {'up': (0,1), 'down':(0,-1), 'left': (-1,0), 'right': (1,0), 'ul': (-1,1), 'ur': (1,1), 'll': (-1,-1), 'lr': (1,-1)}
primitiveSPrime = tf.GetPrimitiveSPrime(primitivePolicies, stateSet, getNextState)
		
optionTerminations = {'L': (4,9), 'R': (0,9)}
landmarkSPrime = tf.GetLandmarkSPrime(optionTerminations)

optionSPrime = {'S': landmarkSPrime, 'L': landmarkSPrime, 'R': landmarkSPrime}
transitionFunction = tf.TransitionFunction(optionSPrime)

actionCost = -1
moveCost = -3
goalStates = [(0,9)]
goalReward = 10
primitiveReward = rf.GetPrimitiveOptionReward(actionCost, moveCost, goalStates, goalReward, primitiveSPrime)

landmarkPolicies = {'L': {(0, 0): {(0, 1): 0.5, (1, 1): 0.5}, (0, 1): {(0, 1): 0.5, (1, 1): 0.5}, (0, 2): {(0, 1): 0.5, (1, 1): 0.5}, (0, 3): {(0, 1): 0.5, (1, 1): 0.5}, (0, 4): {(0, 1): 0.5, (1, 1): 0.5}, (0, 5): {(1, 1): 1.0}, (0, 6): {(1, 0): 0.5, (1, 1): 0.5}, (0, 7): {(1, 0): 0.3333333333333333, (1, 1): 0.3333333333333333, (1, -1): 0.3333333333333333}, (0, 8): {(1, 0): 0.3333333333333333, (1, 1): 0.3333333333333333, (1, -1): 0.3333333333333333}, (0, 9): {(1, 0): 0.5, (1, -1): 0.5}, (1, 0): {(0, 1): 0.3333333333333333, (1, 1): 0.3333333333333333, (-1, 1): 0.3333333333333333}, (1, 1): {(0, 1): 0.3333333333333333, (1, 1): 0.3333333333333333, (-1, 1): 0.3333333333333333}, (1, 2): {(0, 1): 0.3333333333333333, (1, 1): 0.3333333333333333, (-1, 1): 0.3333333333333333}, (1, 3): {(0, 1): 0.3333333333333333, (1, 1): 0.3333333333333333, (-1, 1): 0.3333333333333333}, (1, 4): {(0, 1): 0.3333333333333333, (1, 1): 0.3333333333333333, (-1, 1): 0.3333333333333333}, (1, 5): {(0, 1): 0.5, (1, 1): 0.5}, (1, 6): {(1, 1): 1.0}, (1, 7): {(1, 0): 0.5, (1, 1): 0.5}, (1, 8): {(1, 0): 0.3333333333333333, (1, 1): 0.3333333333333333, (1, -1): 0.3333333333333333}, (1, 9): {(1, 0): 0.5, (1, -1): 0.5}, (2, 0): {(0, 1): 0.3333333333333333, (1, 1): 0.3333333333333333, (-1, 1): 0.3333333333333333}, (2, 1): {(0, 1): 0.3333333333333333, (1, 1): 0.3333333333333333, (-1, 1): 0.3333333333333333}, (2, 2): {(0, 1): 0.3333333333333333, (1, 1): 0.3333333333333333, (-1, 1): 0.3333333333333333}, (2, 3): {(0, 1): 0.3333333333333333, (1, 1): 0.3333333333333333, (-1, 1): 0.3333333333333333}, (2, 4): {(0, 1): 0.3333333333333333, (1, 1): 0.3333333333333333, (-1, 1): 0.3333333333333333}, (2, 5): {(0, 1): 0.3333333333333333, (1, 1): 0.3333333333333333, (-1, 1): 0.3333333333333333}, (2, 6): {(0, 1): 0.5, (1, 1): 0.5}, (2, 7): {(1, 1): 1.0}, (2, 8): {(1, 0): 0.5, (1, 1): 0.5}, (2, 9): {(1, 0): 0.5, (1, -1): 0.5}, (3, 0): {(0, 1): 0.3333333333333333, (1, 1): 0.3333333333333333, (-1, 1): 0.3333333333333333}, (3, 1): {(0, 1): 0.3333333333333333, (1, 1): 0.3333333333333333, (-1, 1): 0.3333333333333333}, (3, 2): {(0, 1): 0.3333333333333333, (1, 1): 0.3333333333333333, (-1, 1): 0.3333333333333333}, (3, 3): {(0, 1): 0.3333333333333333, (1, 1): 0.3333333333333333, (-1, 1): 0.3333333333333333}, (3, 4): {(0, 1): 0.3333333333333333, (1, 1): 0.3333333333333333, (-1, 1): 0.3333333333333333}, (3, 5): {(0, 1): 0.3333333333333333, (1, 1): 0.3333333333333333, (-1, 1): 0.3333333333333333}, (3, 6): {(0, 1): 0.3333333333333333, (1, 1): 0.3333333333333333, (-1, 1): 0.3333333333333333}, (3, 7): {(0, 1): 0.5, (1, 1): 0.5}, (3, 8): {(1, 1): 1.0}, (3, 9): {(1, 0): 1.0}, (4, 0): {(0, 1): 0.5, (-1, 1): 0.5}, (4, 1): {(0, 1): 0.5, (-1, 1): 0.5}, (4, 2): {(0, 1): 0.5, (-1, 1): 0.5}, (4, 3): {(0, 1): 0.5, (-1, 1): 0.5}, (4, 4): {(0, 1): 0.5, (-1, 1): 0.5}, (4, 5): {(0, 1): 0.5, (-1, 1): 0.5}, (4, 6): {(0, 1): 0.5, (-1, 1): 0.5}, (4, 7): {(0, 1): 0.5, (-1, 1): 0.5}, (4, 8): {(0, 1): 1.0}, (4, 9): {(0, 1): 0.2, (1, 0): 0.2, (1, 1): 0.2, (-1, 1): 0.2, (1, -1): 0.2}}, 'R': {(0, 5): {(0, 1): 0.5, (1, 1): 0.5}, (0, 6): {(0, 1): 0.5, (1, 1): 0.5}, (0, 7): {(0, 1): 0.5, (1, 1): 0.5}, (0, 8): {(0, 1): 1.0}, (0, 9): {(0, 1): 0.2, (-1, 0): 0.2, (1, 1): 0.2, (-1, 1): 0.2, (-1, -1): 0.2}, (1, 5): {(0, 1): 0.3333333333333333, (1, 1): 0.3333333333333333, (-1, 1): 0.3333333333333333}, (1, 6): {(0, 1): 0.3333333333333333, (1, 1): 0.3333333333333333, (-1, 1): 0.3333333333333333}, (1, 7): {(0, 1): 0.5, (-1, 1): 0.5}, (1, 8): {(-1, 1): 1.0}, (1, 9): {(-1, 0): 1.0}, (2, 5): {(0, 1): 0.3333333333333333, (1, 1): 0.3333333333333333, (-1, 1): 0.3333333333333333}, (2, 6): {(0, 1): 0.5, (-1, 1): 0.5}, (2, 7): {(-1, 1): 1.0}, (2, 8): {(-1, 0): 0.5, (-1, 1): 0.5}, (2, 9): {(-1, 0): 0.5, (-1, -1): 0.5}, (3, 5): {(0, 1): 0.5, (-1, 1): 0.5}, (3, 6): {(-1, 1): 1.0}, (3, 7): {(-1, 0): 0.5, (-1, 1): 0.5}, (3, 8): {(-1, 0): 0.3333333333333333, (-1, 1): 0.3333333333333333, (-1, -1): 0.3333333333333333}, (3, 9): {(-1, 0): 0.5, (-1, -1): 0.5}, (4, 5): {(-1, 1): 1.0}, (4, 6): {(-1, 0): 0.5, (-1, 1): 0.5}, (4, 7): {(-1, 0): 0.3333333333333333, (-1, 1): 0.3333333333333333, (-1, -1): 0.3333333333333333}, (4, 8): {(-1, 0): 0.3333333333333333, (-1, 1): 0.3333333333333333, (-1, -1): 0.3333333333333333}, (4, 9): {(-1, 0): 0.5, (-1, -1): 0.5}}}
landmarkReward = rf.GetLandmarkOptionReward(actionCost, moveCost, goalStates, goalReward, landmarkPolicies, landmarkSPrime, getNextState)

optionReward = {'S': landmarkReward, 'L': landmarkReward, 'R': landmarkReward}
rewardFunction = rf.RewardFunction(optionReward)

optionSpace = {(0, 0): ['L'], (0, 1): ['L'], (0, 2): ['L'], (0, 3): ['L'], (0, 4): ['L'], (0, 5): ['L', 'R'], (0, 6): ['L', 'R'], (0, 7): ['L', 'R'], (0, 8): ['L', 'R'], (0, 9): ['L', 'R'], (1, 0): ['L'], (1, 1): ['L'], (1, 2): ['L'], (1, 3): ['L'], (1, 4): ['L'], (1, 5): ['L', 'R'], (1, 6): ['L', 'R'], (1, 7): ['L', 'R'], (1, 8): ['L', 'R'], (1, 9): ['L', 'R'], (2, 0): ['L'], (2, 1): ['L'], (2, 2): ['L'], (2, 3): ['L'], (2, 4): ['L'], (2, 5): ['L', 'R'], (2, 6): ['L', 'R'], (2, 7): ['L', 'R'], (2, 8): ['L', 'R'], (2, 9): ['L', 'R'], (3, 0): ['L'], (3, 1): ['L'], (3, 2): ['L'], (3, 3): ['L'], (3, 4): ['L'], (3, 5): ['L', 'R'], (3, 6): ['L', 'R'], (3, 7): ['L', 'R'], (3, 8): ['L', 'R'], (3, 9): ['L', 'R'], (4, 0): ['L'], (4, 1): ['L'], (4, 2): ['L'], (4, 3): ['L'], (4, 4): ['L'], (4, 5): ['L', 'R'], (4, 6): ['L', 'R'], (4, 7): ['L', 'R'], (4, 8): ['L', 'R'], (4, 9): ['L', 'R']}
optionSpaceFunction = lambda x: optionSpace[x]

gamma = 0.9
convergenceTolerance = 0.00001

bellmanUpdate = vi.BellmanUpdate(stateSet, optionSpaceFunction, transitionFunction, rewardFunction, gamma)
valueItSetUp = vi.ValueIteration(stateSet, optionSpaceFunction, convergenceTolerance, bellmanUpdate)
V = valueItSetUp()

policySetUp = vi.GetPolicy(stateSet, optionSpaceFunction, transitionFunction, rewardFunction, gamma, V, convergenceTolerance)
policy = {s:policySetUp(s) for s in stateSet} #interruption = policy ONLY with landmark options 

normalPathSetUp = GetNormalPath(landmarkPolicies, policy, optionTerminations, getNextState, goalState, stateSet)

checkCondition = io.CheckCondition(optionSpaceFunction)
interruptedPathSetUp = GetInterruptedPath(checkCondition, landmarkPolicies, policy, optionTerminations, getNextState, goalState, stateSet)

agentLocation = (4,0)
normalPath = normalPathSetUp(agentLocation)
interruptedPath = interruptedPathSetUp(agentLocation)

print("Original Path: ", normalPath)
print ("Interrupted Path: ", interruptedPath)
