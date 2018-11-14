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

# text = open("De_Telegraaf_2011_2.TXT")
text = open("De_Volkskrant_2017_1.TXT")
# text = open("NRC_SAMPLE.TXT")


# reading the article, using TextBlob library to seperate each word
text = text.read()
blob = TextBlob(text)

# these are words that are bound to the meta-deta of the articlesfile
ruis = ["DOCUMENTS", "SECTION", "LENGTH", "LOAD-DATE", "LANGUAGE",
        "PUBLICATION-TYPE", "JOURNAL-CODE", "BYLINE", "All", "Rights",
        "Reserved", "Copyright", "krant", "Krant", "KRANT"]

# make a list for all the words in the articles
wordList = []

# and store every word in that list
for word in blob.words:
    if not any(x in word for x in ruis):
       word = word.lower()
       wordList.append(word)

# # code for checking the wordlist:
# count = 0
# for each in wordList:
#     print(count, each)
#     count += 1

# variables for the frequencies of negative and positive words in articles
amountPos = 0
amountNeg = 0

count = 0

# if a word from the article is included in either positive or negative word list
for word in wordList:
    print("words",count, word)
    count += 1
    for pos in positives:
        if word == pos:
            print("positief woord ^")

            # increment the frequency of positive words
            amountPos += 1
    for neg in negatives:
        if word == neg:
            print("negatief woord ^")

            # or increment the frequency of negative words
            amountNeg += 1


print("aantal positieve woorden:", amountPos)
print("aantal negatieve woorden:", amountNeg)
