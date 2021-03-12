# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re
import sys

def split_in_lines(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        return file.read().split('\n')
        
def split_at_tabs(list_of_lines):
    new_list = []
    for line in list_of_lines:
        new_line = line.split('\t')
        new_list.append(new_line)
    return new_list
    
def open_write(filename):
    return open(filename,'w',encoding="utf-8") 
    
    
'''
text = "Juhuu! Es ist Fr&#x00FC;hling &#x1F600; und die &#x2600;&#xFE0F; \
scheint! &#x2753; Wo lebstu? Hier Schei&#x00DF; Wetter &#x1F327; \
&#x1F620; &#x26A1;..."

'''

html_text = split_in_lines("emojis.html")
text = [html_text[line-1] for line in range(len(html_text)) if line==5 or line==7]
text = " ".join(text)


'''
dic = {'&#x00FC;':'ü', '&#x1F600;':'grinning face', '&#x2600;&#xFE0F;':'sun',
       '&#x2753;':'question mark', '&#x00DF;':'ß', '&#x1F327;':'cloud with rain',
       '&#x1F620;':'angry face', '&#x26A1;':'high voltage'}
'''           


emojis_lines = split_in_lines("emoji-test_tab.txt")
sp_letters_lines = split_in_lines("Unicode_UTF-8-character_table_tab.txt")

emojis_lines = split_at_tabs(emojis_lines)
sp_letters_lines = split_at_tabs(sp_letters_lines)

specials = re.compile("&#x[A-F0-9&#x;]{4,12};")
list_of_specials = re.findall(specials,text)
dic = {}
for line in emojis_lines:
    if line[0] in list_of_specials:
        dic[line[0]] = line[2]
for line in sp_letters_lines:
    if line[0] in list_of_specials:
        dic[line[0]] = line[1]
print(dic)

    
specials = re.compile("&#x[A-F0-9&#x;]{4,12};")
list_of_specials = re.findall(specials,text)
#file = open_write("found html-entities.txt") 
file = open_write(sys.argv[1])
for code in list_of_specials:
    print(code,": ",dic[code])
    file.write(code) 
    file.write(" : ") 
    file.write(dic[code]) 
    file.write("\n") 
file.close() 

'''
text1 = text
for key in dic:
    dic[key] = str("("))
    text1 = re.sub(key,dic[key],text1)
    
print("Starttext:\n",text,'\n\n')
print("Nach Ersetzung:\n",text1)
'''





