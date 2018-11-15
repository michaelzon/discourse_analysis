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

for lines in negatives:
    lines = lines.lower()
    negList.append(lines.strip("\n"))

posSpaces = []
negSpaces = []

for pos in posList:
    if " " in pos:
        posSpaces.append(pos)

for neg in negList:
    if " " in neg:
        negSpaces.append(neg)

print(posSpaces)
print(negSpaces)
