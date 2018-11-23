from textblob import TextBlob


# open the file with articles
# text = open("De_Volkskrant_2017_1.TXT")
text = open("De_Telegraaf_2011_2.TXT")

# reading the file, save it in the variable blob
text = text.read()
# text = "Blij vrolijk gelukkig mooie dag zon plantjes"
blob = TextBlob(text)

# storing all words from file in words
# words = blob.words

# convert it to a python list for usebility
# wordList = list(words)


# for word in blob.words:
#     if "x" in word:
#         print(word)


# print(blob.sentences)

# for s in blob.sentences:
#     if len(s) > 280:
#         print(s)

# for s in blob.sentences:
#     if "verraad" in s:
#         print(s)

# print(blob.np_counts)

# dictionary = blob.np_counts
# dictionary = dict(dictionary)
#
# rankedList = sorted(dictionary, key = dictionary.get, reverse = True)
#
# for i in range(0, len(rankedList)):
#     key = rankedList[i]
#     value = dictionary[key]
#     print(key.capitalize()+ " repeats", str(value) + " times")


# for s in blob.sentences:
#     if blob.polarity < 0.0:
#         print(s)

print(blob)
# print(blob.translate(to="en"))

text.close()
