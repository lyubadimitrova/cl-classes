#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Tue Dec 6 16:58:45 2016

@authors: Lyuba Dimitrova <dimitrova@cl.uni-heidelberg.de>
          Martina Brauchler <brauchler@cl.uni-heidelberg.de>
          Utaemon Toyota <toyota@cl.uni-heidelberg.de>
name: aufg20.py
usage: /aufg20.py
license:
"""

def checkSolution(problem, solution):
    
    if len(solution) != len(problem):
        return False
    for i in range (len(problem)):
        if problem[i] != "_" and problem[i]!=solution[i]:
            return False
    return True
    
    
print(checkSolution('St__l___en', 'Stallhosen'))
print(checkSolution('St__l___en', 'Stuhlboden'))
print(checkSolution('St__l___en', 'Stilleben'))
    