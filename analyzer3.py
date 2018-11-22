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

for neg in negList:
    if " " in neg:
        negSpaces.append(neg)


l1 = ["ten einde raad", "oude vrijster", "boef"]

joinedl1 = []



for i in range(len(l1)):
    l1[i].split(" ")
    # if " " + " " in l1[i]:
    #     print('yes')
    # else:
    #     print("no")

print(l1)

# for i in range(len(posSpaces)):
#     print(posSpaces[i])
#
# for i in range(len(negSpaces)):
#     print(negSpaces[i])
#
# oneSpace = []
#
# for i in range(len(posSpaces)):
#     if posSpace[i] ==  + " "

# text = open("ontslag.txt")
#
# # reading the article, using TextBlob library to seperate each word
# text = text.read()
# blob = TextBlob(text)
#
# # make a list for all the words in the articles
# wordList = []
#
# # and store every word in that list
# for word in blob.words:
#    word = word.lower()
#    wordList.append(word)
#
# print('wordlist1', wordList)
#
# negOntslag = ["de oude vrijster", "ontslag genomen", "ten einde raad", "boos", "pak slaag", "verkeerd voorstellen"]
#
# print("negontslag", negOntslag)
#
# # at the end of a string item, merge it with the adjacent item
# s = "".join(negOntslag)
#
# n = []
#
# for i in wordList:
#     if i in s:
#         n.append(i)
#
# print('newnegOntslag', n)
#
# c = 0
#
# for i in n:
#     if c == len(n) - 2:
#         break
#     if (n[c] + " " + n[c+1]):
#         word = n[c] + " " + n[c+1]
#         print('WORD2', word)
#         if word in negOntslag:
#             print("word in negontslag", word)
#             ix1 = wordList.index(n[c])
#             ("ix1", ix1)
#             del wordList[ix1: ix1+2]
#             wordList.insert(ix1,word)
#     if (n[c] + " " + n[c+1] + " " + n[c+2]):
#         word = n[c] + " " + n[c+1] + " " + n[c+2]
#         print('WORD3', word)
#         if word in negOntslag:
#             print("word in negontslag", word)
#             ix1 = wordList.index(n[c])
#             ("ix1", ix1)
#             del wordList[ix1: ix1+2: ix1+3]
#             wordList.insert(ix1,word)
#     c += 1
#
# print('newWordlist', wordList)
#
#
#
#
#



# # variables for the frequencies of negative and positive words in articles
# amountPos = 0
# amountNeg = 0
#
# count = 0
#
# # if a word from the article is included in either positive or negative word list
# for word in wordList:
#     # print("words",count, word)
#     count += 1
#     for pos in posList:
#         if word == pos:
#             # print("positief woord ^")
#
#             # increment the frequency of positive words
#             amountPos += 1
#     for neg in negList:
#         if word == neg:
#             # print("negatief woord ^")
#
#             # or increment the frequency of negative words
#             amountNeg += 1
#
# print("aantal positieve woorden:", amountPos)
# print("aantal negatieve woorden:", amountNeg)
