#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created on Fri Nov 11 22:59:00 2016
# author:  & Martina Brauchler
# Aufgabenblatt 04

# Aufgabe 12


def printUnEven(astring=''):
        for i in range(1,len(astring)-1,2):
                print(astring[i])

# Aufgabe 13


def printEvery(astring='',n=1):
    for i in range(0,len(astring)-1,n):
        print(astring[i])

def readInputNumber():
        inp_number = int(input('Eine Zahl:' ))
        return inp_number

def printSelective(astring='',alist=[]):
    pass




astring = 'hbdxlsöjuqiqop'
printUnEven(astring)
printEvery()
'''
a,b,c = 0,1,2
print(a)
print(b)
print(c)
'''