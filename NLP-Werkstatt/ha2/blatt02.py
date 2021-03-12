# -*- coding: utf-8 -*-
"""
@author: Lyubomira Dimitrova
E-Mail: <dimitrova@cl.uni-heidelberg.de>
"""
import re
import sys

'''
Specification of input and output path; if fewer command line arguments 
are found, the paths default to an empty string
'''
input_path = ''
output_path = ''

try:
    input_path = sys.argv[1]
    try:
        output_path = sys.argv[2]
    except IndexError:
        pass
except IndexError:
    pass
   
'''
Extract lines from file; Lines beginning with #(in this case specifying 
start/end of document) are ignored, empty lines remain
'''
with open(input_path + "cctv_0001.v4_gold_conll.txt",'r') as file:
    conll = [line for line in file.readlines() if line[0]!='#']

'''             
Aufgabe1: 
    Goal: Extraction of sentences, output in file with 1 sentence per line
'''
with open(output_path + "sentences.txt",'w') as file:
    for line in conll:
        if line == '\n':             #empty lines mean end of sentence
            file.write('\n')         #-> new line in output file
            continue
        file.write(line.split()[3])  #the word tokens are in the 4th column 
        file.write(' ')              #of the table -> 3rd item in split line

'''
Aufgabe2:
    Goal: Get the sets of used POS-tags and Entity-labels
    + Output in file
'''
conll = [line for line in conll if line!='\n']    #remove empty lines, since
                                                  #sentences no longer matter                                                 
#POS-tags in the 5th column; we use a set comprehension to remove duplicates
pos_tags = {line.split()[4] for line in conll}
with open(output_path + "postags.txt",'w') as file:
    for elm in pos_tags:
        file.write(elm)
        file.write('\n')

#Entity-tags -> 11th column; set comprehension to remove duplicates, strip()
#method to get only the tag, and a difference to remove the empty string
entity_labels = {line.split()[10].strip('()*') for line in conll} - {''}
with open(output_path + "entlabels.txt",'w') as file:
    for elm in entity_labels:
        file.write(elm)
        file.write('\n')

'''
Aufgabe3:
    Goal: For each entity-label extract all instances in the table;
          For each entity-label a separate output file (alphabetically sorted)  
'''
new = []                   
for line in conll:           #final split: each line becaomes a list of tokens
    new.append(line.split())
        
for label in entity_labels:
    found_list = []
    for i in range(len(new)):     #not very cheap, but the only idea that worked
        item = []
        if re.search(label,new[i][10])!=None:   #true if line contains label
            while True:                         #builds multiple-word instances
                item.append(new[i][3])        
                if new[i][10].endswith(')'):        #signifies end of instance
                    found_list.append(item)      
                    break
                i+=1              #gets next line
                
    with open(output_path + label + '.txt','w') as file:
        for instance in sorted(found_list):        
            file.write(' '.join(instance))       #instance: list -> string
            file.write('\n')


