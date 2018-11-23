# open the files with negative words
negatives = open("neg_dutch_2.txt")

neg_list = []

# push all the words from text file to list
for lines in negatives:
    lines = lines.lower()
    neg_list.append(lines.strip("\n"))

neg_no_space = []
neg_one_space = []
neg_two_spaces = []
neg_three_spaces = []

count = 0

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

print("neg_no_space", neg_no_space)
# print("neg_one_space", neg_one_space)
# print("neg_two_spaces", neg_two_spaces)
# print("neg_three_spaces", neg_three_spaces)


# for i in range(len(neg_no_space)):
#     print(i, neg_no_space[i])
#
# for i in range(len(neg_one_space)):
#     print(i, neg_one_space[i])
#
# for i in range(len(neg_two_spaces)):
#     print(i, neg_two_spaces[i])

# for i in range(len(neg_three_spaces)):
#     print(i, neg_three_spaces[i])
