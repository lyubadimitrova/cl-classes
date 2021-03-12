# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 14:31:24 2016

@author: Martina Brauchler, Lyuba Dimitrova

"""
def int_list(string, list):   #input of integer-only list
    stopper = 0
    while stopper==0 :
        new_element = input()
        if new_element.isdigit():
            number = int(new_element)
            list.append(number)
        else:
            stopper = 1
    return list
  
def print_selective(string, list):
    for number in list:
        if number>=len(string):
            print(number, '\t', "Not a string index")
        else:
            for i in range(len(string)):
                if number==i:
                    print(number,'\t', string[i])
                    break  
    return None
 
print("Gimme a string: ")
str = input()

list1 = []
print("Now enter your list! \
      (To end input, enter something other than an integer>=0):")

list1 = int_list(str, list1)
print("Your list: ", list1)

print("Your selection: ")
print_selective(str, list1)
