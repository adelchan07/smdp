"""
Created on Thu Sep 10 19:03:38 2020
@author: adelphachan

main.py

code to run value iteration on Figure 5 in the publication
goalState = G2 (9,3)
"""
import numpy as np 
import valueIteration as targetCode 

fullGrid = [(i,j) for i in range(13) for j in range(13)]
border = [(0, 12), (1, 12), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12), (8, 12), (9, 12), (10, 12), (11, 12), (12, 12), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (12, 1), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 9), (12, 10), (12, 11)]
hallways = [(6,1), (6,3), (6,4), (6,5), (6,6), (11,6), (9,6), (8,6), (7,6), (5,6), (4,6), (2,6), (1,6), (7,7), (8,7), (10,7), (11,7)]

for state in border:
	fullGrid.remove(state)

for state in hallways:
	fullGrid.remove(state)

stateSet = fullGrid

getNextState = targetCode.tf.getNextState
primitivePolicies = {'up': (0,1), 'down': (0,-1), 'right': (1,0), 'left': (-1,0)}
primitiveSPrime = targetCode.tf.GetPrimitiveSPrime(primitivePolicies, stateSet, getNextState)
		
optionTerminations = {"h1": (6,2), "h2": (10,6), "h3": (3,6), "h4": (7,9)}
landmarkSPrime = targetCode.tf.GetLandmarkSPrime(optionTerminations)

actionCost = -1
moveCost = -3
goalStates = [(9,9)]
goalReward = 10
primitiveReward = targetCode.rf.GetPrimitiveOptionReward(actionCost, moveCost, goalStates, goalReward, primitiveSPrime)

landmarkPolicies = 
landmarkReward = targetCode.rf.GetLandmarkOptionReward(actionCost, moveCost, goalStates, goalReward, landmarkPolicies, landmarkSPrime, getNextState)

optionSPrime = {'up': primitiveSPrime, 'down':primitiveSPrime, 'left': primitiveSPrime, 'right': primitiveSPrime,'h1': landmarkSPrime, 'h2': landmarkSPrime, 'h3': landmarkSPrime, 'h4': landmarkSPrime} 
transitionFunction = targetCode.tf.TransitionFunction(optionSPrime)

optionReward = {'up': primitiveReward, 'down': primitiveReward, 'left': primitiveReward, 'right': primitiveReward, 'h1':landmarkReward, 'h2':landmarkReward, 'h3':landmarkReward, 'h4':landmarkReward} 
rewardFunction = targetCode.rf.RewardFunction(optionReward)

optionSpace = 
optionSpaceFunction = targetCode.osf.OptionSpaceFunction(optionSpace)

gamma = 0.9
convergenceTolerance = 0.00001

bellmanUpdate = targetCode.BellmanUpdate(stateSet, optionSpaceFunction, transitionFunction, rewardFunction, gamma)
valueItSetUp = targetCode.ValueIteration(stateSet, optionSpaceFunction, convergenceTolerance, bellmanUpdate)
V = valueItSetUp()

policySetUp = targetCode.GetPolicy(stateSet, optionSpaceFunction, transitionFunction, rewardFunction, gamma, V, convergenceTolerance)
policy = {s:policySetUp(s) for s in stateSet}

print(V)
print(policy)
