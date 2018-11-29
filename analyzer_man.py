from spaces import *
from article_list import article_list

neg_how_many_spaces(neg_list, neg_no_space, neg_one_space,
                    neg_two_spaces, neg_three_spaces, count)


pos_how_many_spaces(pos_list, pos_no_space, pos_one_space,
                    pos_two_spaces, pos_three_spaces, count)


# text = open("lil_sample.txt")
# text = open("samples/AD_Algemeen_Dagblad_2011.TXT")
text = open("ad_test/ad_1998.txt")

# reading the article, using TextBlob library to seperate each word
text = text.read()
blob = TextBlob(text)

# these are words that are bound to the meta-deta of the articlesfile
ruis = ["SECTION", "LENGTH", "LOAD-DATE", "LANGUAGE",
        "PUBLICATION-TYPE", "JOURNAL-CODE", "BYLINE", "All", "Rights",
        "Reserved", "Copyright", "krant", "Krant", "KRANT", "blz"]

# make a list for all the words in the articles
word_list = []
sample_size = 0

# and store every word in that list
for word in blob.words:
    if word == "DOCUMENTS":
        sample_size += 1
    if not any(x in word for x in ruis):
       word = word.lower()
       if word.isalpha():
           word_list.append(word)



# variables for the frequencies of negative and positive words in articles
amount_pos = 0
amount_neg = 0

phrases_four = []
phrases_three = []
phrases_two = []
phrases_one = []
amount_neg = 0

# amount of words in one phrase
phrase_q = 4

# iterating untill hitting last four words, otherwise iterating is out of range
for i in range(0, len(word_list) - phrase_q, 1):

    # until reaching the last word of the list, make for every four words one phrase
    if word_list[-1]:
        phrase = " "
        strings = word_list[i], word_list[i+1], word_list[i+2], word_list[i+3]
        phrase = phrase.join(strings)
        phrases_four.append(phrase)
        count = 0

for phrase in phrases_four:
    count += 1

    # create a new index for proper deletion of classified phrases
    index = count - 1

    # examine each negative phrase, and check if the same phrase exists in the phrases list
    for neg in neg_three_spaces:
        if phrase == neg:

            # manipulate words from list that are classified as either a pos
            # or neg phrase
            for j in range(0, phrase_q):
                word_list[index+j] = "!" + word_list[index+j]
            amount_neg += 1

    for pos in pos_three_spaces:
        if phrase == pos:
            for k in range(0, phrase_q):
                word_list[index+k] = "$" + word_list[index+k]

            amount_pos += 1

phrase_q = 3

for i in range(0, len(word_list) - phrase_q, 1):
    if word_list[-1]:
        phrase = " "
        strings = word_list[i], word_list[i+1], word_list[i+2]
        phrase = phrase.join(strings)
        phrases_three.append(phrase)
        count = 0

for phrase in phrases_three:
    count += 1
    index = count - 1
    for neg in neg_two_spaces:
        if phrase == neg:
            for j in range(0, phrase_q):
                word_list[index+j] = "!" + word_list[index+j]
            amount_neg += 1
    for pos in pos_two_spaces:
        if phrase == pos:
            for k in range(0, phrase_q):
                word_list[index+k] = "$" + word_list[index+k]
            amount_pos += 1

phrase_q = 2

# start at index zero, till one before end of the list
for i in range(0, len(word_list) - phrase_q, 1):

    if word_list[-1]:
        phrase = " "
        strings = word_list[i], word_list[i+1]
        phrase = phrase.join(strings)
        phrases_two.append(phrase)
        count = 0

for phrase in phrases_two:
    count += 1
    index = count - 1

    for neg in neg_one_space:
        if phrase == neg:
            for j in range(0, phrase_q):
                word_list[index+j] = "!" + word_list[index+j]
            amount_neg += 1

    for pos in pos_one_space:
        if phrase == pos:
            for k in range(0, phrase_q):
                word_list[index+k] = "$" + word_list[index+k]
            amount_pos += 1

phrase_q = 1

for i in range(0, len(word_list) - phrase_q, 1):
    if word_list[-1]:
        phrase = word_list[i]
        phrases_one.append(phrase)
        count = 0

for phrase in phrases_one:
    count += 1
    index = count - 1

    for neg in neg_no_space:
        if phrase == neg:

            for j in range(0, phrase_q):
                word_list[index+j] = "!" + word_list[index+j]
            amount_neg += 1

    for pos in pos_no_space:
        if phrase == pos:
            for k in range(0, phrase_q):
                word_list[index+k] = "$" + word_list[index+k]
            amount_pos += 1

print("( N =",sample_size,")")
print("amount_pos", amount_pos)
print("amount_neg", amount_neg)
