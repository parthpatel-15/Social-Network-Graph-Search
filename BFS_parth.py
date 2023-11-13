#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 22:04:12 2021

@author: Parth patel
"""
from Node import Node
from State import State
from collections import deque
from GraphData import graph , graph1

# function with 3 arguments as per assignment
def BFS_Parth(graph, initname, goal):
    """
    This function performs BFS search using a queue
    
    """
    check = True
    goalAvailable = False
    
    # check graph (req:7):
    if not type(graph) == dict:
        print("-----------------------------")
        print("")
        print("graph is not available")
        print("")
        print("-----------------------------")
        check = False
    # check  the  initialname 
    elif initname not in graph:
        print("-----------------------------")
        print("")
        print(initname +"(initial name) is not in the graph ")
        print("")
        print("-----------------------------")
        check = False
    # check the goal that it is exist or not  in the graph
    else:
        for studentName in graph:
            for name in graph[studentName]:
                if name == goal:
                    goalAvailable = True
                    break
                    break
        if not  goalAvailable:
            print("-----------------------------")
            print("")
            print(goal + "(target name) is not exist.")
            print("")
            print("-----------------------------")
            check = False
            
            
            
    if check:
    
        #create queue
        queue = deque([]) 
        #since it is a graph, we create visited list
        visited = [] 
        #create root node
        initialState = State(initname, goal, graph)
        root = Node(initialState)
        #add to queue and visited list
        queue.append(root)    
        visited.append(root.state.name)
        # check if there is something in queue to dequeue
        while len(queue) > 0:
        
            #get first item in queue
            currentNode = queue.popleft()
        
            print (("-- dequeue --"), currentNode.state.name)
        
            #check if this is goal state
            if currentNode.state.checkGoalState():
                print ("reached goal state")
                #print the path
                print ("----------------------")
                print ("Path")
                currentNode.printPath()
                break  

            
            #get the child nodes 
            childStates = currentNode.state.successorFunction()
            for childState in childStates:
            
                childNode = Node(State(childState, goal, graph))
            
                #check if node is not visited
                if childNode.state.name not in visited:
                
                    #add this node to visited nodes
                    visited.append(childNode.state.name)
                
                
                    #add to tree and queue
                    currentNode.addChild(childNode)
                    queue.append(childNode) 

        if not currentNode.state.checkGoalState():
            print ("----------------------")
            print ("sorry, realtion is not available")

        #print tree
        print ("----------------------")
        print ("Tree")
        root.printTree()
        print("***************************************************")
        print("")
        print("")
        print("")
    
# req 9 : Dolly needs to get introduced to you (Parth)    
BFS_Parth(graph, "Dolly", "Parth")
# req 9 : George needs to get introduced to Bob:
BFS_Parth(graph, "George", "Bob")

# req 6 : relationship cannot be established:
BFS_Parth(graph1, "George", "Rock")

# req 8 : initialname does not exist :
BFS_Parth(graph, "Justin", "Bob")

# req 9 : Target does not exist :
BFS_Parth(graph, "George", "Henry")

# req 7 : arguments do not exist:
BFS_Parth("graph2", "George", "Bob")



