"""
Created on Sun Aug 23 17:02:48 2020

@author: adelphachan

testOptionValueIteration.py

"""
import sys
sys.path.append('..') 

import numpy as np
import unittest
from ddt import ddt, data, unpack
import optionValueIteration as targetCode 

@ddt
class TestValueIteration(unittest.TestCase):
	def setUp(self):
		#13x9 grid w/ outer boundary and inner hallways
		#blockList = [(5, 1), (1, 3), (2, 3), (4, 3), (5, 3), (5, 4), (6, 4), (7, 4), (8, 4), (10, 4), (11, 4), (5, 5), (5, 7), (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (12, 0), (12, 1), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (9, 8), (10, 8), (11, 8)]
		stateSet = [(1, 1), (1, 2), (1, 4), (1, 5), (1, 6), (1, 7), (2, 1), (2, 2), (2, 4), (2, 5), (2, 6), (2, 7), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (4, 1), (4, 2), (4, 4), (4, 5), (4, 6), (4, 7), (5, 2), (5, 6), (6, 1), (6, 2), (6, 3), (6, 5), (6, 6), (6, 7), (7, 1), (7, 2), (7, 3), (7, 5), (7, 6), (7, 7), (8, 1), (8, 2), (8, 3), (8, 5), (8, 6), (8, 7), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (10, 1), (10, 2), (10, 3), (10, 5), (10, 6), (10, 7), (11, 1), (11, 2), (11, 3), (11, 5), (11, 6), (11, 7)]	
		
		optionSpace = {(1, 1): ['up', 'down', 'left', 'right', 'h1', 'h2'], (1, 2): ['up', 'down', 'left', 'right', 'h1', 'h2'], (1, 4): ['up', 'down', 'left', 'right', 'h1', 'h3'], (1, 5): ['up', 'down', 'left', 'right', 'h1', 'h3'], (1, 6): ['up', 'down', 'left', 'right', 'h1', 'h3'], (1, 7): ['up', 'down', 'left', 'right', 'h1', 'h3'], (2, 1): ['up', 'down', 'left', 'right', 'h1', 'h2'], (2, 2): ['up', 'down', 'left', 'right', 'h1', 'h2'], (2, 4): ['up', 'down', 'left', 'right', 'h1', 'h3'], (2, 5): ['up', 'down', 'left', 'right', 'h1', 'h3'], (2, 6): ['up', 'down', 'left', 'right', 'h1', 'h3'], (2, 7): ['up', 'down', 'left', 'right', 'h1', 'h3'], (3, 1): ['up', 'down', 'left', 'right', 'h1', 'h2'], (3, 2): ['up', 'down', 'left', 'right', 'h1', 'h2'], (3, 3): ['up', 'down', 'left', 'right', 'h1'], (3, 4): ['up', 'down', 'left', 'right', 'h1', 'h3'], (3, 5): ['up', 'down', 'left', 'right', 'h1', 'h3'], (3, 6): ['up', 'down', 'left', 'right', 'h1', 'h3'], (3, 7): ['up', 'down', 'left', 'right', 'h1', 'h3'], (4, 1): ['up', 'down', 'left', 'right', 'h1', 'h2'], (4, 2): ['up', 'down', 'left', 'right', 'h1', 'h2'], (4, 4): ['up', 'down', 'left', 'right', 'h1', 'h3'], (4, 5): ['up', 'down', 'left', 'right', 'h1', 'h3'], (4, 6): ['up', 'down', 'left', 'right', 'h1', 'h3'], (4, 7): ['up', 'down', 'left', 'right', 'h1', 'h3'], (5, 2): ['up', 'down', 'left', 'right', 'h2'], (5, 6): ['up', 'down', 'left', 'right', 'h3'], (6, 1): ['up', 'down', 'left', 'right', 'h2', 'h4'], (6, 2): ['up', 'down', 'left', 'right', 'h2', 'h4'], (6, 3): ['up', 'down', 'left', 'right', 'h2', 'h4'], (6, 5): ['up', 'down', 'left', 'right', 'h3', 'h4'], (6, 6): ['up', 'down', 'left', 'right', 'h3', 'h4'], (6, 7): ['up', 'down', 'left', 'right', 'h3', 'h4'], (7, 1): ['up', 'down', 'left', 'right', 'h2', 'h4'], (7, 2): ['up', 'down', 'left', 'right', 'h2', 'h4'], (7, 3): ['up', 'down', 'left', 'right', 'h2', 'h4'], (7, 5): ['up', 'down', 'left', 'right', 'h3', 'h4'], (7, 6): ['up', 'down', 'left', 'right', 'h3', 'h4'], (7, 7): ['up', 'down', 'left', 'right', 'h3', 'h4'], (8, 1): ['up', 'down', 'left', 'right', 'h2', 'h4'], (8, 2): ['up', 'down', 'left', 'right', 'h2', 'h4'], (8, 3): ['up', 'down', 'left', 'right', 'h2', 'h4'], (8, 5): ['up', 'down', 'left', 'right', 'h3', 'h4'], (8, 6): ['up', 'down', 'left', 'right', 'h3', 'h4'], (8, 7): ['up', 'down', 'left', 'right', 'h3', 'h4'], (9, 1): ['up', 'down', 'left', 'right', 'h2', 'h4'], (9, 2): ['up', 'down', 'left', 'right', 'h2', 'h4'], (9, 3): ['up', 'down', 'left', 'right', 'h2', 'h4'], (9, 4): ['up', 'down', 'left', 'right', 'h4'], (9, 5): ['up', 'down', 'left', 'right', 'h3', 'h4'], (9, 6): ['up', 'down', 'left', 'right', 'h3', 'h4'], (9, 7): ['up', 'down', 'left', 'right', 'h3', 'h4'], (10, 1): ['up', 'down', 'left', 'right', 'h2', 'h4'], (10, 2): ['up', 'down', 'left', 'right', 'h2', 'h4'], (10, 3): ['up', 'down', 'left', 'right', 'h2', 'h4'], (10, 5): ['up', 'down', 'left', 'right', 'h3', 'h4'], (10, 6): ['up', 'down', 'left', 'right', 'h3', 'h4'], (10, 7): ['up', 'down', 'left', 'right', 'h3', 'h4'], (11, 1): ['up', 'down', 'left', 'right', 'h2', 'h4'], (11, 2): ['up', 'down', 'left', 'right', 'h2', 'h4'], (11, 3): ['up', 'down', 'left', 'right', 'h2', 'h4'], (11, 5): ['up', 'down', 'left', 'right', 'h3', 'h4'], (11, 6): ['up', 'down', 'left', 'right', 'h3', 'h4'], (11, 7): ['up', 'down', 'left', 'right', 'h3', 'h4']}
		optionSpaceFunction = targetCode.optionSpaceFunction(optionSpace)
		
		optionType = {'h1': 'landmark', 'h2': 'landmark', 'h3': 'landmark', 'h4': 'landmark', 'up': 'primitive', 'down': 'primitive', 'left': 'primitive', 'right': 'primitive'}
		
		getNextState = targetCode.tf.getNextState
		landmarkTerminations = {"h1": (3,3), "h2": (5,2), "h3": (5,6), "h4": (9,4)}
		primitiveTransition = targetCode.tf.getPrimitiveSPrime(stateSet, getNextState)
		landmarkTransition = targetCode.tf.getLandmarkSPrime(landmarkTerminations)
		optionSPrime = {'h1': landmarkTransition, 'h2': landmarkTransition, 'h3': landmarkTransition, 'h4': landmarkTransition, 'up': primitiveTransition, 'down': primitiveTransition, 'left': primitiveTransition, 'right': primitiveTransition}
		transitionFunction = targetCode.tf.transitionFunction(optionSPrime)
		
		#rewardFunction
		
		#gamma


