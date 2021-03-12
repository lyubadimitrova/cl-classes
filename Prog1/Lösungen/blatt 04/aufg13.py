# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 17:59:56 2016

@author: Martina Brauchler, Lyuba Dimitrova
"""

def print_every(string,integer):
  for i in range(len(string)):
    if i%integer==0:
      print(string[i])
  return None

str = input("Enter a string:  ")
number = int(input("Enter an integer:"))
print_every(str,number)
