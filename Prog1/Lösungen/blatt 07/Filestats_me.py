#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 22:12:21 2016

@author: Asus
"""

def count_lines(filename):
    text=open(filename, 'r').read()
    lines = text.split('\n')
    lines = [elm for elm in lines if elm!='']
#"""
    if lines[0]=='п»ї':   #Windows adds this symbol at the start of every .txt file
        del lines[0]
#"""
    return len(lines)
    
def count_characters(filename):
    import re
    text=open(filename, 'r').read()
    return len(re.findall('[a-zA-Z]',text))
    
if __name__ == '__main__':
    print("This file has", count_lines("test.txt"), "non-empty lines and",\
          count_characters("test.txt"), "letters!")