#testing main value iteration code
@ddt
class TestOptionValueIteration(unittest.TestCase):
	def setUp(self):

		#13x9 grid w/ outer boundary and inner hallways
		#blockList = [(5, 1), (1, 3), (2, 3), (4, 3), (5, 3), (5, 4), (6, 4), (7, 4), (8, 4), (10, 4), (11, 4), (5, 5), (5, 7), (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (12, 0), (12, 1), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (9, 8), (10, 8), (11, 8)]
		stateSet = [(1, 1), (1, 2), (1, 4), (1, 5), (1, 6), (1, 7), (2, 1), (2, 2), (2, 4), (2, 5), (2, 6), (2, 7), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (4, 1), (4, 2), (4, 4), (4, 5), (4, 6), (4, 7), (5, 2), (5, 6), (6, 1), (6, 2), (6, 3), (6, 5), (6, 6), (6, 7), (7, 1), (7, 2), (7, 3), (7, 5), (7, 6), (7, 7), (8, 1), (8, 2), (8, 3), (8, 5), (8, 6), (8, 7), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (10, 1), (10, 2), (10, 3), (10, 5), (10, 6), (10, 7), (11, 1), (11, 2), (11, 3), (11, 5), (11, 6), (11, 7)]

		primitivePolicies = {'up': {(1, 1): (0, 1), (1, 2): (0, 1), (1, 4): (0, 1), (1, 5): (0, 1), (1, 6): (0, 1), (1, 7): (0, 1), (2, 1): (0, 1), (2, 2): (0, 1), (2, 4): (0, 1), (2, 5): (0, 1), (2, 6): (0, 1), (2, 7): (0, 1), (3, 1): (0, 1), (3, 2): (0, 1), (3, 3): (0, 1), (3, 4): (0, 1), (3, 5): (0, 1), (3, 6): (0, 1), (3, 7): (0, 1), (4, 1): (0, 1), (4, 2): (0, 1), (4, 4): (0, 1), (4, 5): (0, 1), (4, 6): (0, 1), (4, 7): (0, 1), (5, 2): (0, 1), (5, 6): (0, 1), (6, 1): (0, 1), (6, 2): (0, 1), (6, 3): (0, 1), (6, 5): (0, 1), (6, 6): (0, 1), (6, 7): (0, 1), (7, 1): (0, 1), (7, 2): (0, 1), (7, 3): (0, 1), (7, 5): (0, 1), (7, 6): (0, 1), (7, 7): (0, 1), (8, 1): (0, 1), (8, 2): (0, 1), (8, 3): (0, 1), (8, 5): (0, 1), (8, 6): (0, 1), (8, 7): (0, 1), (9, 1): (0, 1), (9, 2): (0, 1), (9, 3): (0, 1), (9, 4): (0, 1), (9, 5): (0, 1), (9, 6): (0, 1), (9, 7): (0, 1), (10, 1): (0, 1), (10, 2): (0, 1), (10, 3): (0, 1), (10, 5): (0, 1), (10, 6): (0, 1), (10, 7): (0, 1), (11, 1): (0, 1), (11, 2): (0, 1), (11, 3): (0, 1), (11, 5): (0, 1), (11, 6): (0, 1), (11, 7): (0, 1)}, 'down': {(1, 1): (0, -1), (1, 2): (0, -1), (1, 4): (0, -1), (1, 5): (0, -1), (1, 6): (0, -1), (1, 7): (0, -1), (2, 1): (0, -1), (2, 2): (0, -1), (2, 4): (0, -1), (2, 5): (0, -1), (2, 6): (0, -1), (2, 7): (0, -1), (3, 1): (0, -1), (3, 2): (0, -1), (3, 3): (0, -1), (3, 4): (0, -1), (3, 5): (0, -1), (3, 6): (0, -1), (3, 7): (0, -1), (4, 1): (0, -1), (4, 2): (0, -1), (4, 4): (0, -1), (4, 5): (0, -1), (4, 6): (0, -1), (4, 7): (0, -1), (5, 2): (0, -1), (5, 6): (0, -1), (6, 1): (0, -1), (6, 2): (0, -1), (6, 3): (0, -1), (6, 5): (0, -1), (6, 6): (0, -1), (6, 7): (0, -1), (7, 1): (0, -1), (7, 2): (0, -1), (7, 3): (0, -1), (7, 5): (0, -1), (7, 6): (0, -1), (7, 7): (0, -1), (8, 1): (0, -1), (8, 2): (0, -1), (8, 3): (0, -1), (8, 5): (0, -1), (8, 6): (0, -1), (8, 7): (0, -1), (9, 1): (0, -1), (9, 2): (0, -1), (9, 3): (0, -1), (9, 4): (0, -1), (9, 5): (0, -1), (9, 6): (0, -1), (9, 7): (0, -1), (10, 1): (0, -1), (10, 2): (0, -1), (10, 3): (0, -1), (10, 5): (0, -1), (10, 6): (0, -1), (10, 7): (0, -1), (11, 1): (0, -1), (11, 2): (0, -1), (11, 3): (0, -1), (11, 5): (0, -1), (11, 6): (0, -1), (11, 7): (0, -1)}, 'left': {(1, 1): (-1, 0), (1, 2): (-1, 0), (1, 4): (-1, 0), (1, 5): (-1, 0), (1, 6): (-1, 0), (1, 7): (-1, 0), (2, 1): (-1, 0), (2, 2): (-1, 0), (2, 4): (-1, 0), (2, 5): (-1, 0), (2, 6): (-1, 0), (2, 7): (-1, 0), (3, 1): (-1, 0), (3, 2): (-1, 0), (3, 3): (-1, 0), (3, 4): (-1, 0), (3, 5): (-1, 0), (3, 6): (-1, 0), (3, 7): (-1, 0), (4, 1): (-1, 0), (4, 2): (-1, 0), (4, 4): (-1, 0), (4, 5): (-1, 0), (4, 6): (-1, 0), (4, 7): (-1, 0), (5, 2): (-1, 0), (5, 6): (-1, 0), (6, 1): (-1, 0), (6, 2): (-1, 0), (6, 3): (-1, 0), (6, 5): (-1, 0), (6, 6): (-1, 0), (6, 7): (-1, 0), (7, 1): (-1, 0), (7, 2): (-1, 0), (7, 3): (-1, 0), (7, 5): (-1, 0), (7, 6): (-1, 0), (7, 7): (-1, 0), (8, 1): (-1, 0), (8, 2): (-1, 0), (8, 3): (-1, 0), (8, 5): (-1, 0), (8, 6): (-1, 0), (8, 7): (-1, 0), (9, 1): (-1, 0), (9, 2): (-1, 0), (9, 3): (-1, 0), (9, 4): (-1, 0), (9, 5): (-1, 0), (9, 6): (-1, 0), (9, 7): (-1, 0), (10, 1): (-1, 0), (10, 2): (-1, 0), (10, 3): (-1, 0), (10, 5): (-1, 0), (10, 6): (-1, 0), (10, 7): (-1, 0), (11, 1): (-1, 0), (11, 2): (-1, 0), (11, 3): (-1, 0), (11, 5): (-1, 0), (11, 6): (-1, 0), (11, 7): (-1, 0)}, 'right': {(1, 1): (1, 0), (1, 2): (1, 0), (1, 4): (1, 0), (1, 5): (1, 0), (1, 6): (1, 0), (1, 7): (1, 0), (2, 1): (1, 0), (2, 2): (1, 0), (2, 4): (1, 0), (2, 5): (1, 0), (2, 6): (1, 0), (2, 7): (1, 0), (3, 1): (1, 0), (3, 2): (1, 0), (3, 3): (1, 0), (3, 4): (1, 0), (3, 5): (1, 0), (3, 6): (1, 0), (3, 7): (1, 0), (4, 1): (1, 0), (4, 2): (1, 0), (4, 4): (1, 0), (4, 5): (1, 0), (4, 6): (1, 0), (4, 7): (1, 0), (5, 2): (1, 0), (5, 6): (1, 0), (6, 1): (1, 0), (6, 2): (1, 0), (6, 3): (1, 0), (6, 5): (1, 0), (6, 6): (1, 0), (6, 7): (1, 0), (7, 1): (1, 0), (7, 2): (1, 0), (7, 3): (1, 0), (7, 5): (1, 0), (7, 6): (1, 0), (7, 7): (1, 0), (8, 1): (1, 0), (8, 2): (1, 0), (8, 3): (1, 0), (8, 5): (1, 0), (8, 6): (1, 0), (8, 7): (1, 0), (9, 1): (1, 0), (9, 2): (1, 0), (9, 3): (1, 0), (9, 4): (1, 0), (9, 5): (1, 0), (9, 6): (1, 0), (9, 7): (1, 0), (10, 1): (1, 0), (10, 2): (1, 0), (10, 3): (1, 0), (10, 5): (1, 0), (10, 6): (1, 0), (10, 7): (1, 0), (11, 1): (1, 0), (11, 2): (1, 0), (11, 3): (1, 0), (11, 5): (1, 0), (11, 6): (1, 0), (11, 7): (1, 0)}}
		landmarkPolicies =  {'h1': {(1, 1): (0, 1), (1, 2): (1, 0), (2, 1): (0, 1), (2, 2): (1, 0), (3, 1): (0, 1), (3, 2): (0, 1), (4, 1): (0, 1), (4, 2): (-1, 0), (1, 4): (1, 0), (1, 5): (1, 0), (1, 6): (1, 0), (1, 7): (1, 0), (2, 4): (1, 0), (2, 5): (1, 0), (2, 6): (1, 0), (2, 7): (1, 0), (3, 4): (0, -1), (3, 5): (0, -1), (3, 6): (0, -1), (3, 7): (0, -1), (4, 4): (-1, 0), (4, 5): (0, -1), (4, 6): (0, -1), (4, 7): (0, -1), (3, 3): (1, 0)}, 'h2': {(1, 1): (0, 1), (1, 2): (1, 0), (2, 1): (0, 1), (2, 2): (1, 0), (3, 1): (0, 1), (3, 2): (1, 0), (4, 1): (0, 1), (4, 2): (1, 0), (6, 1): (0, 1), (6, 2): (-1, 0), (6, 3): (0, -1), (7, 1): (0, 1), (7, 2): (-1, 0), (7, 3): (0, -1), (8, 1): (0, 1), (8, 2): (-1, 0), (8, 3): (0, -1), (9, 1): (0, 1), (9, 2): (-1, 0), (9, 3): (0, -1), (10, 1): (0, 1), (10, 2): (-1, 0), (10, 3): (0, -1), (11, 1): (0, 1), (11, 2): (-1, 0), (11, 3): (0, -1), (5, 2): (0, 1)}, 'h3': {(1, 4): (0, 1), (1, 5): (0, 1), (1, 6): (1, 0), (1, 7): (1, 0), (2, 4): (0, 1), (2, 5): (0, 1), (2, 6): (1, 0), (2, 7): (1, 0), (3, 4): (0, 1), (3, 5): (0, 1), (3, 6): (1, 0), (3, 7): (1, 0), (4, 4): (0, 1), (4, 5): (0, 1), (4, 6): (1, 0), (4, 7): (0, -1), (6, 5): (0, 1), (6, 6): (-1, 0), (6, 7): (0, -1), (7, 5): (0, 1), (7, 6): (-1, 0), (7, 7): (0, -1), (8, 5): (0, 1), (8, 6): (-1, 0), (8, 7): (0, -1), (9, 5): (0, 1), (9, 6): (-1, 0), (9, 7): (0, -1), (10, 5): (0, 1), (10, 6): (-1, 0), (10, 7): (0, -1), (11, 5): (0, 1), (11, 6): (-1, 0), (11, 7): (0, -1), (5, 6): (0, 1)}, 'h4': {(6, 5): (1, 0), (6, 6): (1, 0), (6, 7): (1, 0), (7, 5): (1, 0), (7, 6): (1, 0), (7, 7): (1, 0), (8, 5): (1, 0), (8, 6): (1, 0), (8, 7): (1, 0), (9, 5): (0, -1), (9, 6): (0, -1), (9, 7): (0, -1), (10, 5): (-1, 0), (10, 6): (0, -1), (10, 7): (0, -1), (11, 5): (-1, 0), (11, 6): (0, -1), (11, 7): (0, -1), (6, 1): (0, 1), (6, 2): (0, 1), (6, 3): (1, 0), (7, 1): (0, 1), (7, 2): (0, 1), (7, 3): (1, 0), (8, 1): (0, 1), (8, 2): (0, 1), (8, 3): (1, 0), (9, 1): (0, 1), (9, 2): (0, 1), (9, 3): (0, 1), (10, 1): (0, 1), (10, 2): (0, 1), (10, 3): (-1, 0), (11, 1): (0, 1), (11, 2): (0, 1), (11, 3): (-1, 0), (9, 4): (1, 0)}}

		optionsDictionary = {'up': {(1, 1): (0, 1), (1, 2): (0, 1), (1, 4): (0, 1), (1, 5): (0, 1), (1, 6): (0, 1), (1, 7): (0, 1), (2, 1): (0, 1), (2, 2): (0, 1), (2, 4): (0, 1), (2, 5): (0, 1), (2, 6): (0, 1), (2, 7): (0, 1), (3, 1): (0, 1), (3, 2): (0, 1), (3, 3): (0, 1), (3, 4): (0, 1), (3, 5): (0, 1), (3, 6): (0, 1), (3, 7): (0, 1), (4, 1): (0, 1), (4, 2): (0, 1), (4, 4): (0, 1), (4, 5): (0, 1), (4, 6): (0, 1), (4, 7): (0, 1), (5, 2): (0, 1), (5, 6): (0, 1), (6, 1): (0, 1), (6, 2): (0, 1), (6, 3): (0, 1), (6, 5): (0, 1), (6, 6): (0, 1), (6, 7): (0, 1), (7, 1): (0, 1), (7, 2): (0, 1), (7, 3): (0, 1), (7, 5): (0, 1), (7, 6): (0, 1), (7, 7): (0, 1), (8, 1): (0, 1), (8, 2): (0, 1), (8, 3): (0, 1), (8, 5): (0, 1), (8, 6): (0, 1), (8, 7): (0, 1), (9, 1): (0, 1), (9, 2): (0, 1), (9, 3): (0, 1), (9, 4): (0, 1), (9, 5): (0, 1), (9, 6): (0, 1), (9, 7): (0, 1), (10, 1): (0, 1), (10, 2): (0, 1), (10, 3): (0, 1), (10, 5): (0, 1), (10, 6): (0, 1), (10, 7): (0, 1), (11, 1): (0, 1), (11, 2): (0, 1), (11, 3): (0, 1), (11, 5): (0, 1), (11, 6): (0, 1), (11, 7): (0, 1)}, 'down': {(1, 1): (0, -1), (1, 2): (0, -1), (1, 4): (0, -1), (1, 5): (0, -1), (1, 6): (0, -1), (1, 7): (0, -1), (2, 1): (0, -1), (2, 2): (0, -1), (2, 4): (0, -1), (2, 5): (0, -1), (2, 6): (0, -1), (2, 7): (0, -1), (3, 1): (0, -1), (3, 2): (0, -1), (3, 3): (0, -1), (3, 4): (0, -1), (3, 5): (0, -1), (3, 6): (0, -1), (3, 7): (0, -1), (4, 1): (0, -1), (4, 2): (0, -1), (4, 4): (0, -1), (4, 5): (0, -1), (4, 6): (0, -1), (4, 7): (0, -1), (5, 2): (0, -1), (5, 6): (0, -1), (6, 1): (0, -1), (6, 2): (0, -1), (6, 3): (0, -1), (6, 5): (0, -1), (6, 6): (0, -1), (6, 7): (0, -1), (7, 1): (0, -1), (7, 2): (0, -1), (7, 3): (0, -1), (7, 5): (0, -1), (7, 6): (0, -1), (7, 7): (0, -1), (8, 1): (0, -1), (8, 2): (0, -1), (8, 3): (0, -1), (8, 5): (0, -1), (8, 6): (0, -1), (8, 7): (0, -1), (9, 1): (0, -1), (9, 2): (0, -1), (9, 3): (0, -1), (9, 4): (0, -1), (9, 5): (0, -1), (9, 6): (0, -1), (9, 7): (0, -1), (10, 1): (0, -1), (10, 2): (0, -1), (10, 3): (0, -1), (10, 5): (0, -1), (10, 6): (0, -1), (10, 7): (0, -1), (11, 1): (0, -1), (11, 2): (0, -1), (11, 3): (0, -1), (11, 5): (0, -1), (11, 6): (0, -1), (11, 7): (0, -1)}, 'left': {(1, 1): (-1, 0), (1, 2): (-1, 0), (1, 4): (-1, 0), (1, 5): (-1, 0), (1, 6): (-1, 0), (1, 7): (-1, 0), (2, 1): (-1, 0), (2, 2): (-1, 0), (2, 4): (-1, 0), (2, 5): (-1, 0), (2, 6): (-1, 0), (2, 7): (-1, 0), (3, 1): (-1, 0), (3, 2): (-1, 0), (3, 3): (-1, 0), (3, 4): (-1, 0), (3, 5): (-1, 0), (3, 6): (-1, 0), (3, 7): (-1, 0), (4, 1): (-1, 0), (4, 2): (-1, 0), (4, 4): (-1, 0), (4, 5): (-1, 0), (4, 6): (-1, 0), (4, 7): (-1, 0), (5, 2): (-1, 0), (5, 6): (-1, 0), (6, 1): (-1, 0), (6, 2): (-1, 0), (6, 3): (-1, 0), (6, 5): (-1, 0), (6, 6): (-1, 0), (6, 7): (-1, 0), (7, 1): (-1, 0), (7, 2): (-1, 0), (7, 3): (-1, 0), (7, 5): (-1, 0), (7, 6): (-1, 0), (7, 7): (-1, 0), (8, 1): (-1, 0), (8, 2): (-1, 0), (8, 3): (-1, 0), (8, 5): (-1, 0), (8, 6): (-1, 0), (8, 7): (-1, 0), (9, 1): (-1, 0), (9, 2): (-1, 0), (9, 3): (-1, 0), (9, 4): (-1, 0), (9, 5): (-1, 0), (9, 6): (-1, 0), (9, 7): (-1, 0), (10, 1): (-1, 0), (10, 2): (-1, 0), (10, 3): (-1, 0), (10, 5): (-1, 0), (10, 6): (-1, 0), (10, 7): (-1, 0), (11, 1): (-1, 0), (11, 2): (-1, 0), (11, 3): (-1, 0), (11, 5): (-1, 0), (11, 6): (-1, 0), (11, 7): (-1, 0)}, 'right': {(1, 1): (1, 0), (1, 2): (1, 0), (1, 4): (1, 0), (1, 5): (1, 0), (1, 6): (1, 0), (1, 7): (1, 0), (2, 1): (1, 0), (2, 2): (1, 0), (2, 4): (1, 0), (2, 5): (1, 0), (2, 6): (1, 0), (2, 7): (1, 0), (3, 1): (1, 0), (3, 2): (1, 0), (3, 3): (1, 0), (3, 4): (1, 0), (3, 5): (1, 0), (3, 6): (1, 0), (3, 7): (1, 0), (4, 1): (1, 0), (4, 2): (1, 0), (4, 4): (1, 0), (4, 5): (1, 0), (4, 6): (1, 0), (4, 7): (1, 0), (5, 2): (1, 0), (5, 6): (1, 0), (6, 1): (1, 0), (6, 2): (1, 0), (6, 3): (1, 0), (6, 5): (1, 0), (6, 6): (1, 0), (6, 7): (1, 0), (7, 1): (1, 0), (7, 2): (1, 0), (7, 3): (1, 0), (7, 5): (1, 0), (7, 6): (1, 0), (7, 7): (1, 0), (8, 1): (1, 0), (8, 2): (1, 0), (8, 3): (1, 0), (8, 5): (1, 0), (8, 6): (1, 0), (8, 7): (1, 0), (9, 1): (1, 0), (9, 2): (1, 0), (9, 3): (1, 0), (9, 4): (1, 0), (9, 5): (1, 0), (9, 6): (1, 0), (9, 7): (1, 0), (10, 1): (1, 0), (10, 2): (1, 0), (10, 3): (1, 0), (10, 5): (1, 0), (10, 6): (1, 0), (10, 7): (1, 0), (11, 1): (1, 0), (11, 2): (1, 0), (11, 3): (1, 0), (11, 5): (1, 0), (11, 6): (1, 0), (11, 7): (1, 0)}, 'h1': {(1, 1): (0, 1), (1, 2): (1, 0), (2, 1): (0, 1), (2, 2): (1, 0), (3, 1): (0, 1), (3, 2): (0, 1), (4, 1): (0, 1), (4, 2): (-1, 0), (1, 4): (1, 0), (1, 5): (1, 0), (1, 6): (1, 0), (1, 7): (1, 0), (2, 4): (1, 0), (2, 5): (1, 0), (2, 6): (1, 0), (2, 7): (1, 0), (3, 4): (0, -1), (3, 5): (0, -1), (3, 6): (0, -1), (3, 7): (0, -1), (4, 4): (-1, 0), (4, 5): (0, -1), (4, 6): (0, -1), (4, 7): (0, -1), (3, 3): (1, 0)}, 'h2': {(1, 1): (0, 1), (1, 2): (1, 0), (2, 1): (0, 1), (2, 2): (1, 0), (3, 1): (0, 1), (3, 2): (1, 0), (4, 1): (0, 1), (4, 2): (1, 0), (6, 1): (0, 1), (6, 2): (-1, 0), (6, 3): (0, -1), (7, 1): (0, 1), (7, 2): (-1, 0), (7, 3): (0, -1), (8, 1): (0, 1), (8, 2): (-1, 0), (8, 3): (0, -1), (9, 1): (0, 1), (9, 2): (-1, 0), (9, 3): (0, -1), (10, 1): (0, 1), (10, 2): (-1, 0), (10, 3): (0, -1), (11, 1): (0, 1), (11, 2): (-1, 0), (11, 3): (0, -1), (5, 2): (0, 1)}, 'h3': {(1, 4): (0, 1), (1, 5): (0, 1), (1, 6): (1, 0), (1, 7): (1, 0), (2, 4): (0, 1), (2, 5): (0, 1), (2, 6): (1, 0), (2, 7): (1, 0), (3, 4): (0, 1), (3, 5): (0, 1), (3, 6): (1, 0), (3, 7): (1, 0), (4, 4): (0, 1), (4, 5): (0, 1), (4, 6): (1, 0), (4, 7): (0, -1), (6, 5): (0, 1), (6, 6): (-1, 0), (6, 7): (0, -1), (7, 5): (0, 1), (7, 6): (-1, 0), (7, 7): (0, -1), (8, 5): (0, 1), (8, 6): (-1, 0), (8, 7): (0, -1), (9, 5): (0, 1), (9, 6): (-1, 0), (9, 7): (0, -1), (10, 5): (0, 1), (10, 6): (-1, 0), (10, 7): (0, -1), (11, 5): (0, 1), (11, 6): (-1, 0), (11, 7): (0, -1), (5, 6): (0, 1)}, 'h4': {(6, 5): (1, 0), (6, 6): (1, 0), (6, 7): (1, 0), (7, 5): (1, 0), (7, 6): (1, 0), (7, 7): (1, 0), (8, 5): (1, 0), (8, 6): (1, 0), (8, 7): (1, 0), (9, 5): (0, -1), (9, 6): (0, -1), (9, 7): (0, -1), (10, 5): (-1, 0), (10, 6): (0, -1), (10, 7): (0, -1), (11, 5): (-1, 0), (11, 6): (0, -1), (11, 7): (0, -1), (6, 1): (0, 1), (6, 2): (0, 1), (6, 3): (1, 0), (7, 1): (0, 1), (7, 2): (0, 1), (7, 3): (1, 0), (8, 1): (0, 1), (8, 2): (0, 1), (8, 3): (1, 0), (9, 1): (0, 1), (9, 2): (0, 1), (9, 3): (0, 1), (10, 1): (0, 1), (10, 2): (0, 1), (10, 3): (-1, 0), (11, 1): (0, 1), (11, 2): (0, 1), (11, 3): (-1, 0), (9, 4): (1, 0)}}

		availableOptionsAtState = {(1, 1): ['up', 'down', 'left', 'right', 'h1', 'h2'], (1, 2): ['up', 'down', 'left', 'right', 'h1', 'h2'], (1, 4): ['up', 'down', 'left', 'right', 'h1', 'h3'], (1, 5): ['up', 'down', 'left', 'right', 'h1', 'h3'], (1, 6): ['up', 'down', 'left', 'right', 'h1', 'h3'], (1, 7): ['up', 'down', 'left', 'right', 'h1', 'h3'], (2, 1): ['up', 'down', 'left', 'right', 'h1', 'h2'], (2, 2): ['up', 'down', 'left', 'right', 'h1', 'h2'], (2, 4): ['up', 'down', 'left', 'right', 'h1', 'h3'], (2, 5): ['up', 'down', 'left', 'right', 'h1', 'h3'], (2, 6): ['up', 'down', 'left', 'right', 'h1', 'h3'], (2, 7): ['up', 'down', 'left', 'right', 'h1', 'h3'], (3, 1): ['up', 'down', 'left', 'right', 'h1', 'h2'], (3, 2): ['up', 'down', 'left', 'right', 'h1', 'h2'], (3, 3): ['up', 'down', 'left', 'right', 'h1'], (3, 4): ['up', 'down', 'left', 'right', 'h1', 'h3'], (3, 5): ['up', 'down', 'left', 'right', 'h1', 'h3'], (3, 6): ['up', 'down', 'left', 'right', 'h1', 'h3'], (3, 7): ['up', 'down', 'left', 'right', 'h1', 'h3'], (4, 1): ['up', 'down', 'left', 'right', 'h1', 'h2'], (4, 2): ['up', 'down', 'left', 'right', 'h1', 'h2'], (4, 4): ['up', 'down', 'left', 'right', 'h1', 'h3'], (4, 5): ['up', 'down', 'left', 'right', 'h1', 'h3'], (4, 6): ['up', 'down', 'left', 'right', 'h1', 'h3'], (4, 7): ['up', 'down', 'left', 'right', 'h1', 'h3'], (5, 2): ['up', 'down', 'left', 'right', 'h2'], (5, 6): ['up', 'down', 'left', 'right', 'h3'], (6, 1): ['up', 'down', 'left', 'right', 'h2', 'h4'], (6, 2): ['up', 'down', 'left', 'right', 'h2', 'h4'], (6, 3): ['up', 'down', 'left', 'right', 'h2', 'h4'], (6, 5): ['up', 'down', 'left', 'right', 'h3', 'h4'], (6, 6): ['up', 'down', 'left', 'right', 'h3', 'h4'], (6, 7): ['up', 'down', 'left', 'right', 'h3', 'h4'], (7, 1): ['up', 'down', 'left', 'right', 'h2', 'h4'], (7, 2): ['up', 'down', 'left', 'right', 'h2', 'h4'], (7, 3): ['up', 'down', 'left', 'right', 'h2', 'h4'], (7, 5): ['up', 'down', 'left', 'right', 'h3', 'h4'], (7, 6): ['up', 'down', 'left', 'right', 'h3', 'h4'], (7, 7): ['up', 'down', 'left', 'right', 'h3', 'h4'], (8, 1): ['up', 'down', 'left', 'right', 'h2', 'h4'], (8, 2): ['up', 'down', 'left', 'right', 'h2', 'h4'], (8, 3): ['up', 'down', 'left', 'right', 'h2', 'h4'], (8, 5): ['up', 'down', 'left', 'right', 'h3', 'h4'], (8, 6): ['up', 'down', 'left', 'right', 'h3', 'h4'], (8, 7): ['up', 'down', 'left', 'right', 'h3', 'h4'], (9, 1): ['up', 'down', 'left', 'right', 'h2', 'h4'], (9, 2): ['up', 'down', 'left', 'right', 'h2', 'h4'], (9, 3): ['up', 'down', 'left', 'right', 'h2', 'h4'], (9, 4): ['up', 'down', 'left', 'right', 'h4'], (9, 5): ['up', 'down', 'left', 'right', 'h3', 'h4'], (9, 6): ['up', 'down', 'left', 'right', 'h3', 'h4'], (9, 7): ['up', 'down', 'left', 'right', 'h3', 'h4'], (10, 1): ['up', 'down', 'left', 'right', 'h2', 'h4'], (10, 2): ['up', 'down', 'left', 'right', 'h2', 'h4'], (10, 3): ['up', 'down', 'left', 'right', 'h2', 'h4'], (10, 5): ['up', 'down', 'left', 'right', 'h3', 'h4'], (10, 6): ['up', 'down', 'left', 'right', 'h3', 'h4'], (10, 7): ['up', 'down', 'left', 'right', 'h3', 'h4'], (11, 1): ['up', 'down', 'left', 'right', 'h2', 'h4'], (11, 2): ['up', 'down', 'left', 'right', 'h2', 'h4'], (11, 3): ['up', 'down', 'left', 'right', 'h2', 'h4'], (11, 5): ['up', 'down', 'left', 'right', 'h3', 'h4'], (11, 6): ['up', 'down', 'left', 'right', 'h3', 'h4'], (11, 7): ['up', 'down', 'left', 'right', 'h3', 'h4']}

		V = {state: 0 for state in stateSet}
		convergenceTolerance = .000001
		gamma = .9

		getMaxValue = targetCode.getMaxValue
		getNextState = targetCode.transition.getNextState

		actionCost = -1
		moveCost = -3
		goalReward = 10
		goalStates = [(9,2)]
		landmarkTerminations = {"h1": (3,3), "h2": (5,2), "h3": (5,6), "h4": (9,4)}
		
		getLandmarkReward = targetCode.reward.getLandmarkOptionReward(stateSet, actionCost, moveCost, goalStates, goalReward, getNextState)
		getPrimitiveReward = targetCode.reward.getPrimitiveOptionReward(stateSet, actionCost, moveCost, goalStates, goalReward, getNextState)

		getPrimitiveExpectedValue = targetCode.getPrimitiveExpectedValue(gamma, primitivePolicies, getNextState, getPrimitiveReward, stateSet)
		getLandmarkExpectedValue = targetCode.getLandmarkExpectedValue(gamma, landmarkPolicies, landmarkTerminations, getLandmarkReward)
		
		optionType = {"up": "primitive", "down": "primitive", "left": "primitive", "right": "primitive", "h1": "landmark", "h2": "landmark", "h3": "landmark", "h4": "landmark"}

		getExpectedValue = targetCode.getExpectedValue(optionType, getPrimitiveExpectedValue, getLandmarkExpectedValue)
		
		valueIterationSetUp = targetCode.optionValueIteration(stateSet, optionsDictionary, availableOptionsAtState, V, convergenceTolerance, gamma, getMaxValue, getNextState, getExpectedValue)
		result = valueIterationSetUp()
		self.policy = result[1]

	#when the agent is in the same room as the goalstate
	@data(((8,2), "right"), ((10,2), "left"), ((9,3), "down"), ((9,1), "up"), ((6,2), "right"))
	@unpack
	def test_SameRoomPolicy(self, state, expectedOption):
		self.assertEqual(self.policy[state], expectedOption)

	#when agent is in a room adjacent to the goalstate
	#test case #1 (4,2) --> option 'right' and 'h2' result with the same overall cost
	@data(((4,2), "right"), ((3,1), "h2"), ((7,6), "h4"), ((10,6), "h4"))
	@unpack
	def test_AdjacentRoomPolicy(self, state, expectedOption):
		self.assertEqual(self.policy[state], expectedOption)

	#code good until here
	#when agent is farther than 1 room away from the agent
	@data(((3,4), "h3"), ((2,6), "h3")) 
	@unpack
	def test_FarRoomPolicy(self, state, expectedOption):
		self.assertEqual(self.policy[state], expectedOption)

	def tearDown(self):
		pass

