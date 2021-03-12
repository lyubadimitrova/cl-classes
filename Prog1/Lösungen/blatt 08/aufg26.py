# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 09:29:32 2017
Created on Tue Jan 10 07:50:32 2017
authors: Lyuba Dimitrova <dimitrova@cl.uni-heidelberg.de>
          Martina Brauchler <brauchler@cl.uni-heidelberg.de>
          Utaemon Toyota <toyota@cl.uni-heidelberg.de>
name: aufg.26.py
usage: execute aufg.26 to count words and lines in a file
license: MIT Copyright (c) 2017@authors
"""
from nltk.tokenize import word_tokenize
from random import choice

def process_text(filename):
    new_file = open(filename, 'r')              #opens a file
    file_str = new_file.read()                  #puts all words in a list
    new_file.close()                            #closes the file
    ls_all_words = word_tokenize(file_str)      #creates a list of words

    bigram_list = []

    for i in range(len(ls_all_words) - 1):
        """
        Creates a list of tuples (word, next word)
        """
        bigram = ls_all_words[i], ls_all_words[i+1]
        bigram_list.append(bigram)

    dic = {}

    for pair in bigram_list:
        """
        Creates a dictionary with the word types as keys, and a set of all
        words that can follow them as value
        """
        dic[pair[0]] = set([all_pairs[1] for all_pairs in bigram_list if all_pairs[0] == pair[0]])

    return dic


def markov_gen(dic, n=100):
    generated_string = ''
    a_word = choice(list(dic.keys()))   #chooses the first word from the available keys
    generated_string += a_word          #adds it to the empty string
    generated_string += ' '             #spaces are important
    for i in range(n-1):
        a_word = choice(list(dic[a_word])) #new wordes are chosen from the set of values of the previous word
        generated_string += a_word
        generated_string += ' '
    return generated_string

#print(process_text('3000.txt'))
print(markov_gen(process_text('hp.txt'), 200))