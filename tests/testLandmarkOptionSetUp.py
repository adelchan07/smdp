"""
Created on Thu Sep 3 9:14:23 2020

@author: adelphachan

testLandmarkOptionSetUp.py

getLandmarkPolicy and getLandmarkReward classes tested on a simple 2x2 grid
setUpLandmark class tested on 13x9 grid with hallways and outer border

class of test cases for each class present in landmarkOptionSetUp.py
merge function tested in testPrimitiveOptions.py
"""

import sys
sys.path.append('../setUp/')

import numpy as np
import unittest
from ddt import ddt, data, unpack
import landmarkOptionSetUp as targetCode #change to file name

@ddt
class TestGetTransitionTable(unittest.TestCase):
	def setUp(self):
		actionSet = [(0,1), (0,-1), (1,0), (-1,0)]
		setUp = targetCode.getTransitionTable(actionSet)

		stateSet = [(i,j) for i in range(2) for j in range(2)]
		self.transitionTable = setUp(stateSet)

@data(((0,0), (-1,0), (0,0)), ((1,1), (0,1), (1,1)), ((1,0), (1,0), (1,0)))
@unpack
def test_BoundaryLocations(self, state, action, expectedNextState):
	self.assertEqual(self.transitionTable[state][action], {expectedNextState: 1})

@data(((0,0), (1,0), (1,0)), ((1,1), (0,-1), (1,0)), ((1,0), (0,1), (1,1)))
@unpack
def test_InnerLocations(self, state, action, expectedNextState):
	self.assertEqual(self.transitionTable[state][action], {expectedNextState: 1})

def tearDown(self):
	pass


@ddt 
class TestGetLandmarkReward(unittest.TestCase):
	def setUp(self):

		actionSet = [(0,-1), (1,0), (-1,0), (0,1)]
		actionCost = -1
		goalReward = 10

		goal1 = (0,0)
		goal2 = (0,1)
		goal3 = (1,0)
		goal4 = (1,1)

		setUp = targetCode.getLandmarkRewardTable(actionSet, actionCost, goalReward)

		transitionTable = {(0, 0): {(0, 1): {(0, 1): 1}, (0, -1): {(0, 0): 1}, (1, 0): {(1, 0): 1}, (-1, 0): {(0, 0): 1}}, (0, 1): {(0, 1): {(0, 1): 1}, (0, -1): {(0, 0): 1}, (1, 0): {(1, 1): 1}, (-1, 0): {(0, 1): 1}}, (1, 0): {(0, 1): {(1, 1): 1}, (0, -1): {(1, 0): 1}, (1, 0): {(1, 0): 1}, (-1, 0): {(0, 0): 1}}, (1, 1): {(0, 1): {(1, 1): 1}, (0, -1): {(1, 0): 1}, (1, 0): {(1, 1): 1}, (-1, 0): {(0, 1): 1}}}
		
		self.reward1 = setUp(transitionTable, goal1)
		self.reward2 = setUp(transitionTable, goal2)
		self.reward3 = setUp(transitionTable, goal3)
		self.reward4 = setUp(transitionTable, goal4)

	@data(((0,0), (0,1), (0,1), -1), ((1,0), (0,1), (1,1), -1), ((1,0), (-1,0), (0,0), 10))
	@unpack
	def test_RewardGoal1(self, state, action, nextState, expectedReward):
		self.assertEqual(self.reward1[state][action][nextState], expectedReward)

	@data(((0,0), (0,1), (0,1), 10), ((1,0), (0,1), (1,1), -1), ((1,0), (-1,0), (0,0), -1))
	@unpack
	def test_RewardGoal2(self, state, action, nextState, expectedReward):
		self.assertEqual(self.reward2[state][action][nextState], expectedReward)

	@data(((0,0), (0,1), (0,1), -1), ((1,0), (1,0), (1,0), 10), ((1,0), (-1,0), (0,0), -1))
	@unpack
	def test_RewardGoal3(self, state, action, nextState, expectedReward):
		self.assertEqual(self.reward3[state][action][nextState], expectedReward)

	@data(((0,0), (0,1), (0,1), -1), ((1,0), (0,1), (1,1), 10), ((1,0), (-1,0), (0,0), -1))
	@unpack
	def test_RewardGoal4(self, state, action, nextState, expectedReward):
		self.assertEqual(self.reward4[state][action][nextState], expectedReward)

	def tearDown(self):
		pass