if __name__ == '__main__':
	unittest.main(verbosity=2)
________________	
		
		
#testing general functions
@ddt
class TestGetMaxValue(unittest.TestCase):
	def setUp(self):
		self.getMaxValue = targetCode.getMaxValue

	@data(({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}, "e"), ( {"a": 1, "b": 5, "c": 3, "d": 4, "e": 5}, "b"), ({"a": 101, "b": 2, "c": 103.5, "d": 4, "e": 5}, "c"), ({"a": 10, "b": 2013, "c": 32041, "d": 420314, "e": 5}, "d"))
	@unpack
	def test_GetDictionaryMaxValue(self, dictionary, expectedKey):
		self.assertEqual(self.getMaxValue(dictionary), expectedKey)

	def tearDown(self):
		pass

#testing helper classes used to obtain Q value
@ddt
class TestPrimitiveExpectedValue(unittest.TestCase):
	def setUp(self):
		stateSet = [(i,j) for i in range(2) for j in range(2)]
		actionCost = -1
		moveCost = -3
		goalReward = 10
		goalStates = [(0,0)]
		
		getNextState = targetCode.transition.getNextState

		getPrimitiveReward = targetCode.reward.getPrimitiveOptionReward(stateSet, actionCost, moveCost, goalStates, goalReward, getNextState)

		gamma = 0.9
		optionPolicies = {'up': {(0, 0): (0, 1), (0, 1): (0, 1), (1, 0): (0, 1), (1, 1): (0, 1)}, 'down': {(0, 0): (0, -1), (0, 1): (0, -1), (1, 0): (0, -1), (1, 1): (0, -1)}, 'left': {(0, 0): (-1, 0), (0, 1): (-1, 0), (1, 0): (-1, 0), (1, 1): (-1, 0)}, 'right': {(0, 0): (1, 0), (0, 1): (1, 0), (1, 0): (1, 0), (1, 1): (1, 0)}}

		self.getPrimitiveExpectedValue = targetCode.getPrimitiveExpectedValue(gamma, optionPolicies, getNextState, getPrimitiveReward, stateSet)
		self.V = {state: 0 for state in stateSet}

	#rewardExpectedValue = termination at goal state (0,0)
	@data(((0,0), "down", 6), ((1,0), "left", 6), ((0,1), "down", 6))
	@unpack
	def test_RewardExpectedValue(self, state, option, expectedValue):
		self.assertEqual(self.getPrimitiveExpectedValue(state, option, self.V), expectedValue)

	@data(((0,0), "right", -4), ((1,1), "right", -4), ((1,0), "up", -4))
	@unpack
	def test_nonRewardExpectedValue(self, state, option, expectedValue):
		self.assertEqual(self.getPrimitiveExpectedValue(state, option, self.V), expectedValue)

	def tearDown(self):
		pass

