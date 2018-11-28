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

# def generator(phrase_q, word_list, phrases_one, phrases_two, phrases_three, phrases_four):
#     phrase_q = phrase_q
#     phrases_four = []
#     phrases_three = []
#     phrases_two = []
#     phrases_one = []
#
#     for i in range(0, len(word_list) - phrase_q, 1):
#         print("w00rdenlijst", i,word_list[i])
#         if word_list[-1]:
#             phrase = " "
#             if phrase_q == 4:
#                 strings = word_list[i], word_list[i+1], word_list[i+2], word_list[i+3]
#                 phrase = phrase.join(strings)
#                 phrases_four.append(phrase)
#             elif phrase_q == 3:
#                 strings = word_list[i], word_list[i+1], word_list[i+2]
#                 phrase = phrase.join(strings)
#                 phrases_three.append(phrase)
#             elif phrase_q == 2:
#                 strings = word_list[i], word_list[i+1]
#                 print("stringss", strings)
#                 phrase = phrase.join(strings)
#                 print("JOINstringsforPhrase", phrase)
#                 phrases_two.append(phrase)
#                 print("INBLOCKPHRASE", phrases_two)
#             elif phrase_q == 1:
#                 phrase = word_list[i]
#                 phrases_one.append(phrase)
#             count = 0
#     # print("phrases_twoINGEN", phrases_two)
#     return phrase_q, word_list, phrases_one, phrases_two, phrases_three, phrases_four

class Phraser():
    def __init__(self, phrase_q, word_list2, phrases_one, phrases_two, phrases_three, phrases_four):
        self.phrase_q = phrase_q
        self.word_list2 = word_list2
        self.phrase_one = []
        self.phrase_two = []
        self.phrase_three = []
        self.phrase_four = []

    # def generator(phrase_q, word_list2, phrases_one, phrases_two, phrases_three, phrases_four):
    def generator(self):

        for i in range(0, len(self.word_list2) - self.phrase_q, 1):
            print("w00rdenlijst", i,self.word_list2[i])
            if self.word_list2[-1]:
                phrase = " "
                if self.phrase_q == 4:
                    strings = self.word_list2[i], self.word_list2[i+1], self.word_list2[i+2], self.word_list2[i+3]
                    phrase = phrase.join(strings)
                    phrases_four.append(phrase)
                elif self.phrase_q == 3:
                    strings = self.word_list2[i], self.word_list2[i+1], self.word_list2[i+2]
                    phrase = phrase.join(strings)
                    phrases_three.append(phrase)
                elif self.phrase_q == 2:
                    strings = self.word_list2[i], self.word_list2[i+1]
                    print("stringss", strings)
                    phrase = phrase.join(strings)
                    print("JOINstringsforPhrase", phrase)
                    phrases_two.append(phrase)
                    print("INBLOCKPHRASE", phrases_two)
                elif self.phrase_q == 1:
                    phrase = self.word_list2[i]
                    phrases_one.append(phrase)
                count = 0
        # print("phrases_twoINGEN", phrases_two)
        return self.phrase_q, self.word_list2, phrases_one, phrases_two, phrases_three, phrases_four

# generator(4, word_list)
# generator(3, word_list)
# generator(2, word_list)
# generator(1, word_list)

# for phrase in phrases_four:
#     print("phrase4", count, phrase)
#     count += 1
#
# for phrase in phrases_three:
#     print("phrase3", count, phrase)
#     count += 1

phrase_q = 2
phrase_gen = Phraser(phrase_q, word_list, phrases_one, phrases_two, phrases_three, phrases_four)
# print("prhase_gen_",phrase_gen)

phrase_gen.generator()


for phrase in phrases_two:
    print("phrase2afterfirstGen", count, phrase)
    count += 1

print("123", word_list)
del word_list[1]
print("4566", word_list)

print("DELETE boeren")
print("GENERATOR:")
phrase_gen1 = Phraser(phrase_q, word_list, phrases_one, phrases_two, phrases_three, phrases_four)
phrase_gen1.generator()

print("WJIK")
print(phrases_two)
for phrase in phrases_two:
    print("phrase2!", phrase)
    count += 1

# for phrase in phrases_one:
#     print("phrase1", count, phrase)
#     count += 1

