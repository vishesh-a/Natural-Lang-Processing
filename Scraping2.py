#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 18:41:05 2019

@author: vishesh
"""

from urllib.request import urlopen # Wsed for opening the url
from bs4 import BeautifulSoup # Used for parsing the HTML script
from langdetect import detect # Used to detect the language

url = "https://www.bbc.com/hindi/india-47088054"
web_page = urlopen(url)

# Pasing the language using the lxml parser
soup = BeautifulSoup(web_page,"lxml")

z=""
k=""

# Extracting the data and splitting it into characters
for paragraph in soup.findAll("p"):
    z+=paragraph.text

# Set containg the required encodings which the characters may belomng to
set_word = {'mr', 'hi', 'ne'}

# Set of characters not recognized by langdetect
set_word2 = [' ','1','2','3','4','5','6','7','8','9','0']

# Printing the valid characters
for i in z:
    try:
        if (detect(i) in set_word):
            print (i)
    except:
        if (i in set_word2):
            print (i)
        else:
            print ("********* Invalid char ************")

# Merginging the characters back into the passage
for i in z:
    try:
        if (detect(i) in set_word):
            k+=i
    except:
        if (i in set_word2):
            k+=i
        else:
            k+=''
            
print(k)

#for i in z:
 #   try:
  #      whole_data[i]=detect(i)
   # except:
    #    print("Unknown char found")
        
#print (whole_data)
        
    
#import pandas as pd


"""      


for paragraph in soup.findAll("p"):
    print (paragraph.text)
"""