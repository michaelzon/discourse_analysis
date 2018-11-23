from textblob import TextBlob
import itertools
import nltk

# mooie woordenlijst deels zonder meta data.

text = open("De_Volkskrant_2017_1.TXT")

# reading the file, save it in the variable blob
text = text.read()
# text = "Blij vrolijk gelukkig mooie dag zon plantjes"
blob = TextBlob(text)

ruis = ["DOCUMENTS", "SECTION", "LENGTH", "LOAD-DATE", "LANGUAGE",
        "PUBLICATION-TYPE", "JOURNAL-CODE", "BYLINE", "All", "Rights",
        "Reserved", "Copyright"]


for word in blob.words:
    if not any(x in word for x in ruis):
       word = word.lower()
       print(word)

# i = 0
# with open("pos_words.txt", "r") as posWords:
#     while i < len(pos_words)