@ddt 
class TestGetLandmarkPolicy(unittest.TestCase):
	def setUp(self):

		stateSet = [(0,0), (1,0), (1,1), (0,1)]
		V = {state: 0 for state in stateSet}
		convergenceTolerance = .000001
		gamma = .9

		setUp = targetCode.getLandmarkPolicy(V, convergenceTolerance, gamma)
		
		transitionTable = {(0, 0): {(0, 1): {(0, 1): 1}, (0, -1): {(0, 0): 1}, (1, 0): {(1, 0): 1}, (-1, 0): {(0, 0): 1}}, (0, 1): {(0, 1): {(0, 1): 1}, (0, -1): {(0, 0): 1}, (1, 0): {(1, 1): 1}, (-1, 0): {(0, 1): 1}}, (1, 0): {(0, 1): {(1, 1): 1}, (0, -1): {(1, 0): 1}, (1, 0): {(1, 0): 1}, (-1, 0): {(0, 0): 1}}, (1, 1): {(0, 1): {(1, 1): 1}, (0, -1): {(1, 0): 1}, (1, 0): {(1, 1): 1}, (-1, 0): {(0, 1): 1}}}
		
		#LL = (0,0), UR = (1,1)
		rewardTableLL =  {(0, 0): {(0, 1): {(0, 1): -1}, (0, -1): {(0, 0): 10}, (1, 0): {(1, 0): -1}, (-1, 0): {(0, 0): 10}}, (0, 1): {(0, 1): {(0, 1): -1}, (0, -1): {(0, 0): 10}, (1, 0): {(1, 1): -1}, (-1, 0): {(0, 1): -1}}, (1, 0): {(0, 1): {(1, 1): -1}, (0, -1): {(1, 0): -1}, (1, 0): {(1, 0): -1}, (-1, 0): {(0, 0): 10}}, (1, 1): {(0, 1): {(1, 1): -1}, (0, -1): {(1, 0): -1}, (1, 0): {(1, 1): -1}, (-1, 0): {(0, 1): -1}}}
		rewardTableUR = {(0, 0): {(0, 1): {(0, 1): -1}, (0, -1): {(0, 0): -1}, (1, 0): {(1, 0): -1}, (-1, 0): {(0, 0): -1}}, (0, 1): {(0, 1): {(0, 1): -1}, (0, -1): {(0, 0): -1}, (1, 0): {(1, 1): 10}, (-1, 0): {(0, 1): -1}}, (1, 0): {(0, 1): {(1, 1): 10}, (0, -1): {(1, 0): -1}, (1, 0): {(1, 0): -1}, (-1, 0): {(0, 0): -1}}, (1, 1): {(0, 1): {(1, 1): 10}, (0, -1): {(1, 0): -1}, (1, 0): {(1, 1): 10}, (-1, 0): {(0, 1): -1}}}

		self.policyLL = setUp(transitionTable, rewardTableLL)
		self.policyUR = setUp(transitionTable, rewardTableUR)

	@data(((0,0), (0,-1)), ((1,1), (0,-1)), ((1,0), (-1,0)))
	@unpack
	def test_LandmarkRewardLL(self, state, expectedAction):
		self.assertEqual(self.policyLL[state], expectedAction)

	@data(((0,0), (0,1)), ((1,1), (0,1)), ((1,0), (0,1)))
	@unpack
	def test_LandmarkRewardUR(self, state, expectedAction):
		self.assertEqual(self.policyUR[state], expectedAction)

	def tearDown(self):
		pass


