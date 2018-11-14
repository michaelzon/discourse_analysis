from textblob import TextBlob
import itertools
import nltk
import os
import sys


# # absolute paths to lists
# positives = os.path.join(sys.path[0], "pos_dutch.txt")
# negatives = os.path.join(sys.path[0], "neg_dutch.txt")


positiveWords = open("pos_dutch_2.txt")

positiveWords = positiveWords.read()

blobBlob = TextBlob(positiveWords)

positiveWords = []

for posWord in blobBlob.words:
    positiveWords.append(posWord)

print("positive words list:", positiveWords)

negativeWords = open("neg_dutch_2.txt")

negativeWords = negativeWords.read()

blobBlobBlob = TextBlob(negativeWords)

negativeWords = []

for negWord in blobBlobBlob.words:
    negativeWords.append(negWord)

print("negative words list:", negativeWords)

# positiveWords.close()

# get words from article
def getWords():
    # mooie woordenlijst deels zonder meta data.
    text = open("De_Volkskrant_2017_1.TXT")

    # reading the file, save it in the variable blob
    text = text.read()
    # text = "Blij vrolijk gelukkig mooie dag zon plantjes"
    blob = TextBlob(text)

    ruis = ["DOCUMENTS", "SECTION", "LENGTH", "LOAD-DATE", "LANGUAGE",
            "PUBLICATION-TYPE", "JOURNAL-CODE", "BYLINE", "All", "Rights",
            "Reserved", "Copyright"]

    wordList = []

    for word in blob.words:
        if not any(x in word for x in ruis):
           word = word.lower()
           wordList.append(word)

    # print(wordList)

# getWords()
#
# if __name__ == '__main__':
#     main()
