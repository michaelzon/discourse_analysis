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


# for i in range(len(pos_three_spaces)):
#     print("pos_three_spaces[i]",i, pos_three_spaces[i])
#
# for i in range(len(pos_two_spaces)):
#     print("pos_two_spaces[i]",i, pos_two_spaces[i])
#
# for i in range(len(pos_one_space)):
#     print("pos_one_space[i]",i, pos_one_space[i])
#
# for i in range(len(pos_no_space)):
#     print("pos_no_space[i]",i, pos_no_space[i])


# for i in range(len(neg_three_spaces)):
#     print("neg_three_spaces[i]",i, neg_three_spaces[i])
#
# for i in range(len(neg_two_spaces)):
#     print("neg_two_spaces[i]",i, neg_two_spaces[i])
#
# for i in range(len(neg_one_space)):
#     print("neg_one_space[i]",i, neg_one_space[i])
#
# for i in range(len(neg_no_space)):
#     print("neg_no_space[i]",i, neg_no_space[i])

text = open("lil_sample.txt")
# text = open("De_Telegraaf_2011_2.TXT")

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

# PHRASE 4
for i in range(len(word_list)):
    print(i,word_list[i])

flag = True

while flag == True:

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
        print("phrase4", count, phrase)
        count += 1

        # create a new index for proper deletion of classified phrases
        index = count - 1

        # examine each negative phrase, and check if the same phrase exists in the phrases list
        for neg in neg_three_spaces:
            if phrase == neg:
                print("negatief woord^")
                print("word_list[index]",index, word_list[index])

                # deleting words from list that are classified as either a pos
                # or neg phrase
                for j in range(0, phrase_q):
                    print("(index), delete:", index, word_list[index])
                    del word_list[index]
                for i in range(len(word_list)):
                    print('nieuwe woordenlijst', i,word_list[i])
                amount_neg += 1

        for pos in pos_three_spaces:
            if phrase == pos:
                print("positief woord^")

                print("index & word_list[index]", index, word_list[index-phrase_q])

                for k in range(0, phrase_q):
                    print("delete:", word_list[index-phrase_q])
                    del word_list[index-phrase_q]
                amount_pos += 1

    print("amount_neg", amount_neg)
    print("amount_pos", amount_pos)

    for i in range(len(word_list)):
        print('nieuwe woordenlijst', i,word_list[i])

    phrase_q = 3

    for i in range(0, len(word_list) - phrase_q, 1):
        if word_list[-1]:
            phrase = " "
            strings = word_list[i], word_list[i+1], word_list[i+2]
            phrase = phrase.join(strings)
            phrases_three.append(phrase)
            count = 0

    for phrase in phrases_three:
        print("phrase3", count, phrase)
        count += 1

        index = count - 1

        for neg in neg_two_spaces:
            if phrase == neg:
                print("negatief woord^")
                print('index', index)
                print("word_list[index]",word_list[index])

                # for j in range(0, phrase_q):
                #     print("delete:", word_list[index])
                #     del word_list[index]
                amount_neg += 1

        for pos in pos_two_spaces:
            if phrase == pos:
                print("positief woord^")
                print('index', index)

                print("word_list[index]", word_list[index-phrase_q])

                for k in range(0, phrase_q):
                    print("delete:", word_list[index-phrase_q])
                    del word_list[index-phrase_q]
                amount_pos += 1

    print("amount_neg", amount_neg)
    print("amount_pos", amount_pos)

    for i in range(len(word_list)):
        print('nieuwe woordenlijst', i,word_list[i])

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
        print("phrase2", count, phrase)
        count += 1

        index = count - 1

        for neg in neg_one_space:
            if phrase == neg:
                print("negatief woord^")
                print('index', index)
                print("word_list[index]",word_list[index])

                # for j in range(0, phrase_q):
                #     print("delete:", word_list[index])
                #     del word_list[index]
                amount_neg += 1

        for pos in pos_one_space:
            if phrase == pos:
                print("positief woord^")
                print('index', index)

                print("word_list[index]", word_list[index-phrase_q])

                for k in range(0, phrase_q):
                    print("delete:", word_list[index-phrase_q])
                    del word_list[index-phrase_q]
                amount_pos += 1

    print('amount_neg', amount_neg)
    print("amount_pos", amount_pos)

    for i in range(len(word_list)):
        print('nieuwe woordenlijst', i,word_list[i])

    # nothing has to be delete... right???? (pos/neg validity)(don't forget to take a look at this)
    phrase_q = 1
    for i in range(0, len(word_list) - phrase_q, 1):
        if word_list[-1]:
            phrase = word_list[i]
            phrases_one.append(phrase)
            count = 0

    for phrase in phrases_one:
        print("phrase1", count, phrase)
        count += 1

        index = count - 1

        for neg in neg_no_space:
            if phrase == neg:
                print("negatief woord^")
                print('index', index)
                print("word_list[index]",word_list[index])
                print("delete:", word_list[index])
                # del word_list[index]
                amount_neg += 1

        for pos in pos_no_space:
            if phrase == pos:
                print("positief woord^")
                print('index', index)
                print("word_list[index]",word_list[index])
                for k in range(0, phrase_q):
                    print("delete:", word_list[index-phrase_q])
                    del word_list[index-phrase_q]
                amount_pos += 1
                amount_pos += 1

    for i in range(len(word_list)):
        print('nieuwe woordenlijst', i,word_list[i])
    print("amount_neg", amount_neg)
    print("amount_pos", amount_pos)

# de boeren zagen de oude vrijster op de loer liggen terwijl ze een hekel hebben aan haar, toen moesten ze de varkens in de steek laten, ze waren ten einde raad maar ook boos, maarja

# Gelukkig was het niet voor de hand liggend dat dol zijn op boodschappen doen bovenmenselijk was, media
