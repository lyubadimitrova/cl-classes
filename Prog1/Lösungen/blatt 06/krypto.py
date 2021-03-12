#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Wed Dec  7 21:43:46 2016

@authors: Lyuba Dimitrova <dimitrova@cl.uni-heidelberg.de>
          Martina Brauchler <brauchler@cl.uni-heidelberg.de>
          Utaemon Toyota <toyota@cl.uni-heidelberg.de>
name: krypto.py
usage: import krypto (module to be used in python interpreter)
       krypto.albam(string)
license:
"""


def albam(aString):
    '''
    encrypts a string by substituting its characters
    with other characters. Substituting characters are specified
    by key (in this case key=13)

    Parameters
    ----------
    aString: string

    Returns
    -------
        str: encrypted Version of aString -> message

    Example
    -------

    >>> albam('hallo')
    'unyyb'
    >>> albam('unyyb')
    'hallo'
    >>> albam('MAKARENA')
    'ZNXNERAN'
    >>> albam('makarena')
    'znxneran'
    >>> albam('mAkArEna')
    'zNxNeRan'
    '''
    message=''
    for i in range(len(aString)):
        if   'M'< aString[i] <='Z'   or   'm'< aString[i] <='z':
            message += chr(ord(aString[i])-13)
        else: message += chr(ord(aString[i])+13)
    return message

if __name__ == '__main__':
    import doctest
    doctest.testmod()