@ddt 
class TestLandmarkExpectedValue(unittest.TestCase):
	def setUp(self):
		stateSet = [(i,j) for i in range(2) for j in range(2)]
		actionCost = -1
		moveCost = -3
		goalReward = 10
		goalStates = [(0,0)]
		getNextState = targetCode.transition.getNextState

		getLandmarkReward = targetCode.reward.getLandmarkOptionReward(stateSet, actionCost, moveCost, goalStates, goalReward, getNextState)

		gamma = 0.9
		optionPolicies = {'LL': {(0, 0): (0, -1), (0, 1): (0, -1), (1, 0): (-1, 0), (1, 1): (0, -1)}, 'UL': {(0, 0): (0, 1), (0, 1): (0, 1), (1, 0): (0, 1), (1, 1): (-1, 0)}, 'LR': {(0, 0): (1, 0), (0, 1): (1, 0), (1, 0): (0, -1), (1, 1): (0, -1)}, 'UR': {(0, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, 1), (1, 1): (0, 1)}}
		optionTerminations = {'LL': (0, 0), 'UL': (0, 1), 'LR': (1, 0), 'UR': (1, 1)}

		self.getLandmarkExpectedValue = targetCode.getLandmarkExpectedValue(gamma, optionPolicies, optionTerminations, getLandmarkReward)
		self.V = {state: 0 for state in stateSet}

	#rewardExpectedValue = termination at goal state (0,0)
	@data(((1,0), "LL", 6), ((0,0), "LL", 7), ((1,1), "LL", 5))
	@unpack
	def test_RewardExpectedValue(self, state, option, expectedValue):
		self.assertEqual(self.getLandmarkExpectedValue(state, option, self.V), expectedValue)

	@data(((0,0), "UR", -5), ((1,0), "LR", -3), ((1,1), "LR", -4))
	@unpack
	def test_nonRewardExpectedValue(self, state, option, expectedValue):
		self.assertEqual(self.getLandmarkExpectedValue(state, option, self.V), expectedValue)

	def tearDown(self):
		pass

