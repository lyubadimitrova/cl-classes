"""
Created on Wed Jan  18 15:01:46 2017

@authors:   Lyuba Dimitrova <dimitrova@cl.uni-heidelberg.de>
            Martina Brauchler <brauchler@cl.uni-heidelberg.de>
            Utaemon Toyota <toyota@cl.uni-heidelberg.de>
name:       ngrams2.py
usage:      import ngrams2 (module for creating ngrams from txt-data-instances)
            print (NGrams("any.txt",n).getNGrams()) (choose any txt.files for "any.txt" and choose an Integer for the nGrams)

            The modul ngrams created on Mon Dec 5 18:35:44 2016 by @authors is required.
license:    MIT Copyright (c) 2017 @authors
"""

class NGrams:
    def __init__(self,file,n):
        """Creating an instance for each .txt-file"""
        self._file = file
        self._n = n

    def openfile (self):
        """Opens and reads a .txt-file and returns a string"""
        file = self._file
        text = open (file, 'r').read()
        text.close()
        text = str(text)
        return text

    def getNGrams (self):
        """Imports the function makeNGRams from the module ngrams and returns an NGram-list of the .txt-file"""
        from ngrams import makeNGrams
        newtext = self._file
        n = self._n
        ngrams = makeNGrams(newtext,n)
        return ngrams

if __name__=="__main__":
    import doctest
    doctest.testmod()