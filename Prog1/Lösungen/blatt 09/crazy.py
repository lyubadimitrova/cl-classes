# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 20:14:59 2017

@author: Asus
"""

from ngrams2 import NGrams
ng = NGrams("hp.txt")
print(ng.getNGrams(2))