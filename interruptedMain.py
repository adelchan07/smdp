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
import valueIteration as vi 
import interruptionTransition as it

stateSet = [(i,j) for i in range(5) for j in range(10)]

optionTerminations = {'S': (4,5), 'L': (4,9), 'R': (0,9)}
landmarkSPrime = vi.tf.GetLandmarkSPrime(optionTerminations)
primitivePolicies = {'up': (0,1), 'down':(0,-1), 'left': (-1,0), 'right': (1,0)}

actionCost, moveCost = -1, -3
goalReward = 10
goalState = (0,9)

landmarkPolicies = {'S': {(0, 0): {(0, 1): 0.5, (1, 0): 0.5}, (0, 1): {(0, 1): 0.5, (1, 0): 0.5}, (0, 2): {(0, 1): 0.5, (1, 0): 0.5}, (0, 3): {(0, 1): 0.5, (1, 0): 0.5}, (0, 4): {(0, 1): 0.5, (1, 0): 0.5}, (0, 5): {(1, 0): 1.0}, (0, 6): {(1, 0): 0.5, (0, -1): 0.5}, (0, 7): {(1, 0): 0.5, (0, -1): 0.5}, (0, 8): {(1, 0): 0.5, (0, -1): 0.5}, (0, 9): {(1, 0): 0.5, (0, -1): 0.5}, (1, 0): {(0, 1): 0.5, (1, 0): 0.5}, (1, 1): {(0, 1): 0.5, (1, 0): 0.5}, (1, 2): {(0, 1): 0.5, (1, 0): 0.5}, (1, 3): {(0, 1): 0.5, (1, 0): 0.5}, (1, 4): {(0, 1): 0.5, (1, 0): 0.5}, (1, 5): {(1, 0): 1.0}, (1, 6): {(1, 0): 0.5, (0, -1): 0.5}, (1, 7): {(1, 0): 0.5, (0, -1): 0.5}, (1, 8): {(1, 0): 0.5, (0, -1): 0.5}, (1, 9): {(1, 0): 0.5, (0, -1): 0.5}, (2, 0): {(0, 1): 0.5, (1, 0): 0.5}, (2, 1): {(0, 1): 0.5, (1, 0): 0.5}, (2, 2): {(0, 1): 0.5, (1, 0): 0.5}, (2, 3): {(0, 1): 0.5, (1, 0): 0.5}, (2, 4): {(0, 1): 0.5, (1, 0): 0.5}, (2, 5): {(1, 0): 1.0}, (2, 6): {(1, 0): 0.5, (0, -1): 0.5}, (2, 7): {(1, 0): 0.5, (0, -1): 0.5}, (2, 8): {(1, 0): 0.5, (0, -1): 0.5}, (2, 9): {(1, 0): 0.5, (0, -1): 0.5}, (3, 0): {(0, 1): 0.5, (1, 0): 0.5}, (3, 1): {(0, 1): 0.5, (1, 0): 0.5}, (3, 2): {(0, 1): 0.5, (1, 0): 0.5}, (3, 3): {(0, 1): 0.5, (1, 0): 0.5}, (3, 4): {(0, 1): 0.5, (1, 0): 0.5}, (3, 5): {(1, 0): 1.0}, (3, 6): {(1, 0): 0.5, (0, -1): 0.5}, (3, 7): {(1, 0): 0.5, (0, -1): 0.5}, (3, 8): {(1, 0): 0.5, (0, -1): 0.5}, (3, 9): {(1, 0): 0.5, (0, -1): 0.5}, (4, 0): {(0, 1): 1.0}, (4, 1): {(0, 1): 1.0}, (4, 2): {(0, 1): 1.0}, (4, 3): {(0, 1): 1.0}, (4, 4): {(0, 1): 1.0}, (4, 5): {(1, 0): 1.0}, (4, 6): {(0, -1): 1.0}, (4, 7): {(0, -1): 1.0}, (4, 8): {(0, -1): 1.0}, (4, 9): {(0, -1): 1.0}}, 'L': {(0, 0): {(0, 1): 0.5, (1, 0): 0.5}, (0, 1): {(0, 1): 0.5, (1, 0): 0.5}, (0, 2): {(0, 1): 0.5, (1, 0): 0.5}, (0, 3): {(0, 1): 0.5, (1, 0): 0.5}, (0, 4): {(0, 1): 0.5, (1, 0): 0.5}, (0, 5): {(0, 1): 0.5, (1, 0): 0.5}, (0, 6): {(0, 1): 0.5, (1, 0): 0.5}, (0, 7): {(0, 1): 0.5, (1, 0): 0.5}, (0, 8): {(0, 1): 0.5, (1, 0): 0.5}, (0, 9): {(1, 0): 1.0}, (1, 0): {(0, 1): 0.5, (1, 0): 0.5}, (1, 1): {(0, 1): 0.5, (1, 0): 0.5}, (1, 2): {(0, 1): 0.5, (1, 0): 0.5}, (1, 3): {(0, 1): 0.5, (1, 0): 0.5}, (1, 4): {(0, 1): 0.5, (1, 0): 0.5}, (1, 5): {(0, 1): 0.5, (1, 0): 0.5}, (1, 6): {(0, 1): 0.5, (1, 0): 0.5}, (1, 7): {(0, 1): 0.5, (1, 0): 0.5}, (1, 8): {(0, 1): 0.5, (1, 0): 0.5}, (1, 9): {(1, 0): 1.0}, (2, 0): {(0, 1): 0.5, (1, 0): 0.5}, (2, 1): {(0, 1): 0.5, (1, 0): 0.5}, (2, 2): {(0, 1): 0.5, (1, 0): 0.5}, (2, 3): {(0, 1): 0.5, (1, 0): 0.5}, (2, 4): {(0, 1): 0.5, (1, 0): 0.5}, (2, 5): {(0, 1): 0.5, (1, 0): 0.5}, (2, 6): {(0, 1): 0.5, (1, 0): 0.5}, (2, 7): {(0, 1): 0.5, (1, 0): 0.5}, (2, 8): {(0, 1): 0.5, (1, 0): 0.5}, (2, 9): {(1, 0): 1.0}, (3, 0): {(0, 1): 0.5, (1, 0): 0.5}, (3, 1): {(0, 1): 0.5, (1, 0): 0.5}, (3, 2): {(0, 1): 0.5, (1, 0): 0.5}, (3, 3): {(0, 1): 0.5, (1, 0): 0.5}, (3, 4): {(0, 1): 0.5, (1, 0): 0.5}, (3, 5): {(0, 1): 0.5, (1, 0): 0.5}, (3, 6): {(0, 1): 0.5, (1, 0): 0.5}, (3, 7): {(0, 1): 0.5, (1, 0): 0.5}, (3, 8): {(0, 1): 0.5, (1, 0): 0.5}, (3, 9): {(1, 0): 1.0}, (4, 0): {(0, 1): 1.0}, (4, 1): {(0, 1): 1.0}, (4, 2): {(0, 1): 1.0}, (4, 3): {(0, 1): 1.0}, (4, 4): {(0, 1): 1.0}, (4, 5): {(0, 1): 1.0}, (4, 6): {(0, 1): 1.0}, (4, 7): {(0, 1): 1.0}, (4, 8): {(0, 1): 1.0}, (4, 9): {(0, 1): 0.5, (1, 0): 0.5}}, 'R': {(0, 5): {(0, 1): 1.0}, (0, 6): {(0, 1): 1.0}, (0, 7): {(0, 1): 1.0}, (0, 8): {(0, 1): 1.0}, (0, 9): {(0, 1): 0.5, (-1, 0): 0.5}, (1, 5): {(0, 1): 0.5, (-1, 0): 0.5}, (1, 6): {(0, 1): 0.5, (-1, 0): 0.5}, (1, 7): {(0, 1): 0.5, (-1, 0): 0.5}, (1, 8): {(0, 1): 0.5, (-1, 0): 0.5}, (1, 9): {(-1, 0): 1.0}, (2, 5): {(0, 1): 0.5, (-1, 0): 0.5}, (2, 6): {(0, 1): 0.5, (-1, 0): 0.5}, (2, 7): {(0, 1): 0.5, (-1, 0): 0.5}, (2, 8): {(0, 1): 0.5, (-1, 0): 0.5}, (2, 9): {(-1, 0): 1.0}, (3, 5): {(0, 1): 0.5, (-1, 0): 0.5}, (3, 6): {(0, 1): 0.5, (-1, 0): 0.5}, (3, 7): {(0, 1): 0.5, (-1, 0): 0.5}, (3, 8): {(0, 1): 0.5, (-1, 0): 0.5}, (3, 9): {(-1, 0): 1.0}, (4, 5): {(0, 1): 0.5, (-1, 0): 0.5}, (4, 6): {(0, 1): 0.5, (-1, 0): 0.5}, (4, 7): {(0, 1): 0.5, (-1, 0): 0.5}, (4, 8): {(0, 1): 0.5, (-1, 0): 0.5}, (4, 9): {(-1, 0): 1.0}}}
landmarkReward = vi.rf.GetLandmarkOptionReward(actionCost, moveCost, goalStates, goalReward, landmarkPolicies, landmarkSPrime, getNextState)

