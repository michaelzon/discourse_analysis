from textblob import TextBlob
import itertools
import nltk

# lines = []
#
# with open ("De_Telegraaf_2011_2.TXT", "r") as f:
#
#     for line in itertools.islice(f, 16, None):
#         for i in range(f):
#             lines = line[i]
#
# print(lines)

# text = open("De_Telegraaf_2011_2.TXT")
#
# text = text.read()
#
# blob = TextBlob(text)
#
# print(blob.words)
#
# # words = blob.words
# #
# # wordList = list(words)
# #
# # print(wordList)
#
# text.close()

# nu heb ik het artikel zonder de eerste 16 regels
with open ("NRC_SAMPLE.TXT", "r") as f:
    articles = list(f)

# articles = articles[16:]

articles = str(articles)

blob = TextBlob(articles)

count = 0

ruis = ["SECTION:", "LENGTH:", "LOAD-DATE:", "LANGUAGE:", "PUBLICATION-TYPE:", "JOURNAL-CODE:"]

# i = 0
# while i < len(ruis):
#     print(ruis[i])
#     i += 1

for word in blob.words:
    word = str(word.lower())
    word = word.strip('\n')
    if word:
    # if word.startswith("a"):
        count += 1
        print(count,type(word), word)


# ik heb nu alles lowercase woord voor woord uitgeprint maar wel veel meta data
