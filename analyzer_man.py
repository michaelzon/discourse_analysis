from textblob import TextBlob

# open the files with negative words
negatives = open("neg_dutch_2.txt")

neg_list = []

# push all the words from text file to list
for lines in negatives:
    lines = lines.lower()
    neg_list.append(lines.strip("\n"))

negatives.close()

neg_no_space = []
neg_one_space = []
neg_two_spaces = []
neg_three_spaces = []

count = 0

# deviding the negative phrases in classes corresponding to the quantity of words
def neg_how_many_spaces(neg_list, neg_no_space, neg_one_space, neg_two_spaces,
                        neg_three_spaces, count):

    # read every word in the list with negative words
    for i in range(len(neg_list)):

        # every word is a phrase, because there are "words" with spaces
        phrase = neg_list[i]

        # look at every character and assign the phrase to a list
        # that correspondes with the number of spaces in it
        for j in range(len(phrase)):
            if phrase[j] == " ":
                count += 1
        if phrase[-1]:
            if count == 1:
                neg_one_space.append(phrase)
            elif count == 2:
                neg_two_spaces.append(phrase)
            elif count == 3:
                neg_three_spaces.append(phrase)
            else:
                neg_no_space.append(phrase)

            # reset the counter to avoid the total sum of spaces in a list
            count = 0

    return neg_list, neg_no_space, neg_one_space, neg_two_spaces,
    neg_three_spaces, count

neg_how_many_spaces(neg_list, neg_no_space, neg_one_space,
                    neg_two_spaces, neg_three_spaces, count)

# open the files with positive words
positives = open("pos_dutch_2.txt")

pos_list = []

# push all the words from text file to list
for lines in positives:
    lines = lines.lower()
    pos_list.append(lines.strip("\n"))

positives.close()

pos_no_space = []
pos_one_space = []
pos_two_spaces = []
pos_three_spaces = []
count = 0

# deviding the positive phrases in classes corresponding to the quantity of words
def pos_how_many_spaces(pos_list, pos_no_space, pos_one_space, pos_two_spaces,
                        pos_three_spaces, count):

    # read every word in the list with positive words
    for i in range(len(pos_list)):

        # every word is a phrase, because there are "words" with spaces
        phrase = pos_list[i]

        # look at every character and assign the phrase to a list
        # that correspondes with the number of spaces in it
        for j in range(len(phrase)):
            if phrase[j] == " ":
                count += 1
        if phrase[-1]:
            if count == 1:
                pos_one_space.append(phrase)
            elif count == 2:
                pos_two_spaces.append(phrase)
            elif count == 3:
                pos_three_spaces.append(phrase)
            else:
                pos_no_space.append(phrase)

            # reset the counter to avoid the total sum of spaces in a list
            count = 0

    return pos_list, pos_no_space, pos_one_space, pos_two_spaces,
    pos_three_spaces, count

pos_how_many_spaces(pos_list, pos_no_space, pos_one_space,
                    pos_two_spaces, pos_three_spaces, count)


# text = open("lil_sample.txt")
text = open("AD_Algemeen_Dagblad_2011.TXT")

# reading the article, using TextBlob library to seperate each word
text = text.read()
blob = TextBlob(text)

# these are words that are bound to the meta-deta of the articlesfile
ruis = ["DOCUMENTS", "SECTION", "LENGTH", "LOAD-DATE", "LANGUAGE",
        "PUBLICATION-TYPE", "JOURNAL-CODE", "BYLINE", "All", "Rights",
        "Reserved", "Copyright", "krant", "Krant", "KRANT", "blz"]

# make a list for all the words in the articles
word_list = []

# and store every word in that list
for word in blob.words:
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


print("amount_pos", amount_pos)
print("amount_neg", amount_neg)