optionSPrime = {'S': landmarkSPrime, 'L': landmarkSPrime, 'R': landmarkSPrime}
transitionFunction = vi.tf.TransitionFunction(optionSPrime)

optionReward = {'S': landmarkReward, 'L': landmarkReward, 'R': landmarkReward}
rewardFunction = vi.rf.RewardFunction(optionReward)

optionSpace = {(0, 0): ['L', 'S'], (0, 1): ['L', 'S'], (0, 2): ['L', 'S'], (0, 3): ['L', 'S'], (0, 4): ['L', 'S'], (0, 5): ['L', 'S', 'R'], (0, 6): ['L', 'S', 'R'], (0, 7): ['L', 'S', 'R'], (0, 8): ['L', 'S', 'R'], (0, 9): ['L', 'S', 'R'], (1, 0): ['L', 'S'], (1, 1): ['L', 'S'], (1, 2): ['L', 'S'], (1, 3): ['L', 'S'], (1, 4): ['L', 'S'], (1, 5): ['L', 'S', 'R'], (1, 6): ['L', 'S', 'R'], (1, 7): ['L', 'S', 'R'], (1, 8): ['L', 'S', 'R'], (1, 9): ['L', 'S', 'R'], (2, 0): ['L', 'S'], (2, 1): ['L', 'S'], (2, 2): ['L', 'S'], (2, 3): ['L', 'S'], (2, 4): ['L', 'S'], (2, 5): ['L', 'S', 'R'], (2, 6): ['L', 'S', 'R'], (2, 7): ['L', 'S', 'R'], (2, 8): ['L', 'S', 'R'], (2, 9): ['L', 'S', 'R'], (3, 0): ['L', 'S'], (3, 1): ['L', 'S'], (3, 2): ['L', 'S'], (3, 3): ['L', 'S'], (3, 4): ['L', 'S'], (3, 5): ['L', 'S', 'R'], (3, 6): ['L', 'S', 'R'], (3, 7): ['L', 'S', 'R'], (3, 8): ['L', 'S', 'R'], (3, 9): ['L', 'S', 'R'], (4, 0): ['L', 'S'], (4, 1): ['L', 'S'], (4, 2): ['L', 'S'], (4, 3): ['L', 'S'], (4, 4): ['L', 'S'], (4, 5): ['L', 'S', 'R'], (4, 6): ['L', 'S', 'R'], (4, 7): ['L', 'S', 'R'], (4, 8): ['L', 'S', 'R'], (4, 9): ['L', 'S', 'R']}
optionSpaceFunction = vi.osf.OptionSpaceFunction(optionSpace)

