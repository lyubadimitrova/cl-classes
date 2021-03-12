# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
Goal: Authomatic discovery, decoding and output of 
      hexadecimal encoded HTML entities 
Author: Lyubomira Dimitrova <dimitrova@cl.uni-heidelberg.de>

"""

import sys
import re

def split_in_lines(filename):
    with open(filename, 'r', encoding = 'utf-8') as file:
        return file.read().split('\n')
        
def split_at_tabs(list_of_lines):       #For the documents emoji-test_tab.txt and 
    new_list = []			#Unicode_UTF-8-character_table_tab.txt
    for line in list_of_lines:
        new_line = line.split('\t')
        new_list.append(new_line)
    return new_list

def open_write(filename):
    return open(filename,'w', encoding = 'utf-8')


"""
Extract the 5th and 7th line of the HTML source file -> string
"""
'''
text = "Juhuu! Es ist Fr&#x00FC;hling &#x1F600; und die &#x2600;&#xFE0F; \
	scheint! &#x2753; Wo lebstu? Hier Schei&#x00DF; Wetter &#x1F327; \
	&#x1F620; &#x26A1;..."
'''

html_text = split_in_lines("emojis.html")
text = [html_text[line-1] for line in range(len(html_text)) if line==5 or line==7]
text = " ".join(text)


"""
Create a dictionary with the hexadecimal codes in the text 
as keys and their description as values
"""

'''
dic = {'&#x00FC;':'ü', '&#x1F600;':'grinning face', '&#x2600;&#xFE0F;':'sun',
       '&#x2753;':'question mark', '&#x00DF;':'ß', '&#x1F327;':'cloud with rain',
       '&#x1F620;':'angry face', '&#x26A1;':'high voltage'}
'''           

emojis_description = split_at_tabs(split_in_lines("emoji-test_tab.txt"))
sp_characters = split_at_tabs(split_in_lines("Unicode_UTF-8-character_table_tab.txt"))

codes = re.compile("&#x[A-F0-9&#x;]{4,12};")
list_of_specials = re.findall(codes,text)      # Makes a list of all HTML entities
					       # found in the text
dic = {}
for line in emojis_description:                
    if line[0] in list_of_specials:
        dic[line[0]] = line[2]	      # The emoji description is after the second tab
					
for line in sp_characters:
    if line[0] in list_of_specials:
        dic[line[0]] = line[1]	      # The special characters are after the first tab


"""
Output: all found HTML entities in the text
"""
print("Original text:\n",text,'\n')

try:				# Check if there is a specified output file
  filename = sys.argv[1]	
  file = open_write(filename)
except IndexError:
  filename = "found_html-entities.txt"
  file = open_write(filename)
finally: 
  print('Output in file',filename,'\n')
  
print("Found HTML entities: ")
for code in list_of_specials:         # Goes through all HTML entities in the text
    print(code,": ",dic[code])
    file.write(code) 
    file.write(" : ") 
    file.write(dic[code]) 
    file.write("\n")
file.close() 
print('\n')


"""
Output: Replace all HTML entities in the text with description/character
For better readability, emoji descriptions get parenthesis, special characters don't
"""
for key in dic:                                   
    if re.fullmatch('.',dic[key]) == None:        
        dic[key] = '(' + dic[key] + ')'
    text = re.sub(key,dic[key],text)    
print("After replacement:\n",text)






