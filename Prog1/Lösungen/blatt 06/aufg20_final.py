#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
Created on Thu Dec  1 20:11:23 2016
@author: Lyuba Dimitrova, Utaemon Toyota & Martina Brauchler
name: Aufg_20_checkSolution.py
Checks if a solution for a problem string is valid
usage: /Aufg_20_checkSolution.py
license: feel free to use
"""

def checkSolution(problem, solution):
    '''
    Given a problemstring with missing characters - replaced
    by underscores - and an solutionstring, check if
    solutionstring is a valid solution which can be
    generated from problemstring and matches its length


    Parameters
    ----------
    problem: a String,
    solution: a String

    Returns
    -------
        bool

    Example
    -------

    >>> checkSolution('St__l___en', 'Stallhosen')
    True
    >>> checkSolution('St__l___en', 'Stuhlboden')
    True
    >>> checkSolution('St__l___en', 'Stilleben')
    False
    '''
    if len(solution) != len(problem):
        print('solution is invalid because of length:')
        return False
    for i in range (len(problem)):
        if problem[i] != "_" and problem[i]!=solution[i] :
            print('solution is invalid because of invalid character:')
            return False
    return True


if __name__ == '__main__':

    print('1: ', checkSolution('St__l___en', 'Stallhosen'))
    print('2: ',checkSolution('St__l___en', 'Stuhlboden'))
    print('3: ',checkSolution('St__l___en', 'Stilleben'))
    print('4: ',checkSolution('St__l___en', 'Stallhos5n'))
    print('5: ',checkSolution('St__l___en', 'Stallhosen'))