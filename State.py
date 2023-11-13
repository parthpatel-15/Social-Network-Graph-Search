#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 22:04:12 2021

@author: Parth Patel
"""



class State:
    '''
    This class retrieves state information for social connection feature
    '''
    
    def __init__(self, name, goal, graph):
        
        self.name  = name
        self.goal  = goal
        self.graph = graph
       

    def successorFunction(self):
        """
        This is the successor function. It finds all the persons connected to the
        current person
        """
        return self.graph[self.name]
        
        
    def checkGoalState(self):
        """
        This method checks whether the person is Jill.
        """ 
        #check if the person's name 
        return self.name == self.goal