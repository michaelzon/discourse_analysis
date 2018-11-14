from textblob import TextBlob
import itertools
import nltk

# mooie woordenlijst deels zonder meta data.

text = open("NRC_SAMPLE.TXT")

# reading the file, save it in the variable blob
text = text.read()
# text = "Blij vrolijk gelukkig mooie dag zon plantjes"
blob = TextBlob(text)

ruis = ["DOCUMENTS", "SECTION", "LENGTH", "LOAD-DATE", "LANGUAGE",
        "PUBLICATION-TYPE", "JOURNAL-CODE", "BYLINE", "All", "Rights",
        "Reserved", "Copyright"]


for lines in blob:
    if not any(x in s for x in ruis):
       print(s)
