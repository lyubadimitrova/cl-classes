#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 19:43:33 2017

@authors: Lyuba Dimitrova <dimitrova@cl.uni-heidelberg.de>
          Martina Brauchler <brauchler@cl.uni-heidelberg.de>
          Utaemon Toyota <toyota@cl.uni-heidelberg.de>
name: ngrams2.py
usage: Module to be used in Python Interpreter
       from ngrams2 import NGrams
       object = NGrams(filename_as_string)
license: MIT Copyright (c) 2017 @authors
"""

class NGrams:
    '''
    Objects are initialised with a filename

    Parameters
    ----------
    filename: string; name of a text file

    Example
    -------
    
    >>> instance = NGrams("test.txt")
    >>> print(instance)
    Das ist eine kleine Datei zum Testen

    '''
    def __init__(self,filename):
        self.string = open(filename, 'r').read()
        
    def __str__(self):
        return self.string
    
    def getNGrams(self,n):
        '''
        creates an n-gram model from self.string

        Parameters
        ----------
        n: determines unigram (n=1), bigram (n=2)...

        Returns
        -------
        ngram_list: list of lists(separate ngrams)

        Example
        -------
        >>> instance = NGrams("test.txt")
        >>> print(instance.getNGrams(2))
        [['Das', 'ist'], ['ist', 'eine'], ['eine', 'kleine'], ['kleine', 'Datei'], ['Datei', 'zum'], ['zum', 'Testen']]
         
        '''
        tokens = self.string.split()
        ngram_list=[]
    
        for i in range(len(tokens)-n+1):
            ngram=[word for word in tokens[i:i+n]]
            ngram_list.append(ngram)

        return ngram_list
        
if __name__=="__main__":
    ng = NGrams("test.txt")
    print(ng)
    print(ng.getNGrams(2))
    import doctest
    doctest.testmod()

