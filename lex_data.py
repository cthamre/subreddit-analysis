# -*- coding: utf-8 -*-

#define output file locations/names
e = open('wordcounts.txt', 'w', encoding="utf-8-sig") #open output file for raw word counts
f = open('varpermils.txt', 'w', encoding="utf-8-sig") #open output file for the per million stats
g = open('ratios.txt', 'w', encoding="utf-8-sig") #open output file for ratios
h = open('corpuswordcounts.txt', 'w', encoding="utf-8-sig") #open output file for word counts of corpora

#SETTING UP COLUMNS IN EACH OUTPUT FILE

#prepare columns for raw word counts
e.write("Subcorpus") #first column name
#cycle through variables and print names
for row in open('variables.txt', 'r', encoding="utf-8-sig"): #open variables file and cycle through each row
   pair = row.rstrip().split(",") #split the row by the comma
   for variant in pair: #cycle through each variant
       e.write(","+str(variant)) #print the name of the variant
e.write("\n") #line break

#prepare columns for varpermils
f.write("Subcorpus") #first column name
#cycle through variables and print names
for row in open('variables.txt', 'r', encoding="utf-8-sig"): #open variables file and cycle through each row
   pair = row.rstrip().split(",") #split the row by the comma
   for variant in pair: #cycle through each variant
       f.write(","+str(variant)) #print the name of the variant
f.write("\n") #line break

#prepare columns for ratios
g.write("Subcorpus") #first two column names
#cycle through variables and print each row with underscore
for row in open('variables.txt', 'r', encoding="utf-8-sig"): #open variables file and cycle through each row
   pair = row.rstrip().split(",") #split the row by the comma
   g.write(","+str(pair[0]+"_"+str(pair[1]))) #print the names of the variants joined by an underscore
g.write("\n") #line break

#prepare columns for word counts of texts
h.write("Subcorpus,WordCount\n") #column names

#EXTRACTING THE DATA

import re #regular expressions
import glob #get multiple files
path = "Corpora\*.txt" #define path for files

for filename in glob.glob(path): #cycle through each file in the glob list
   with open(filename, 'r', encoding="utf-8-sig") as file: #while that file is open
      wc = 0 #reset wordcount variable to 0 before going through each file
      v1count = 0 #reset variable counts to 0 before going through each file
      v2count = 0
      
      #---get wordcount for subcorpus file---
      
      for line in file: #cycle through each line in file
          words = line.split(" ") #split by spaces
          wc += len(words) #add the length of the line in words to the wordcount total
          names = str(filename) #folder and filename
          names = names.split(".") #split '.txt' from filename
          names = str(names[0])
          names = names.split("\\") #split 'corpora' from filename
          name = str(names[1]) #extract filename
      h.write(str(name)+","+str(wc)+"\n") #print filename and word count
      
      #---get variable counts and calculate ratios---
   
   e.write(str(name)) #print filename in raw word counts file
   f.write(str(name)) #print filename in varpermils file
   g.write(str(name)) #print filename ratios file
      
   for row in open('variables.txt', 'r', encoding="utf-8-sig"): #open variables file and cycle through each row

      #find count for first variant
      with open(filename, 'r', encoding="utf-8-sig") as file: #while that file is open
         pair = row.rstrip().split(",") #split the row by the comma
         variant1 = pair[0] #assign each list/pair member to a variable
         variant2 = pair[1]
         
         data = file.read()
         search = r"\b"+str(variant1)+r"\b" #the thing we're looking for is the variant surrounded by word boundary characters
         match1 = re.findall(search, data, re.IGNORECASE)
         v1count = len(match1)
         
         #print raw word count for first variant in raw counts file
         e.write(","+str(v1count))
         
         v1permil = ((v1count * 1000000) / wc) #calculate per million
         f.write(","+str(v1permil))
         print("Total for "+str(variant1)+" in "+str(name)+": "+str(v1count))

      #find count for second variant
      with open(filename, 'r', encoding="utf-8-sig") as file: #while that file is open
         pair = row.rstrip().split(",") #split the row by the comma
         variant1 = pair[0] #assign each list/pair member to a variable
         variant2 = pair[1]   
         
         data = file.read()
         search = r"\b"+str(variant2)+r"\b" #the thing we're looking for is the variant surrounded by word boundary characters
         match2 = re.findall(search, data, re.IGNORECASE)
         v2count = len(match2)
         
         #print raw word count for second variant in raw counts file
         e.write(","+str(v2count))
         
         v2permil = ((v2count * 1000000) / wc) #calculate per million
         f.write(","+str(v2permil)) #print per million
         print("Total for "+str(variant2)+" in "+str(name)+": "+str(v2count))
         
         #calculate ratio
         try: #try to do this
            ratio = (v1permil / (v1permil + v2permil))
         except ZeroDivisionError: #if you get a divide by zero error
            ratio = "NA" #make it a string variable that says NA
         else: #otherwise do this
            ratio = (v1permil / (v1permil + v2permil))
         g.write(","+str(ratio)) #print ratio
   e.write("\n") #line breaks
   f.write("\n")
   g.write("\n")

e.close() #close output 
f.close()
g.close()
h.close()
