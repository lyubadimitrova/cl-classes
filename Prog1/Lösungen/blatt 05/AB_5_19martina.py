#!/usr/bin/env python

# Created on Fri Nov 11 22:59:00 2016
# author:  Lyuba Dimitrova, Utaemon X & Martina Brauchler
# Aufgabenblatt 05, Aufgabe 19: Gibt Anzahl der Types in einem Korpus aus

# Funktionen


def CountWordsInFile(aFileName):
    text = open(aFileName, 'r').read()
    ls_file = convert_str_to_ls(text)
    ls_types = list(set(ls_file))
    return ls_types


def convert_str_to_ls(aString):
    # konvertiert String in Liste
    ls_str1 = aString.split()
    return ls_str1


# Programm
print(CountWordsInFile('Prog_1_Aufgabenblatt_05.txt'))
