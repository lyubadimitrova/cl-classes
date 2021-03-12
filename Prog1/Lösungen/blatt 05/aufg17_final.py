#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created on Fri Nov 11 22:59:00 2016
# author:  Lyuba Dimitrova, Utaemon X & Martina Brauchler
# Aufgabenblatt 05, Aufgabe 17: Entfernt Stopworte aus einem String


def convert_str_to_ls(aString):   # konvertiert String in Liste
    ls_str1 = aString.split()
    return ls_str1

def convert_ls_to_str(aList):   # konvertiert Liste in String
    aString = ' '.join(aList)
    return aString
    
def erase_stopwords(aString, stopword_list):   
    #entfernt Stopwörter aus einem String
    ls_string = convert_str_to_ls(aString)
    clean_list=[elm for elm in ls_string if elm not in stopword_list]
    text = convert_ls_to_str(clean_list)
    return text

print(erase_stopwords('The man with the cat spoke of the sea',\
                      ['the','of','The','a']),"\n")

print(erase_stopwords('This is a test',['the','of','The','a']),"\n")

print(erase_stopwords('This is a test',[]),"\n")