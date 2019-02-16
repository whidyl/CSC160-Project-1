"""
Creates an dictionary with a key for each unique word in the text.
The index value refers to all unique lines which the word occurs

example:
Act: 3, 9 ...
Romeo: 1, 2, 6 ...
...
"""

from pprint import pprint

def main():
    # start by getting a file and making a dict
    # containting each word in the file as a key
    fhand = getFileFromUser()
    wordIndex = getWordIndexes(fhand)
    # for every word in our index, change it's value to a set
    # of every line # the word appears on
    for word in wordIndex:
        wordIndex[word] = getLineNumbersForWord(word, fhand)
    # write this data to a file and print it
    pprint(wordIndex)
    with open('Word-Index.txt', 'w') as f:
        print(wordIndex, file=f)



def getFileFromUser():
    fname = input('Enter the name of the text file: ')
    try:
        fhand = open(fname)
    except:
        print('could not find file ' + fname)
        exit()
    return fhand

def getWordIndexes(fhand):
    """
    Generates a dictionary with every unique word in @param fhand.
    Each word is given a value of None
    """
    wordIndex = dict()
    for line in fhand:
        line = line.rstrip()
        words = line.split()
        for word in words:
            wordIndex[word] = None
    return wordIndex

def getLineNumbersForWord(word, fhand):
    """
    Returns a set of each line that @param word appears on in file @param fhand.
    """
    fhand.seek(0) # reset cursor so we can read the file again
    lineNumbers = []
    lineNumber = 0
    for line in fhand:
        lineNumber += 1
        wordsOnFileLine = line.split()
        for wordFromFile in wordsOnFileLine:
            if wordFromFile == word:
                lineNumbers.append(lineNumber)
    return set(lineNumbers)
            
main()
