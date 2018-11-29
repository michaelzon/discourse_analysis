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
