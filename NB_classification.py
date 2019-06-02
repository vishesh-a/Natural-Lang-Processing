#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 16:33:45 2019

@author: vishesh
"""

def gender_features(word):
    return {'last_letter':word[-1]}

print(gender_features("Sherlock"))

from nltk.corpus import names
import random
import nltk

labeled_names = ([(name,'male') for name in names.words('male.txt')]+[(name,'female') for name in names.words('female.txt')])

"print(labeled_names)"

random.shuffle(labeled_names)

"print(labeled_names)"

featuresets = [(gender_features(n),gender) for (n,gender) in labeled_names]

"print(featuresets)"

classifier = nltk.NaiveBayesClassifier.train(featuresets)

print("\n\n\n")

print(classifier.classify(gender_features("David")))
print(classifier.classify(gender_features("Michelle")))

test_set, test_set = featuresets[:750],featuresets[:750]

print(nltk.classify.accuracy(classifier,test_set))