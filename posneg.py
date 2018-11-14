from textblob import TextBlob
import itertools
import nltk
import os
import sys

# open the files with positive and negative words
positivesList = open("pos_dutch_2.txt")
negativesList = open("neg_dutch_2.txt")

positives = []
negatives = []

# store the words in seperate lists
for lines in positivesList:
    lines = lines.lower()
    positives.append(lines.strip("\n"))

for lines in negativesList:
    lines = lines.lower()
    negatives.append(lines.strip("\n"))

# print("Pos list:", positives)
# print("Neg list:", negatives)

posWordsWithSpace = []
negWordsWithSpace = []

for pos in positives:
    if " " in pos:
        posWordsWithSpace.append(pos)

for neg in negatives:
    if " " in neg:
        negWordsWithSpace.append(neg)

print(posWordsWithSpace)
print(negWordsWithSpace)
