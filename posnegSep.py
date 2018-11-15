from textblob import TextBlob
import itertools
import nltk
import os
import sys

# open the files with positive and negative words
positives = open("pos_dutch_2.txt")
negatives = open("neg_dutch_2.txt")

posWords = positives.read()
blob = TextBlob(posWords)

posList = []

for pos in blob.words:
   pos = pos.lower()
   posList.append(pos)

negWords = negatives.read()
blob = TextBlob(negWords)

negList = []

for neg in blob.words:
   neg = neg.lower()
   negList.append(neg)

print(posList)
print(negList)
