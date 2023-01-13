# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 15:27:47 2022

@author: User
"""

import os

os.chdir('location')

import glob #get multiple files
path = "location/*.txt" #define path for files
#this should be a folder containing a series of date lists extracted from subreddits using subreddit_extraction.py
#that is, a series of text files, each containing a list of dates in unix epoch format

with open('location/all_average_dates_table.txt', 'w', encoding = 'latin-1') as outfile:
   for filename in glob.glob(path): #cycle through each file in the glob list
      with open(filename,) as infile:
         datelist = [line.strip() for line in infile]
         while("" in datelist):
            datelist.remove("")
         int_datelist = [int(float(x)) for x in datelist]
         average_date = sum(int_datelist) / len(int_datelist)
         outfile.write(str(filename)) #printing each filename (presumably identifying the subreddit in question)
         outfile.write(" ")
         outfile.write(str(average_date)) #the average post/comment date for each subreddit
         outfile.write("\n")
         
outfile.close()