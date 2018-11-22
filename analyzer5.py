wordList = ['de', 'oude', 'vrijster', 'had', 'ontslag', 'genomen', 'en',
            'was', 'ten', 'einde', 'raad', 'en', 'heel', 'boos', 'dat', 'is',
            'niet', 'verkeerd', 'voorstellen', 'dus', 'pak', 'slaag', 'bijna',
            'einde']

negWords = ["oude vrijster", "ontslag genomen", "ten einde raad", "vervelend"
            "boos", "pak slaag", "verkeerd voorstellen"]


oneSpace = []
twoSpaces = []
threeSpaces = []

def howManySpaces(str, oneSpace, twoSpaces, threeSpaces):
    count = 0
    for i in range(len(str)-1):
        if str[i:i+1] == " ":
            count += 1
    if count == 1:
        oneSpace.append(str)
    elif count == 2:
        twoSpaces.append(str)
    elif count == 3:
        threeSpaces.append(str)

    return oneSpace, twoSpaces, threeSpaces, count



str = "verkeerd voorstellen"
print(howManySpaces(str, oneSpace, twoSpaces, threeSpaces))
print("oneSpace", oneSpace)
print("twoSpaces", twoSpaces)
print("threeSpaces", threeSpaces)
