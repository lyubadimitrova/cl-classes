# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 22:37:58 2016

@author: Asus
"""

text=open("Prog_1_Aufgabenblatt_05.txt",'r').read()
text=text.lower()           #can be left out if 'The' and 'the' need to be 
                            #considered as different words 
                            
                            
def no_punct(aString):  #ensures 'it' and 'it." are the same word, by removing punctuation
    for char in aString:
        if not (char.isalnum() or char.isspace()):
            aString=aString.replace(char," ")
    return aString
    
def count_words_infile(aString):
    li_words=[]
    li=no_punct(aString).split()  #splits at whitespace(one or more spaces, new line)
    
    for elm in li:             #only leaves one instance of each word
        if elm not in li_words:
            li_words.append(elm)
    return li_words
    
print(count_words_infile(text))