phrase_q = 4
for phrase in phrases_four:
    print("phrase4", count, phrase)
    count += 1
    index = count - 1
    for neg in neg_three_spaces:
        if phrase == neg:
            print("negatief woord^")
            print("word_list[index]",index, word_list[index])
            for j in range(0, phrase_q):
                print("(index), delete:", index, word_list[index])
                del word_list[index]
                generator(phrase_q, word_list)
                # for phrase in phrases_four:
                #     print("phrase444", count, phrase)
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



# phrase_q = 3
#
# for i in range(0, len(word_list) - phrase_q, 1):
#     if word_list[-1]:
#         phrase = " "
#         strings = word_list[i], word_list[i+1], word_list[i+2]
#         phrase = phrase.join(strings)
#         phrases_three.append(phrase)
#         count = 0
#
# for phrase in phrases_three:
#     print("phrase3", count, phrase)
#     count += 1
#
#     index = count - 1
#
#     for neg in neg_two_spaces:
#         if phrase == neg:
#             print("negatief woord^")
#             print('index', index)
#             print("word_list[index]",word_list[index])
#
#             # for j in range(0, phrase_q):
#             #     print("delete:", word_list[index])
#             #     del word_list[index]
#             amount_neg += 1
#
#     for pos in pos_two_spaces:
#         if phrase == pos:
#             print("positief woord^")
#             print('index', index)
#
#             print("word_list[index]", word_list[index-phrase_q])
#
#             for k in range(0, phrase_q):
#                 print("delete:", word_list[index-phrase_q])
#                 del word_list[index-phrase_q]
#             amount_pos += 1
#
# print("amount_neg", amount_neg)
# print("amount_pos", amount_pos)
#
# for i in range(len(word_list)):
#     print('nieuwe woordenlijst', i,word_list[i])
#
# phrase_q = 2
#
# # start at index zero, till one before end of the list
# for i in range(0, len(word_list) - phrase_q, 1):
#
#     if word_list[-1]:
#         phrase = " "
#         strings = word_list[i], word_list[i+1]
#         phrase = phrase.join(strings)
#         phrases_two.append(phrase)
#         count = 0
#
# for phrase in phrases_two:
#     print("phrase2", count, phrase)
#     count += 1
#
#     index = count - 1
#
#     for neg in neg_one_space:
#         if phrase == neg:
#             print("negatief woord^")
#             print('index', index)
#             print("word_list[index]",word_list[index])
#
#             # for j in range(0, phrase_q):
#             #     print("delete:", word_list[index])
#             #     del word_list[index]
#             amount_neg += 1
#
#     for pos in pos_one_space:
#         if phrase == pos:
#             print("positief woord^")
#             print('index', index)
#
#             print("word_list[index]", word_list[index-phrase_q])
#
#             for k in range(0, phrase_q):
#                 print("delete:", word_list[index-phrase_q])
#                 del word_list[index-phrase_q]
#             amount_pos += 1
#
# print('amount_neg', amount_neg)
# print("amount_pos", amount_pos)
#
# for i in range(len(word_list)):
#     print('nieuwe woordenlijst', i,word_list[i])
#
# # nothing has to be delete... right???? (pos/neg validity)(don't forget to take a look at this)
# phrase_q = 1
# for i in range(0, len(word_list) - phrase_q, 1):
#     if word_list[-1]:
#         phrase = word_list[i]
#         phrases_one.append(phrase)
#         count = 0
#
# for phrase in phrases_one:
#     print("phrase1", count, phrase)
#     count += 1
#
#     index = count - 1
#
#     for neg in neg_no_space:
#         if phrase == neg:
#             print("negatief woord^")
#             print('index', index)
#             print("word_list[index]",word_list[index])
#             print("delete:", word_list[index])
#             # del word_list[index]
#             amount_neg += 1
#
#     for pos in pos_no_space:
#         if phrase == pos:
#             print("positief woord^")
#             print('index', index)
#             print("word_list[index]",word_list[index])
#             for k in range(0, phrase_q):
#                 print("delete:", word_list[index-phrase_q])
#                 del word_list[index-phrase_q]
#             amount_pos += 1
#             amount_pos += 1
#
# for i in range(len(word_list)):
#     print('nieuwe woordenlijst', i,word_list[i])
# print("amount_neg", amount_neg)
# print("amount_pos", amount_pos)

# de boeren zagen de oude vrijster op de loer liggen terwijl ze een hekel hebben aan haar, toen moesten ze de varkens in de steek laten, ze waren ten einde raad maar ook boos, maarja

# Gelukkig was het niet voor de hand liggend dat dol zijn op boodschappen doen bovenmenselijk was, media
