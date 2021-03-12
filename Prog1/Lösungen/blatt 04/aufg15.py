# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 15:56:51 2016

@author: Martina Brauchler, Lyuba Dimitrova
"""
def tribonacci(n):              
    if n==1 or n==2: 
        return 0
    if n==3:
        return 1
    return tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)
  
#print("You've heard of the Fibonacci sequence, now get ready for... \
       # TRIBONACCI", '\n')
#print("Which consecutive Tribonacci number would you like to know?")

target = int(input())
print(tribonacci(target))


