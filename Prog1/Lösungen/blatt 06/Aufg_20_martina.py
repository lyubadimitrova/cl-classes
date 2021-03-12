#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 20:11:23 2016
@author: Martina Brauchler <brauchler@cl.uni-heidelberg.de>
name: Aufg_20_checkSolution.py
usage: /Aufg_20_checkSolution.py
license:
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
    valid = False
    if len(solution) == len(problem):
        valid_len = True
        for i in range (len(problem)):
            valid_character = False
            if problem[i].isalpha():
                if problem[i] == solution[i]:
                    valid_character = True
                else:
                    valid_character = False
                    print('solution is invalid because of invalid character:')
                    break
            elif problem[i] == '_':
                if solution[i].isalpha():
                    valid_character = True
                elif  solution[i] == '_':
                    valid_character = False
                    print('solution is invalid because of an invalid character:')
                    break
                elif solution[i].isdigit:
                    valid_character = False
                    print('solution is invalid because of an invalid character:')
                    break
    else:
        valid_len = False
        print('solution is invalid because of length:')
    if valid_len == True and valid_character == True:
        valid = True
    return valid
# TODO: shorten function with is not

if __name__ == '__main__':

    print('1: ', checkSolution('St__l___en', 'Stallhosen'))
    print('2: ',checkSolution('St__l___en', 'Stuhlboden'))
    print('3: ',checkSolution('St__l___en', 'Stilleben'))
    print('4: ',checkSolution('St__l___en', 'Stallhos5n'))
    print('5: ',checkSolution('St__l___en', 'Stallhosen'))





