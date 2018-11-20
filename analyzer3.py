#!/usr/bin/python
from textblob import TextBlob
import itertools
import nltk
import os
import sys

# open the files with positive and negative words
positives = open("pos_dutch_2.txt")
negatives = open("neg_dutch_2.txt")

posList = []
negList = []

for lines in positives:
    lines = lines.lower()
    posList.append(lines.strip("\n"))

# print("posList", posList)

for lines in negatives:
    lines = lines.lower()
    negList.append(lines.strip("\n"))

# print("negList", negList)

posSpaces = []
negSpaces = []

for pos in posList:
    if " " in pos:
        posSpaces.append(pos)

# print("posSpaces", posSpaces)

for neg in negList:
    if " " in neg:
        negSpaces.append(neg)

# print("negSpaces", negSpaces)

text = open("ontslag.txt")

# reading the article, using TextBlob library to seperate each word
text = text.read()
blob = TextBlob(text)

# make a list for all the words in the articles
wordList = []

# and store every word in that list
for word in blob.words:
   word = word.lower()
   wordList.append(word)

print("wordList", wordList)



# variables for the frequencies of negative and positive words in articles
amountPos = 0
amountNeg = 0

count = 0

# if a word from the article is included in either positive or negative word list
for word in wordList:
    # print("words",count, word)
    count += 1
    for pos in posList:
        if word == pos:
            # print("positief woord ^")

            # increment the frequency of positive words
            amountPos += 1
    for neg in negList:
        if word == neg:
            # print("negatief woord ^")

            # or increment the frequency of negative words
            amountNeg += 1

print("aantal positieve woorden:", amountPos)
print("aantal negatieve woorden:", amountNeg)
