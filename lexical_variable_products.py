# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 14:52:35 2022

@author: User
"""

import os

#define directory
os.chdir("location")

#define output file locations/names
f = open('location.txt', 'w', encoding="utf-8-sig") #open output file for raw counts
g = open('location.txt', 'w', encoding="utf-8-sig") #open output file for ratios
h = open('location.txt', 'w', encoding="utf-8-sig") #open output file for word counts

#SETTING UP COLUMNS IN EACH OUTPUT FILE

#prepare columns for varpermils
f.write("City,Country") #first two column names
#cycle through variables and print names
for row in open('location.csv', 'r', encoding="utf-8-sig"): #open variables file and cycle through each row
                                                            #this should be a csv with two columns and as many rows as you wish
                                                            #each row contains the two variants of a lexical variable
   pair = row.rstrip().split(",") #split the row by the comma
   for variant in pair: #cycle through each variant
       f.write(","+str(variant)) #print the name of the variant
f.write("\n") #line break

#prepare columns for ratios
g.write("City,Country") #first two column names
#cycle through variables and print each row with underscore
for row in open('location.csv', 'r', encoding="utf-8-sig"): #open variables file and cycle through each row
   pair = row.rstrip().split(",") #split the row by the comma
   g.write(","+str(pair[0]+"_"+str(pair[1]))) #print the names of the variants joined by an underscore
g.write("\n") #line break

#prepare columns for wordcounts
h.write("City Country WordCount\n") #column names

#EXTRACTING THE DATA

import re #regular expressions
import glob #get multiple files
path = "*/*.txt" #define path for files

for filename in glob.glob(path): #cycle through each file in the glob list
   with open(filename, 'r', encoding="utf-8-sig") as file: #while that file is open
      wc = 0 #reset wordcount variable to 0 before going through each file
      v1count = 0 #reset variable counts to 0 before going through each file
      v2count = 0
      
      #---get wordcount for subcorpus file---
      
      for line in file: #cycle through each line in file
          words = line.split(" ") #split by spaces
          wc += len(words) #add the length of the line in words to the wordcount total
          names = str(os.path.splitext(filename)[0]) #extract folder and file name
          names = names.split("\\") #split country and city name
          city = str(names[1]) #extract city name
          country = str(names[0]) #extract country name
      h.write(str(city)+" "+str(country)+" "+str(wc)+"\n") #print city name, country name, and word count
      
      #---get variable counts and calculate ratios---
      
   f.write(str(city)+","+str(country)) #print city name and country name in varpermils file
   g.write(str(city)+","+str(country)) #print city name and country name ratios file
      
   for row in open('location.csv', 'r', encoding="utf-8-sig"): #open variables file and cycle through each row

      #find count for first variant
      with open(filename, 'r', encoding="utf-8-sig") as file: #while that file is open
         pair = row.rstrip().split(",") #split the row by the comma
         variant1 = pair[0] #assign each list/pair member to a variable
         variant2 = pair[1]
         
         data = file.read()
         search = r"\b"+str(variant1)+r"\b" #the thing we're looking for is the variant surrounded by word boundary characters
         match1 = re.findall(search, data, re.IGNORECASE)
         v1count = len(match1)
         
         v1permil = ((v1count * 1000000) / wc) #calculate per million
         f.write(","+str(v1permil))
         print("Total for "+str(variant1)+" in "+str(city)+": "+str(v1count))

      #find count for second variant
      with open(filename, 'r', encoding="utf-8-sig") as file: #while that file is open
         pair = row.rstrip().split(",") #split the row by the comma
         variant1 = pair[0] #assign each list/pair member to a variable
         variant2 = pair[1]   
         
         data = file.read()
         search = r"\b"+str(variant2)+r"\b" #the thing we're looking for is the variant surrounded by word boundary characters
         match2 = re.findall(variant2, data, re.IGNORECASE)
         v2count = len(match2)
         
         v2permil = ((v2count * 1000000) / wc) #calculate per million
         f.write(","+str(v2permil)) #print per million
         print("Total for "+str(variant2)+" in "+str(city)+": "+str(v2count))
         
         #calculate ratio
         try: #try to do this
            ratio = (v1permil / (v1permil + v2permil))
         except ZeroDivisionError: #if you get a divide by zero error
            ratio = "NA" #make it a string variable that says NA
         else: #otherwise do this
            ratio = (v1permil / (v1permil + v2permil))
         g.write(","+str(ratio)) #print ratio
   f.write("\n") #line breaks
   g.write("\n")
   
f.close() #close output
g.close()
h.close()