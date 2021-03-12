# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 17:54:29 2016

@author: Martina Brauchler, Lyuba Dimitrova
"""

def print_un_even(str):
  for i in range(len(str)):
    if i%2==1:
        print (str[i])

print("Enter a string: ")
string = input()
print_un_even(string)
