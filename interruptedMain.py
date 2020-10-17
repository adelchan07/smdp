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

landmarkPolicies = #need to run and fill this in
landmarkReward = vi.rf.GetLandmarkOptionReward(actionCost, moveCost, goalStates, goalReward, landmarkPolicies, landmarkSPrime, getNextState)

optionSPrime = {'S': landmarkSPrime, 'L': landmarkSPrime, 'R': landmarkSPrime}
transitionFunction = vi.tf.TransitionFunction(optionSPrime)

optionReward = {'S': landmarkReward, 'L': landmarkReward, 'R': landmarkReward}
rewardFunction = vi.rf.RewardFunction(optionReward)

optionSpace = #need to run and fill this in
optionSpaceFunction = vi.osf.OptionSpaceFunction(optionSpace)

gamma = 0.9
convergenceTolerance = 0.00001

bellmanUpdate = vi.BellmanUpdate(stateSet, optionSpaceFunction, transitionFunction, rewardFunction, gamma)
valueItSetUp = vi.ValueIteration(stateSet, optionSpaceFunction, convergenceTolerance, bellmanUpdate)
V = valueItSetUp()

policySetUp = vi.GetPolicy(stateSet, optionSpaceFunction, transitionFunction, rewardFunction, gamma, V, convergenceTolerance)
policy = {s:policySetUp(s) for s in stateSet}

print(V, policy)
