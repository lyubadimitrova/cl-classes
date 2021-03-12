#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Mon Dec 5 18:35:44 2016

@authors: Lyuba Dimitrova <dimitrova@cl.uni-heidelberg.de>
          Martina Brauchler <brauchler@cl.uni-heidelberg.de>
          Utaemon Toyota <toyota@cl.uni-heidelberg.de>
name: ngrams.py
usage: import ngrams (module to be used in python interpreter)
       ngrams.makeNGrams(string)
license:
"""


def makeNGrams(filename,n):
    
    '''
    makes an n-gram model out of word sequence

    Parameters
    ----------
    filename: string; name of a text file
    n: determines unigram (n=1), bigram (n=2)...

    Returns
    -------
    list: list of n-grams, where every n-gram is also a list -> ngram_list

    Example
    -------

    >>> makeNGrams('test.txt', 1)
    [['Das'], ['ist'], ['eine'], ['kleine'], ['Datei'], ['zum'], ['Testen']]
    >>> makeNGrams('test.txt', 2)
    [['Das', 'ist'], ['ist', 'eine'], ['eine', 'kleine'], ['kleine', 'Datei'], ['Datei', 'zum'], ['zum', 'Testen']]
    >>> makeNGrams('test.txt', 3)
    [['Das', 'ist', 'eine'], ['ist', 'eine', 'kleine'], ['eine', 'kleine', 'Datei'], ['kleine', 'Datei', 'zum'], ['Datei', 'zum', 'Testen']]
   
    '''
    text=open(filename, 'r').read()
    tokens=text.split()
    ngram_list=[]
    
    for i in range(len(tokens)-n+1):
        ngram=[]
        for word in tokens[i:i+n]:
            ngram.append(word)
        ngram_list.append(ngram)

    return ngram_list

if __name__=="__main__":
    print(makeNGrams("test.txt",2))
    import doctest
    doctest.testmod()
