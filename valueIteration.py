# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 13:47:30 2020

@author: Kevin

just changed name from action --> option for sMDP environment
"""

import sys
import os
dirName = os.path.dirname(__file__)
sys.path.append(os.path.join(dirName, 'executive', ""))

import numpy as np
import transitionFunction as tf
import rewardFunction as rf
import optionSpaceFunction as osf

class BellmanUpdate(object):
    
    def __init__(self, stateSpace, optionSpaceFunction, transitionFunction, rewardFunction, gamma):
        self.stateSpace=stateSpace
        self.optionSpaceFunction=optionSpaceFunction
        self.transitionFunction=transitionFunction
        self.rewardFunction=rewardFunction
        self.gamma=gamma

    def __call__(self, s, V):
        Qs={a: sum([self.transitionFunction(s, a, sPrime)*(self.rewardFunction(s, a, sPrime)+self.gamma*V[sPrime]) for sPrime in self.stateSpace])\
            for a in self.optionSpaceFunction(s)}
        Vs=max(Qs.values())
        return Vs
    

class ValueIteration(object):
    
    def __init__(self, stateSpace, optionSpaceFunction, theta, bellmanUpdate):
        self.stateSpace=stateSpace
        self.optionSpaceFunction=optionSpaceFunction
        self.theta=theta
        self.bellmanUpdate=bellmanUpdate

        
    def __call__(self):
        V={state:0 for state in self.stateSpace}
        delta=np.inf
        while (delta > self.theta):
            delta=0
            for s in self.stateSpace:
                v=V[s]
                V[s]=self.bellmanUpdate(s, V)
                delta=max(delta, abs(v-V[s]))
        return V
    
    
class GetPolicy(object):
    
    def __init__(self, stateSpace, optionSpaceFunction, transitionFunction, rewardFunction, gamma, V, roundingTolerance):
        self.stateSpace=stateSpace
        self.optionSpaceFunction=optionSpaceFunction
        self.transitionFunction=transitionFunction
        self.rewardFunction=rewardFunction
        self.gamma=gamma
        self.V=V
        self.roundingTolerance=roundingTolerance
        
    def __call__(self, s):
        Qs={a: sum([self.transitionFunction(s, a, sPrime)*(self.rewardFunction(s, a, sPrime)+self.gamma*self.V[sPrime]) for sPrime in self.stateSpace])\
            for a in self.optionSpaceFunction(s)}
        optimalActionList=[a for a in self.optionSpaceFunction(s) if abs(Qs[a]-max(Qs.values())) < self.roundingTolerance]
        policy={a: 1/(len(optimalActionList)) for a in optimalActionList}
        return policy
        




        
        
