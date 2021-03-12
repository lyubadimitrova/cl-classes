# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 22:57:02 2016

@author: Asus
"""

def erase_stopwords(text,stopword_list):     
    li_words=text.split()           #split into words at whitespace characters
    
    li_words=[elm for elm in li_words if elm not in stopword_list]
                #makes a list only of the elements not in the stopword-list
    
    new_text=" ".join(li_words) #makes a string of the 'clean' list
    return new_text
    
text="The man with the cat spoke of the sea"
stopword_list=['The','the','of','a']

print(erase_stopwords(text,stopword_list))