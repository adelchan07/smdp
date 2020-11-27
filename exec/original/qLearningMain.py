
import numpy as np
import transitionFunction as tf
import rewardFunction as rf 

import sys
sys.path.append('../../src/')
import qLearningSMDP as qlsmdp

def main(): 
	fullGrid = [(i,j) for i in range(13) for j in range(13)]
	border = [(0, 12), (1, 12), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12), (8, 12), (9, 12), (10, 12), (11, 12), (12, 12), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (12, 1), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 9), (12, 10), (12, 11)]
	hallways = [(6,1), (6,3), (6,4), (6,5), (6,6), (11,6), (9,6), (8,6), (7,6), (5,6), (4,6), (2,6), (1,6), (7,7), (7,8), (7,10), (7,11)]

	for state in border:
		fullGrid.remove(state)

	for state in hallways:
		fullGrid.remove(state)

	stateSet = fullGrid

	getNextState = tf.getNextState
	primitivePolicies = {'up': (0,1), 'down': (0,-1), 'right': (1,0), 'left': (-1,0)}
	primitiveSPrime = tf.GetPrimitiveSPrime(primitivePolicies, stateSet, getNextState)

	optionTerminations = {"h1": (6,2), "h2": (10,6), "h3": (3,6), "h4": (7,9)}
	landmarkSPrime = tf.GetLandmarkSPrime(optionTerminations)

	optionSPrime = {'up': primitiveSPrime, 'down':primitiveSPrime, 'left': primitiveSPrime, 'right': primitiveSPrime,'h1': landmarkSPrime, 'h2': landmarkSPrime, 'h3': landmarkSPrime, 'h4': landmarkSPrime} 
	transitionFunction = tf.TransitionFunction(optionSPrime)
  	availableOptions = list(optionSPrime.keys())

	actionCost = -1
	moveCost = -3
	goalStates = [(9,9)]
	goalReward = 10
	primitiveReward = rf.GetPrimitiveOptionReward(actionCost, moveCost, goalStates, goalReward, primitiveSPrime)

	landmarkPolicies = {'h1': {(1, 1): {(0, 1): 0.5, (1, 0): 0.5}, (1, 2): {(1, 0): 1.0}, (1, 3): {(0, -1): 0.5, (1, 0): 0.5}, (1, 4): {(0, -1): 0.5, (1, 0): 0.5}, (1, 5): {(0, -1): 0.5, (1, 0): 0.5}, (2, 1): {(0, 1): 0.5, (1, 0): 0.5}, (2, 2): {(1, 0): 1.0}, (2, 3): {(0, -1): 0.5, (1, 0): 0.5}, (2, 4): {(0, -1): 0.5, (1, 0): 0.5}, (2, 5): {(0, -1): 0.5, (1, 0): 0.5}, (3, 1): {(0, 1): 0.5, (1, 0): 0.5}, (3, 2): {(1, 0): 1.0}, (3, 3): {(0, -1): 0.5, (1, 0): 0.5}, (3, 4): {(0, -1): 0.5, (1, 0): 0.5}, (3, 5): {(0, -1): 0.5, (1, 0): 0.5}, (4, 1): {(0, 1): 0.5, (1, 0): 0.5}, (4, 2): {(1, 0): 1.0}, (4, 3): {(0, -1): 0.5, (1, 0): 0.5}, (4, 4): {(0, -1): 0.5, (1, 0): 0.5}, (4, 5): {(0, -1): 0.5, (1, 0): 0.5}, (5, 1): {(0, 1): 1.0}, (5, 2): {(1, 0): 1.0}, (5, 3): {(0, -1): 1.0}, (5, 4): {(0, -1): 1.0}, (5, 5): {(0, -1): 1.0}, (7, 1): {(0, 1): 1.0}, (7, 2): {(-1, 0): 1.0}, (7, 3): {(0, -1): 1.0}, (7, 4): {(0, -1): 1.0}, (7, 5): {(0, -1): 1.0}, (8, 1): {(0, 1): 0.5, (-1, 0): 0.5}, (8, 2): {(-1, 0): 1.0}, (8, 3): {(0, -1): 0.5, (-1, 0): 0.5}, (8, 4): {(0, -1): 0.5, (-1, 0): 0.5}, (8, 5): {(0, -1): 0.5, (-1, 0): 0.5}, (9, 1): {(0, 1): 0.5, (-1, 0): 0.5}, (9, 2): {(-1, 0): 1.0}, (9, 3): {(0, -1): 0.5, (-1, 0): 0.5}, (9, 4): {(0, -1): 0.5, (-1, 0): 0.5}, (9, 5): {(0, -1): 0.5, (-1, 0): 0.5}, (10, 1): {(0, 1): 0.5, (-1, 0): 0.5}, (10, 2): {(-1, 0): 1.0}, (10, 3): {(0, -1): 0.5, (-1, 0): 0.5}, (10, 4): {(0, -1): 0.5, (-1, 0): 0.5}, (10, 5): {(0, -1): 0.5, (-1, 0): 0.5}, (11, 1): {(0, 1): 0.5, (-1, 0): 0.5}, (11, 2): {(-1, 0): 1.0}, (11, 3): {(0, -1): 0.5, (-1, 0): 0.5}, (11, 4): {(0, -1): 0.5, (-1, 0): 0.5}, (11, 5): {(0, -1): 0.5, (-1, 0): 0.5}, (6, 2): {(0, 1): 0.5, (0, -1): 0.5}}, 'h2': {(7, 1): {(0, 1): 0.5, (1, 0): 0.5}, (7, 2): {(0, 1): 0.5, (1, 0): 0.5}, (7, 3): {(0, 1): 0.5, (1, 0): 0.5}, (7, 4): {(0, 1): 0.5, (1, 0): 0.5}, (7, 5): {(1, 0): 1.0}, (8, 1): {(0, 1): 0.5, (1, 0): 0.5}, (8, 2): {(0, 1): 0.5, (1, 0): 0.5}, (8, 3): {(0, 1): 0.5, (1, 0): 0.5}, (8, 4): {(0, 1): 0.5, (1, 0): 0.5}, (8, 5): {(1, 0): 1.0}, (9, 1): {(0, 1): 0.5, (1, 0): 0.5}, (9, 2): {(0, 1): 0.5, (1, 0): 0.5}, (9, 3): {(0, 1): 0.5, (1, 0): 0.5}, (9, 4): {(0, 1): 0.5, (1, 0): 0.5}, (9, 5): {(1, 0): 1.0}, (10, 1): {(0, 1): 1.0}, (10, 2): {(0, 1): 1.0}, (10, 3): {(0, 1): 1.0}, (10, 4): {(0, 1): 1.0}, (10, 5): {(0, 1): 1.0}, (11, 1): {(0, 1): 0.5, (-1, 0): 0.5}, (11, 2): {(0, 1): 0.5, (-1, 0): 0.5}, (11, 3): {(0, 1): 0.5, (-1, 0): 0.5}, (11, 4): {(0, 1): 0.5, (-1, 0): 0.5}, (11, 5): {(-1, 0): 1.0}, (8, 7): {(1, 0): 1.0}, (8, 8): {(0, -1): 0.5, (1, 0): 0.5}, (8, 9): {(0, -1): 0.5, (1, 0): 0.5}, (8, 10): {(0, -1): 0.5, (1, 0): 0.5}, (8, 11): {(0, -1): 0.5, (1, 0): 0.5}, (9, 7): {(1, 0): 1.0}, (9, 8): {(0, -1): 0.5, (1, 0): 0.5}, (9, 9): {(0, -1): 0.5, (1, 0): 0.5}, (9, 10): {(0, -1): 0.5, (1, 0): 0.5}, (9, 11): {(0, -1): 0.5, (1, 0): 0.5}, (10, 7): {(0, -1): 1.0}, (10, 8): {(0, -1): 1.0}, (10, 9): {(0, -1): 1.0}, (10, 10): {(0, -1): 1.0}, (10, 11): {(0, -1): 1.0}, (11, 7): {(-1, 0): 1.0}, (11, 8): {(0, -1): 0.5, (-1, 0): 0.5}, (11, 9): {(0, -1): 0.5, (-1, 0): 0.5}, (11, 10): {(0, -1): 0.5, (-1, 0): 0.5}, (11, 11): {(0, -1): 0.5, (-1, 0): 0.5}, (10, 6): {(1, 0): 0.5, (-1, 0): 0.5}}, 'h3': {(1, 1): {(0, 1): 0.5, (1, 0): 0.5}, (1, 2): {(0, 1): 0.5, (1, 0): 0.5}, (1, 3): {(0, 1): 0.5, (1, 0): 0.5}, (1, 4): {(0, 1): 0.5, (1, 0): 0.5}, (1, 5): {(1, 0): 1.0}, (2, 1): {(0, 1): 0.5, (1, 0): 0.5}, (2, 2): {(0, 1): 0.5, (1, 0): 0.5}, (2, 3): {(0, 1): 0.5, (1, 0): 0.5}, (2, 4): {(0, 1): 0.5, (1, 0): 0.5}, (2, 5): {(1, 0): 1.0}, (3, 1): {(0, 1): 1.0}, (3, 2): {(0, 1): 1.0}, (3, 3): {(0, 1): 1.0}, (3, 4): {(0, 1): 1.0}, (3, 5): {(0, 1): 1.0}, (4, 1): {(0, 1): 0.5, (-1, 0): 0.5}, (4, 2): {(0, 1): 0.5, (-1, 0): 0.5}, (4, 3): {(0, 1): 0.5, (-1, 0): 0.5}, (4, 4): {(0, 1): 0.5, (-1, 0): 0.5}, (4, 5): {(-1, 0): 1.0}, (5, 1): {(0, 1): 0.5, (-1, 0): 0.5}, (5, 2): {(0, 1): 0.5, (-1, 0): 0.5}, (5, 3): {(0, 1): 0.5, (-1, 0): 0.5}, (5, 4): {(0, 1): 0.5, (-1, 0): 0.5}, (5, 5): {(-1, 0): 1.0}, (1, 7): {(1, 0): 1.0}, (1, 8): {(0, -1): 0.5, (1, 0): 0.5}, (1, 9): {(0, -1): 0.5, (1, 0): 0.5}, (1, 10): {(0, -1): 0.5, (1, 0): 0.5}, (1, 11): {(0, -1): 0.5, (1, 0): 0.5}, (2, 7): {(1, 0): 1.0}, (2, 8): {(0, -1): 0.5, (1, 0): 0.5}, (2, 9): {(0, -1): 0.5, (1, 0): 0.5}, (2, 10): {(0, -1): 0.5, (1, 0): 0.5}, (2, 11): {(0, -1): 0.5, (1, 0): 0.5}, (3, 7): {(0, -1): 1.0}, (3, 8): {(0, -1): 1.0}, (3, 9): {(0, -1): 1.0}, (3, 10): {(0, -1): 1.0}, (3, 11): {(0, -1): 1.0}, (4, 7): {(-1, 0): 1.0}, (4, 8): {(0, -1): 0.5, (-1, 0): 0.5}, (4, 9): {(0, -1): 0.5, (-1, 0): 0.5}, (4, 10): {(0, -1): 0.5, (-1, 0): 0.5}, (4, 11): {(0, -1): 0.5, (-1, 0): 0.5}, (5, 7): {(-1, 0): 1.0}, (5, 8): {(0, -1): 0.5, (-1, 0): 0.5}, (5, 9): {(0, -1): 0.5, (-1, 0): 0.5}, (5, 10): {(0, -1): 0.5, (-1, 0): 0.5}, (5, 11): {(0, -1): 0.5, (-1, 0): 0.5}, (6, 7): {(-1, 0): 1.0}, (6, 8): {(0, -1): 0.5, (-1, 0): 0.5}, (6, 9): {(0, -1): 0.5, (-1, 0): 0.5}, (6, 10): {(0, -1): 0.5, (-1, 0): 0.5}, (6, 11): {(0, -1): 0.5, (-1, 0): 0.5}, (3, 6): {(1, 0): 0.5, (-1, 0): 0.5}}, 'h4': {(8, 7): {(0, 1): 1.0}, (8, 8): {(0, 1): 1.0}, (8, 9): {(-1, 0): 1.0}, (8, 10): {(0, -1): 1.0}, (8, 11): {(0, -1): 1.0}, (9, 7): {(0, 1): 0.5, (-1, 0): 0.5}, (9, 8): {(0, 1): 0.5, (-1, 0): 0.5}, (9, 9): {(-1, 0): 1.0}, (9, 10): {(0, -1): 0.5, (-1, 0): 0.5}, (9, 11): {(0, -1): 0.5, (-1, 0): 0.5}, (10, 7): {(0, 1): 0.5, (-1, 0): 0.5}, (10, 8): {(0, 1): 0.5, (-1, 0): 0.5}, (10, 9): {(-1, 0): 1.0}, (10, 10): {(0, -1): 0.5, (-1, 0): 0.5}, (10, 11): {(0, -1): 0.5, (-1, 0): 0.5}, (11, 7): {(0, 1): 0.5, (-1, 0): 0.5}, (11, 8): {(0, 1): 0.5, (-1, 0): 0.5}, (11, 9): {(-1, 0): 1.0}, (11, 10): {(0, -1): 0.5, (-1, 0): 0.5}, (11, 11): {(0, -1): 0.5, (-1, 0): 0.5}, (1, 7): {(0, 1): 0.5, (1, 0): 0.5}, (1, 8): {(0, 1): 0.5, (1, 0): 0.5}, (1, 9): {(1, 0): 1.0}, (1, 10): {(0, -1): 0.5, (1, 0): 0.5}, (1, 11): {(0, -1): 0.5, (1, 0): 0.5}, (2, 7): {(0, 1): 0.5, (1, 0): 0.5}, (2, 8): {(0, 1): 0.5, (1, 0): 0.5}, (2, 9): {(1, 0): 1.0}, (2, 10): {(0, -1): 0.5, (1, 0): 0.5}, (2, 11): {(0, -1): 0.5, (1, 0): 0.5}, (3, 7): {(0, 1): 0.5, (1, 0): 0.5}, (3, 8): {(0, 1): 0.5, (1, 0): 0.5}, (3, 9): {(1, 0): 1.0}, (3, 10): {(0, -1): 0.5, (1, 0): 0.5}, (3, 11): {(0, -1): 0.5, (1, 0): 0.5}, (4, 7): {(0, 1): 0.5, (1, 0): 0.5}, (4, 8): {(0, 1): 0.5, (1, 0): 0.5}, (4, 9): {(1, 0): 1.0}, (4, 10): {(0, -1): 0.5, (1, 0): 0.5}, (4, 11): {(0, -1): 0.5, (1, 0): 0.5}, (5, 7): {(0, 1): 0.5, (1, 0): 0.5}, (5, 8): {(0, 1): 0.5, (1, 0): 0.5}, (5, 9): {(1, 0): 1.0}, (5, 10): {(0, -1): 0.5, (1, 0): 0.5}, (5, 11): {(0, -1): 0.5, (1, 0): 0.5}, (6, 7): {(0, 1): 1.0}, (6, 8): {(0, 1): 1.0}, (6, 9): {(1, 0): 1.0}, (6, 10): {(0, -1): 1.0}, (6, 11): {(0, -1): 1.0}, (7, 9): {(0, 1): 0.5, (0, -1): 0.5}}}
	landmarkReward = rf.GetLandmarkOptionReward(actionCost, moveCost, goalStates, goalReward, landmarkPolicies, landmarkSPrime, getNextState)

	optionReward = {'up': primitiveReward, 'down': primitiveReward, 'left': primitiveReward, 'right': primitiveReward, 'h1':landmarkReward, 'h2':landmarkReward, 'h3':landmarkReward, 'h4':landmarkReward} 
	rewardFunction = rf.RewardFunction(optionReward)

	optionSpace = {(1, 1): ['up', 'down', 'left', 'right', 'h1', 'h3'], (1, 2): ['up', 'down', 'left', 'right', 'h1', 'h3'], (1, 3): ['up', 'down', 'left', 'right', 'h1', 'h3'], (1, 4): ['up', 'down', 'left', 'right', 'h1', 'h3'], (1, 5): ['up', 'down', 'left', 'right', 'h1', 'h3'], (1, 7): ['up', 'down', 'left', 'right', 'h3', 'h4'], (1, 8): ['up', 'down', 'left', 'right', 'h3', 'h4'], (1, 9): ['up', 'down', 'left', 'right', 'h3', 'h4'], (1, 10): ['up', 'down', 'left', 'right', 'h3', 'h4'], (1, 11): ['up', 'down', 'left', 'right', 'h3', 'h4'], (2, 1): ['up', 'down', 'left', 'right', 'h1', 'h3'], (2, 2): ['up', 'down', 'left', 'right', 'h1', 'h3'], (2, 3): ['up', 'down', 'left', 'right', 'h1', 'h3'], (2, 4): ['up', 'down', 'left', 'right', 'h1', 'h3'], (2, 5): ['up', 'down', 'left', 'right', 'h1', 'h3'], (2, 7): ['up', 'down', 'left', 'right', 'h3', 'h4'], (2, 8): ['up', 'down', 'left', 'right', 'h3', 'h4'], (2, 9): ['up', 'down', 'left', 'right', 'h3', 'h4'], (2, 10): ['up', 'down', 'left', 'right', 'h3', 'h4'], (2, 11): ['up', 'down', 'left', 'right', 'h3', 'h4'], (3, 1): ['up', 'down', 'left', 'right', 'h1', 'h3'], (3, 2): ['up', 'down', 'left', 'right', 'h1', 'h3'], (3, 3): ['up', 'down', 'left', 'right', 'h1', 'h3'], (3, 4): ['up', 'down', 'left', 'right', 'h1', 'h3'], (3, 5): ['up', 'down', 'left', 'right', 'h1', 'h3'], (3, 6): ['up', 'down', 'left', 'right', 'h3'], (3, 7): ['up', 'down', 'left', 'right', 'h3', 'h4'], (3, 8): ['up', 'down', 'left', 'right', 'h3', 'h4'], (3, 9): ['up', 'down', 'left', 'right', 'h3', 'h4'], (3, 10): ['up', 'down', 'left', 'right', 'h3', 'h4'], (3, 11): ['up', 'down', 'left', 'right', 'h3', 'h4'], (4, 1): ['up', 'down', 'left', 'right', 'h1', 'h3'], (4, 2): ['up', 'down', 'left', 'right', 'h1', 'h3'], (4, 3): ['up', 'down', 'left', 'right', 'h1', 'h3'], (4, 4): ['up', 'down', 'left', 'right', 'h1', 'h3'], (4, 5): ['up', 'down', 'left', 'right', 'h1', 'h3'], (4, 7): ['up', 'down', 'left', 'right', 'h3', 'h4'], (4, 8): ['up', 'down', 'left', 'right', 'h3', 'h4'], (4, 9): ['up', 'down', 'left', 'right', 'h3', 'h4'], (4, 10): ['up', 'down', 'left', 'right', 'h3', 'h4'], (4, 11): ['up', 'down', 'left', 'right', 'h3', 'h4'], (5, 1): ['up', 'down', 'left', 'right', 'h1', 'h3'], (5, 2): ['up', 'down', 'left', 'right', 'h1', 'h3'], (5, 3): ['up', 'down', 'left', 'right', 'h1', 'h3'], (5, 4): ['up', 'down', 'left', 'right', 'h1', 'h3'], (5, 5): ['up', 'down', 'left', 'right', 'h1', 'h3'], (5, 7): ['up', 'down', 'left', 'right', 'h3', 'h4'], (5, 8): ['up', 'down', 'left', 'right', 'h3', 'h4'], (5, 9): ['up', 'down', 'left', 'right', 'h3', 'h4'], (5, 10): ['up', 'down', 'left', 'right', 'h3', 'h4'], (5, 11): ['up', 'down', 'left', 'right', 'h3', 'h4'], (6, 2): ['up', 'down', 'left', 'right', 'h1'], (6, 7): ['up', 'down', 'left', 'right', 'h3', 'h4'], (6, 8): ['up', 'down', 'left', 'right', 'h3', 'h4'], (6, 9): ['up', 'down', 'left', 'right', 'h3', 'h4'], (6, 10): ['up', 'down', 'left', 'right', 'h3', 'h4'], (6, 11): ['up', 'down', 'left', 'right', 'h3', 'h4'], (7, 1): ['up', 'down', 'left', 'right', 'h1', 'h2'], (7, 2): ['up', 'down', 'left', 'right', 'h1', 'h2'], (7, 3): ['up', 'down', 'left', 'right', 'h1', 'h2'], (7, 4): ['up', 'down', 'left', 'right', 'h1', 'h2'], (7, 5): ['up', 'down', 'left', 'right', 'h1', 'h2'], (7, 9): ['up', 'down', 'left', 'right', 'h4'], (8, 1): ['up', 'down', 'left', 'right', 'h1', 'h2'], (8, 2): ['up', 'down', 'left', 'right', 'h1', 'h2'], (8, 3): ['up', 'down', 'left', 'right', 'h1', 'h2'], (8, 4): ['up', 'down', 'left', 'right', 'h1', 'h2'], (8, 5): ['up', 'down', 'left', 'right', 'h1', 'h2'], (8, 7): ['up', 'down', 'left', 'right', 'h2', 'h4'], (8, 8): ['up', 'down', 'left', 'right', 'h2', 'h4'], (8, 9): ['up', 'down', 'left', 'right', 'h2', 'h4'], (8, 10): ['up', 'down', 'left', 'right', 'h2', 'h4'], (8, 11): ['up', 'down', 'left', 'right', 'h2', 'h4'], (9, 1): ['up', 'down', 'left', 'right', 'h1', 'h2'], (9, 2): ['up', 'down', 'left', 'right', 'h1', 'h2'], (9, 3): ['up', 'down', 'left', 'right', 'h1', 'h2'], (9, 4): ['up', 'down', 'left', 'right', 'h1', 'h2'], (9, 5): ['up', 'down', 'left', 'right', 'h1', 'h2'], (9, 7): ['up', 'down', 'left', 'right', 'h2', 'h4'], (9, 8): ['up', 'down', 'left', 'right', 'h2', 'h4'], (9, 9): ['up', 'down', 'left', 'right', 'h2', 'h4'], (9, 10): ['up', 'down', 'left', 'right', 'h2', 'h4'], (9, 11): ['up', 'down', 'left', 'right', 'h2', 'h4'], (10, 1): ['up', 'down', 'left', 'right', 'h1', 'h2'], (10, 2): ['up', 'down', 'left', 'right', 'h1', 'h2'], (10, 3): ['up', 'down', 'left', 'right', 'h1', 'h2'], (10, 4): ['up', 'down', 'left', 'right', 'h1', 'h2'], (10, 5): ['up', 'down', 'left', 'right', 'h1', 'h2'], (10, 6): ['up', 'down', 'left', 'right', 'h2'], (10, 7): ['up', 'down', 'left', 'right', 'h2', 'h4'], (10, 8): ['up', 'down', 'left', 'right', 'h2', 'h4'], (10, 9): ['up', 'down', 'left', 'right', 'h2', 'h4'], (10, 10): ['up', 'down', 'left', 'right', 'h2', 'h4'], (10, 11): ['up', 'down', 'left', 'right', 'h2', 'h4'], (11, 1): ['up', 'down', 'left', 'right', 'h1', 'h2'], (11, 2): ['up', 'down', 'left', 'right', 'h1', 'h2'], (11, 3): ['up', 'down', 'left', 'right', 'h1', 'h2'], (11, 4): ['up', 'down', 'left', 'right', 'h1', 'h2'], (11, 5): ['up', 'down', 'left', 'right', 'h1', 'h2'], (11, 7): ['up', 'down', 'left', 'right', 'h2', 'h4'], (11, 8): ['up', 'down', 'left', 'right', 'h2', 'h4'], (11, 9): ['up', 'down', 'left', 'right', 'h2', 'h4'], (11, 10): ['up', 'down', 'left', 'right', 'h2', 'h4'], (11, 11): ['up', 'down', 'left', 'right', 'h2', 'h4']}
	optionSpaceFunction = lambda x: optionSpace[x]
  
	episodes = 500
	alpha = 0.5
	gamma = 0.9
	epsilon = 0.9
	convergenceTolerance = 0.000001
  
	qLearning = qlsmdp.QLearningSMDP(episodes, alpha, gamma, epsilon, convergenceTolerance)
	result = qLearning(stateSet, transitionFunction, rewardFunction, optionSpaceFunction, goalStates, availableOptions)
	
	print("QTable: ")
	print(result[0])
	print("policy: ")
	print(result[1])
	
if __name__ == "__main__":
    main()
