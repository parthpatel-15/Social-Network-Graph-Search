#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 22:04:12 2021

@author: Parth patel
"""

#create a dictionary with all the mappings :
graph = {}
graph["Parth"] = {"Adam", "Frank","George"}
graph["Adam"] = {"Bob", "Parth", "Ema"}
graph["Ema"] = {"Bob", "Adam", "Dolly"}
graph["Dolly"] = {"Ema", "Bob"}
graph["Bob"] = {"Dolly", "Adam","Ema"}
graph["George"] = {"Parth"}
graph["Frank"] = {"Parth"}




# creat an another graph to check others requirements in assignment :

graph1 = {}
graph1["Parth"] = {"Adam", "Frank","George"}
graph1["Adam"] = {"Bob", "Parth", "Ema"}
graph1["Ema"] = {"Bob", "Adam", "Dolly"}
graph1["Dolly"] = {"Ema", "Bob"}
graph1["Bob"] = {"Dolly", "Adam","Ema"}
graph1["George"] = {"Parth"}
graph1["Frank"] = {"Parth"}
graph1["Rock"] = {"Selena"}
graph1["Selena"] = {"Rock"}






