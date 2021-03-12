#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 21:20:53 2016

@authors: Lyuba Dimitrova <dimitrova@cl.uni-heidelberg.de>
          Martina Brauchler <brauchler@cl.uni-heidelberg.de>
          Utaemon Toyota <toyota@cl.uni-heidelberg.de>
name: aufg25.py
usage: /aufg25.py
        execution in python interpreter, 
        prints substitutions for the defined examples
license: MIT Copyright (c) 2016 @authors
"""

import re

#Tuples for all examples, in the form (pattern-in-string, replacement, string)
ex1 = ('Hallo', 'Hello', 'Hallo, Peter!')
ex2 = ('[aeiu]', 'o', 'Hallo, Peter!')
ex3 = ('.', 'X', 'Hallo, Peter!')
ex4 = ('[A-Za-z]', 'x', 'Hallo, Peter!')
ex5 = ((r'\bPeter\b'), 'Hans', 'Hallo, Peter Petersen!')
ex6 = ('\s', '', 'Hallo, Peter Petersen!')
ex7 = ('[^a-zA-Z]', '', 'Hallo, Peter Petersen!')

list_of_examples = [ex1, ex2, ex3, ex4, ex5, ex6, ex7]

for example in list_of_examples:
    print(example[2], " wird zu ", re.sub(example[0],example[1],example[2]),
    "mit Regex:   (", example[0],")", " ersetzt durch:  ", 
    example[1] if example[1]!='' else "leeren String")