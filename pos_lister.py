# open the files with positive words
positives = open("pos_dutch_2.txt")

pos_list = []

# push all the words from text file to list
for lines in positives:
    lines = lines.lower()
    pos_list.append(lines.strip("\n"))

pos_no_space = []
pos_one_space = []
pos_two_spaces = []
pos_three_spaces = []
count = 0

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

print("pos_no_space", pos_no_space)
print("pos_one_space", pos_one_space)
print("pos_two_spaces", pos_two_spaces)
print("pos_three_spaces", pos_three_spaces)

for i in range(len(pos_no_space)):
    print('0',i, pos_no_space[i])

for i in range(len(pos_one_space)):
    print('1',i, pos_one_space[i])

for i in range(len(pos_two_spaces)):
    print('2',i, pos_two_spaces[i])

for i in range(len(pos_three_spaces)):
    print('3',i, pos_three_spaces[i])
