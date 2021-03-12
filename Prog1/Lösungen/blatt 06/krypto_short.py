#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Wed Dec  7 21:43:46 2016
@author: Lyuba Dimitrova <dimitrova@cl.uni-heidelberg.de>
name: krypto.py
usage: import krypto (module to be used in python interpreter)
license:
"""

def albam(string):
    message=''
    for i in range(len(string)):
        if  'M'< string[i] <='Z'   or   'm'< string[i] <='z':
            message += chr(ord(string[i])-13)
        else: message += chr(ord(string[i])+13)
    return message
    
if __name__ == '__main__':
    
    print(albam('MAKARENA'))
    print(albam('makarena'))
    print(albam('mAkArEna'))
    
    