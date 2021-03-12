# -*- coding: utf-8 -*-
"""
Created on Sun May  7 11:51:35 2017

@author: Asus
"""

with open("CoNLL2009-ST-Spanish-trial.txt",'r') as file:
    sp = file.readlines()

with open("oraciones.txt",'w') as file:
    for line in sp:
        if line == '\n':             #empty lines mean end of sentence
            file.write('\n')         #-> new line in output file
            continue
        file.write(line.split()[1])  #the word tokens are in the 4th column 
        file.write(' ')              #of the table -> 3rd item in split line