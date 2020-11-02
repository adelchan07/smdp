"""
Created on Thu Oct 22 14:32:23 2020
@author: adelphachan
interruptedMain.py

resulting policies that will be used to graph difference between interrupted and normal path
"""
import sys
import os
dirName = os.path.dirname(__file__)
sys.path.append(os.path.join(dirName, 'visualization', ""))

import numpy as np
from drawInterruption import drawFinalMap

width, height = 5,10
state = (4,0)
stateSet = [(i,j) for i in range(5) for j in range(10)]
normalPath = {(4, 0): (0, 1), (4, 1): (0, 1), (4, 2): (0, 1), (4, 3): (0, 1), (4, 4): (0, 1), (4, 5): (0, 1), (4, 6): (0, 1), (4, 7): (0, 1), (4, 8): (0, 1), (4, 9): (-1, 0), (3, 9): (-1, 0), (2, 9): (-1, 0), (1, 9): (-1, 0)}
interruptedPath = {(4, 0): (0, 1), (4, 1): (0, 1), (4, 2): (0, 1), (4, 3): (0, 1), (4, 4): (0, 1), (4, 5): (-1, 1), (3, 6): (-1, 1), (2, 7): (-1, 1), (1, 8): (-1, 1)}
{(-1, 1): 1.0}

goalState = (0,9)
goalStateDomain = [(i,j) for i in range(0,5) for j in range(5,10)]

drawFinalMap(width, height, state, normalPath, interruptedPath, goalState, goalStateDomain)
