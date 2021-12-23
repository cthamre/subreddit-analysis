# -*- coding: utf-8 -*-

"""

import re

f = open("location", "w", encoding='utf-8') #output location

doc = open("location", "r", encoding='utf-8') #location of the word list. words should be in separate lines
readdoc = doc.read()
input = readdoc.splitlines()

list = input

for i in list:   

    source = open("location", encoding="utf8") #location of the text file you want to analyze

    data = source.read()

    match= re.findall(i, data, re.IGNORECASE)

    length= len(match)

    print(i,"\t",length,file = f)

    source.close()
    
f.close()
doc.close()
