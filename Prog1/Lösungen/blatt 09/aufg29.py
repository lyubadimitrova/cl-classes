# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 21:02:52 2017

@authors: Lyuba Dimitrova <dimitrova@cl.uni-heidelberg.de>
          Martina Brauchler <brauchler@cl.uni-heidelberg.de>
          Utaemon Toyota <toyota@cl.uni-heidelberg.de>
name: ngrams2.py
usage: Module to be used in Python Interpreter
       from ngrams2 import NGrams
       object = NGrams(filename_as_string)
license: MIT Copyright (c) 2017 @authors
"""
import re

class RegExMatch:
    def __init__(self, search, sub, search_string):
        self.search = search
        self.sub = sub
        self.string = search_string
        self.result = re.sub(self.search, self.sub, self.string)
        
    def __str__(self):
        return self.result

myregclass = RegExMatch("la","ma","tumbala laika")
print(myregclass)

        
    
    