@ddt
class TestLandmarkOptions(unittest.TestCase):
	def setUp(self): 

		landmarkLocation = {"h1": (3,3), "h2": (5,2), "h3": (5,6), "h4": (9,4)}
		landmarkStateSet = {'h1': [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2), (4, 1), (4, 2), (1, 4), (1, 5), (1, 6), (1, 7), (2, 4), (2, 5), (2, 6), (2, 7), (3, 4), (3, 5), (3, 6), (3, 7), (4, 4), (4, 5), (4, 6), (4, 7), (3, 3)], 'h2': [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2), (4, 1), (4, 2), (6, 1), (6, 2), (6, 3), (7, 1), (7, 2), (7, 3), (8, 1), (8, 2), (8, 3), (9, 1), (9, 2), (9, 3), (10, 1), (10, 2), (10, 3), (11, 1), (11, 2), (11, 3), (5, 2)], 'h3': [(1, 4), (1, 5), (1, 6), (1, 7), (2, 4), (2, 5), (2, 6), (2, 7), (3, 4), (3, 5), (3, 6), (3, 7), (4, 4), (4, 5), (4, 6), (4, 7), (6, 5), (6, 6), (6, 7), (7, 5), (7, 6), (7, 7), (8, 5), (8, 6), (8, 7), (9, 5), (9, 6), (9, 7), (10, 5), (10, 6), (10, 7), (11, 5), (11, 6), (11, 7), (5, 6)], 'h4': [(6, 5), (6, 6), (6, 7), (7, 5), (7, 6), (7, 7), (8, 5), (8, 6), (8, 7), (9, 5), (9, 6), (9, 7), (10, 5), (10, 6), (10, 7), (11, 5), (11, 6), (11, 7), (6, 1), (6, 2), (6, 3), (7, 1), (7, 2), (7, 3), (8, 1), (8, 2), (8, 3), (9, 1), (9, 2), (9, 3), (10, 1), (10, 2), (10, 3), (11, 1), (11, 2), (11, 3), (9, 4)]}
		
		actionSet = [(0,1), (0,-1), (1,0), (-1,0)]
		getTransitionTable = targetCode.getTransitionTable(actionSet)

		actionCost = -1
		goalReward = 10
		getLandmarkReward = targetCode.getLandmarkRewardTable(actionSet, actionCost, goalReward)

		#overall full 13x9 grid w/ outer boundary and inner hallways
		#blockList = [(5, 1), (1, 3), (2, 3), (4, 3), (5, 3), (5, 4), (6, 4), (7, 4), (8, 4), (10, 4), (11, 4), (5, 5), (5, 7), (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (12, 0), (12, 1), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (9, 8), (10, 8), (11, 8)]
		stateSet = [(1, 1), (1, 2), (1, 4), (1, 5), (1, 6), (1, 7), (2, 1), (2, 2), (2, 4), (2, 5), (2, 6), (2, 7), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (4, 1), (4, 2), (4, 4), (4, 5), (4, 6), (4, 7), (5, 2), (5, 6), (6, 1), (6, 2), (6, 3), (6, 5), (6, 6), (6, 7), (7, 1), (7, 2), (7, 3), (7, 5), (7, 6), (7, 7), (8, 1), (8, 2), (8, 3), (8, 5), (8, 6), (8, 7), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (10, 1), (10, 2), (10, 3), (10, 5), (10, 6), (10, 7), (11, 1), (11, 2), (11, 3), (11, 5), (11, 6), (11, 7)]
		V = {state: 0 for state in stateSet}
		convergenceTolerance = .000001
		gamma = .9
		getLandmarkPolicy = targetCode.getLandmarkPolicy(V, convergenceTolerance, gamma)

		merge = targetCode.merge

		setUp = targetCode.setUpLandmark(landmarkLocation, landmarkStateSet, getTransitionTable, getLandmarkReward, getLandmarkPolicy, merge)

		existingOptions = {}
		self.landmarkPolicies = setUp(existingOptions)

	#testing landmark policies --> make sure locations surrounding location of interest AND at location of interestare correct
	@data(((3,2), (0,1)), ((3,4), (0,-1)), ((3,3), (1,0)))
	@unpack
	def test_LandmarkHallway1(self, state, expectedAction):
		self.assertEqual(self.landmarkPolicies["h1"][state], expectedAction)

	@data(((4,2), (1,0)), ((5,2), (0,1)), ((6,2), (-1,0)))
	@unpack
	def test_LandmarkHallway2(self, state, expectedAction):
		self.assertEqual(self.landmarkPolicies["h2"][state], expectedAction)

	@data(((4,6), (1,0)), ((5,6), (0,1)), ((6,6), (-1,0)))
	@unpack
	def test_LandmarkHallway3(self, state, expectedAction):
		self.assertEqual(self.landmarkPolicies["h3"][state], expectedAction)

	@data(((9,3), (0,1)), ((9,4), (1,0)), ((9,5), (0,-1)))
	@unpack
	def test_LandmarkHallway4(self, state, expectedAction):
		self.assertEqual(self.landmarkPolicies["h4"][state], expectedAction)

	#testing boundary locations don't go off the specified grid
	@data(("h1", (3,1), (0,1)), ("h2", (6,1), (0,1)), ("h3", (4,7), (0,-1)), ("h4", (10,7), (0,-1)))
	@unpack
	def testLandmarkBoundaries(self, policy, state, expectedAction):
		self.assertEqual(self.landmarkPolicies[policy][state], expectedAction)

	def tearDown(self):
		pass
 
if __name__ == '__main__':
	unittest.main(verbosity=2)
