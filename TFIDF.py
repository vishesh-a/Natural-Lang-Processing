#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 16:18:02 2019

@author: vishesh
"""

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

s1 = "Today is beautiful."
s2 = "Today is not beautiful"

response = vectorizer.fit_transform([s1,s2])

print(response)