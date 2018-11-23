posWords = ["de oude vrijster", "ontslag genomen", "ten einde raad", "boos", "pak slaag", "verkeerd voorstellen"]
wordList = ['de', 'oude', 'vrijster', 'had', 'ontslag', 'genomen', 'en', 'was', 'ten', 'einde', 'raad', 'en', 'heel', 'boos', 'dat', 'is', 'niet', 'verkeerd', 'voorstellen', 'dus', 'pak', 'slaag', 'poep', 'poep']

print('poswords', posWords)
print('wordlist', wordList)

# Create a sentence for the wordListself.
joinedWordList = " ".join(wordList)

print("joinedwordlist", joinedWordList)

# Find all phrases in the posWords list.
phrases = [elem for elem in posWords if len(elem.split()) > 1]

print("phrases", phrases)
# For every phrase, locate it in the sentence,
# count the space characters which is the same number as the index of the first word of phrase in the word list,
# insert the phrase and delete the word that combine the phrase from the wordList.
for phrase in phrases:
    try:
        i = joinedWordList.index(phrase)
        spaces = len([letter for letter in joinedWordList[:i] if letter==' '])
        wordList.insert(spaces,phrase)
        del wordList[spaces+1:spaces+1:spaces+1 + len(phrase.split())]
    except ValueError:
        pass
print('newwordlist', wordList)