@ddt
class TestGetExpectedValue(unittest.TestCase):
	def setUp(self):
		stateSet = [(i,j) for i in range(2) for j in range(2)]
		actionCost = -1
		moveCost = -3
		goalReward = 10
		goalStates = [(0,0)]
		getNextState = targetCode.transition.getNextState

		getLandmarkReward = targetCode.reward.getLandmarkOptionReward(stateSet, actionCost, moveCost, goalStates, goalReward, getNextState)
		getPrimitiveReward = targetCode.reward.getPrimitiveOptionReward(stateSet, actionCost, moveCost, goalStates, goalReward, getNextState)

		gamma = 0.9
		primitivePolicies = {'up': {(0, 0): (0, 1), (0, 1): (0, 1), (1, 0): (0, 1), (1, 1): (0, 1)}, 'down': {(0, 0): (0, -1), (0, 1): (0, -1), (1, 0): (0, -1), (1, 1): (0, -1)}, 'left': {(0, 0): (-1, 0), (0, 1): (-1, 0), (1, 0): (-1, 0), (1, 1): (-1, 0)}, 'right': {(0, 0): (1, 0), (0, 1): (1, 0), (1, 0): (1, 0), (1, 1): (1, 0)}}
		landmarkPolicies = {'LL': {(0, 0): (0, -1), (0, 1): (0, -1), (1, 0): (-1, 0), (1, 1): (0, -1)}, 'UL': {(0, 0): (0, 1), (0, 1): (0, 1), (1, 0): (0, 1), (1, 1): (-1, 0)}, 'LR': {(0, 0): (1, 0), (0, 1): (1, 0), (1, 0): (0, -1), (1, 1): (0, -1)}, 'UR': {(0, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, 1), (1, 1): (0, 1)}}
		landmarkTerminations = {'LL': (0, 0), 'UL': (0, 1), 'LR': (1, 0), 'UR': (1, 1)}

		getPrimitiveExpectedValue = targetCode.getPrimitiveExpectedValue(gamma, primitivePolicies, getNextState, getPrimitiveReward, stateSet)
		getLandmarkExpectedValue = targetCode.getLandmarkExpectedValue(gamma, landmarkPolicies, landmarkTerminations, getLandmarkReward)
		self.V = {state: 0 for state in stateSet}

		optionType = {"up": "primitive", "down": "primitive", "left": "primitive", "right": "primitive", "LL": "landmark", "UL": "landmark", "LR": "landmark", "UR": "landmark"}

		self.getExpectedValue = targetCode.getExpectedValue(optionType, getPrimitiveExpectedValue, getLandmarkExpectedValue)

	@data(((0,0), "down", 6), ((1,0), "left", 6), ((0,1), "down", 6))
	@unpack
	def test_PrimitiveReward(self, state, option, expectedValue):
		self.assertEqual(self.getExpectedValue(state, option, self.V), expectedValue)

	@data(((0,0), "right", -4), ((1,1), "right", -4), ((1,0), "up", -4))
	@unpack
	def test_PrimitiveNonReward(self, state, option, expectedValue):
		self.assertEqual(self.getExpectedValue(state, option, self.V), expectedValue)

	@data(((1,0), "LL", 6), ((0,0), "LL", 7), ((1,1), "LL", 5))
	@unpack
	def test_LandmarkReward(self, state, option, expectedValue):
		self.assertEqual(self.getExpectedValue(state, option, self.V), expectedValue)

	@data(((0,0), "UR", -5), ((1,0), "LR", -3), ((1,1), "LR", -4))
	@unpack
	def test_LandmarkNonReward(self, state, option, expectedValue):
		self.assertEqual(self.getExpectedValue(state, option, self.V), expectedValue)

	def tearDown(self):
		pass

