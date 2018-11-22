# wordList = ['de', 'oude', 'vrijster', 'had', 'ontslag', 'genomen', 'en',
#             'was', 'ten', 'einde', 'raad', 'en', 'heel', 'boos', 'dat', 'is',
#             'niet', 'verkeerd', 'voorstellen', 'dus', 'pak', 'slaag', 'bijna',
#             'einde']
#
# negWords = ["oude vrijster", "ontslag genomen", "ten einde raad", "vervelend"
#             "boos", "pak slaag", "verkeerd voorstellen"]

# for one string

# oneSpace = []
# twoSpaces = []
# threeSpaces = []
#
# def howManySpaces(str, oneSpace, twoSpaces, threeSpaces):
#     count = 0
#     for i in range(len(str)-1):
#         if str[i:i+1] == " ":
#             count += 1
#     if count == 1:
#         oneSpace.append(str)
#     elif count == 2:
#         twoSpaces.append(str)
#     elif count == 3:
#         threeSpaces.append(str)
#
#     return oneSpace, twoSpaces, threeSpaces, count
#
#
# str = "verkeerd voorstellen"
# print(howManySpaces(str, oneSpace, twoSpaces, threeSpaces))
# print("oneSpace", oneSpace)
# print("twoSpaces", twoSpaces)
# print("threeSpaces", threeSpaces)


# now for a list of strings

wordList = ['de', 'oude', 'vrijster', 'had', 'ontslag', 'genomen', 'en',
            'was', 'ten', 'einde', 'raad', 'en', 'heel', 'boos', 'dat', 'is',
            'niet', 'verkeerd', 'voorstellen', 'dus', 'pak', 'slaag', 'bijna',
            'einde']



negWords = ["oude vrijster is boos", "ontslag genomen", "mega mega mega naar",
            "ten einde raad", "vervelend", "boos", "pak slaag",
            "verkeerd voorstellen"]
            
noSpace = []
oneSpace = []
twoSpaces = []
threeSpaces = []
count = 0

def howManySpaces(negWords, noSpace, oneSpace, twoSpaces, threeSpaces, count):
    flag = True
    for i in range(len(negWords)):
        print('alle negwords', negWords[i])
        phrase = negWords[i]
        print("phrase", phrase)
        for j in range(len(phrase)):
            print('prashe[j]', phrase[j])
            if phrase[j] == " ":
                count += 1
        if phrase[-1]:
            print('the end end count', count)

            if count == 1:
                oneSpace.append(phrase)
            elif count == 2:
                twoSpaces.append(phrase)
            elif count == 3:
                threeSpaces.append(phrase)
            else:
                noSpace.append(phrase)

            count = 0

    return negWords, noSpace, oneSpace, twoSpaces, threeSpaces, count


print("function", howManySpaces(negWords, noSpace, oneSpace, twoSpaces, threeSpaces, count))
print("noSpace", noSpace)
print("oneSpace", oneSpace)
print("twoSpaces", twoSpaces)
print("threeSpaces", threeSpaces)

        #     print('hierphrase', phrase)
        #     print('hierhierhier', oneSpace)

    #     elif count == 2:
    #         twoSpaces.append(phrase)
    #     elif count == 3:
    #         threeSpaces.append(phrase)
    # else:
    #     noSpace.append(phrase)


# def howManySpaces(negWords, noSpace, oneSpace, twoSpaces, threeSpaces, count):
#     flag = True
#     for i in range(len(negWords)):
#         print('alle negwords', negWords[i])
#         phrase = negWords[i]
#         print("phrase", phrase)
#
#         if flag == True:
#             for j in range(len(phrase)):
#                 print('prashe[j]', phrase[j])
#                 if phrase[j:-1]:
#                     flag = False
#
#                 if phrase[j] == " ":
#                     count += 1
#                     if phrase[j:-1]:
#                         print('the end')
#                         flag = False
#                 # print('c', count)
#                 count = 0
#     # print('cr', count)
#     if count == 1:
#         oneSpace.append(phrase)
#
#     return negWords, noSpace, oneSpace, twoSpaces, threeSpaces, count
