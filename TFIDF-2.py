#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 16:19:25 2019

@author: vishesh
"""

import pandas as pd
import math
import numpy as np

def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count/float(bowCount)
    return tfDict

def computeIDF(docList):
    import math
    idfDict = {}
    N = len(docList)
    
    idfDict = dict.fromkeys(docList[0].keys(), 0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] += 1
    
    for word, val in idfDict.items():
        idfDict[word] = math.log10(N / float(val))
        
    return idfDict

def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val*idfs[word]
    return tfidf

def l2_norm(a):
    return math.sqrt(np.dot(a, a))

def cosine_similarity(a, b):
    return np.dot(a,b) / (l2_norm(a) * l2_norm(b))


s1 = "Today is beautiful."
s2 = "Today is not beautiful."

bowA = s1.split(" ")
bowB = s2.split(" ")

bowBwordSet = set(bowA).union(set(bowB))

wordSet = set(bowA).union(set(bowB))

wordDictA = dict.fromkeys(wordSet, 0) 
wordDictB = dict.fromkeys(wordSet, 0)


for word in bowA:
    wordDictA[word]+=1
    
for word in bowB:
    wordDictB[word]+=1


print(pd.DataFrame([wordDictA, wordDictB]))
print("\n\n\n\n")

tfBowA = computeTF(wordDictA, bowA)
tfBowB = computeTF(wordDictB, bowB)

print("TF\n")

print(tfBowA)

print("\n")

print(tfBowB)

print("\n\n\n\n")

idfs = computeIDF([wordDictA, wordDictB])

print("IDF\n")
print(idfs)
print("\n\n\n\n")


tfidfBowA = computeTFIDF(tfBowA, idfs)
tfidfBowB = computeTFIDF(tfBowB, idfs)

print("TF-IDF\n")
print(pd.DataFrame([tfidfBowA, tfidfBowB]))
print("\n\n\n\n")

"""
cs = cosine_similarity(tfidfBowA.values(), tfidfBowB.values())
print(cs)
"""