gamma = 0.9
convergenceTolerance = 0.00001

bellmanUpdate = vi.BellmanUpdate(stateSet, optionSpaceFunction, transitionFunction, rewardFunction, gamma)
valueItSetUp = vi.ValueIteration(stateSet, optionSpaceFunction, convergenceTolerance, bellmanUpdate)
V = valueItSetUp()

policySetUp = vi.GetPolicy(stateSet, optionSpaceFunction, transitionFunction, rewardFunction, gamma, V, convergenceTolerance)
policy = {s:policySetUp(s) for s in stateSet}

"""
#end result = compare original path vs interrupted path
optionType = {'S': 'landmark', 'R': 'landmark', 'L': 'landmark'}

checkCondition = it.checkCondition(optionSpace)
compareOptions = it.compareOptions(policy, landmarkPolicies)

primitiveStep = it.primitiveStep(stateSet)
getNextState = it.getNextState(optionTerminations, primitivePolicies, stateSet)
getStatePath = it.getStatePath(landmarkPolicies, primitivePolicies, optionTerminations, primitiveStep)
getOption = it.getOption(policy, optionType)

normalPathSetUp = it.normalPath(policy, optionType, goalState, getStatePath, getNextState, getOption)
interruptedPathSetUp = it.interruptedPath(policy, primitiveStep, landmarkPolicies, checkCondition, compareOptions, goalState

agentLocation = (4,0)
normalPath = normalPathSetUp(agentLocation)
interruptedPathResult = interruptedPathSetUp(agentLocation)
interruptedPath = interruptedPathResult[0]
interruptedPathHistory = interruptedPathResult[1]

#final visualization = comparison of interruptedPath vs normalPath
"""
