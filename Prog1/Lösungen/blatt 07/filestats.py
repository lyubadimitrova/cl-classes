#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Wed Dec 21 21:43:46 2016

@authors: Lyuba Dimitrova <dimitrova@cl.uni-heidelberg.de>
          Martina Brauchler <brauchler@cl.uni-heidelberg.de>
          Utaemon Toyota <toyota@cl.uni-heidelberg.de>
name: filestats.py
usage: import filestats (module for counting lines and/or alphabetic characters in a text file)
       filestats.countLines(filename)
       filestats.countCharacters(filename)
license: MIT Copyright (c) 2016 @authors
"""

def countLines(string_filename):
    """
        Does: Counts lines in text file (ignoring empty lines and whitespace-only lines)
        
        Parameters: string_filename -> str
        Returns: number of lines -> int
        Usage: filestats.countLines(string_filename) in console
    """
    
    text_file = open(string_filename,'r')               #opens a file 'string_filename'
    listed_lines = text_file.read().splitlines()        #makes a list of the lines in the file
    listed_lines = [i for i in listed_lines if i!='']   #removes every empty item from list of lines
    text_file.close()                                   #closes the file 'string_filename'
    return len(listed_lines)


def countCharacters(string_filename):
    """
        Does: Counts alphabetic characters in file
        
        Parameters: string_filename -> str
        Returns: number of alph. characters -> int
        Usage: filestats.countCharacters(filename)
    """
       
    import re
    text_file = open(string_filename, 'r')      #opens a file 'string_filename'
    string = text_file.read()
    text_file.close()                           #closes the file
    return len(re.findall('[a-zA-Z]', string))
   

if __name__ == '__main__':
    print("This file has", countLines("test.txt"), "non-empty lines and",\
          countCharacters("test.txt"), "letters!")
    import doctest
    doctest.testmod()