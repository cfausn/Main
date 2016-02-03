"""
    main program for first task

    implements letterFreq, draws the letter histogram plot

    AUTHOR: Colin Fausnaught
"""

import wordData
import letterHist

def letterFreq(words):
    """
    organizes the values from the inputted file, then returns that list. Then
    returns that list sorted alphabetically.

    :param words: a dictionary mapping words to lists of YearCount objects
    :return: a list containing the relative frequency of letters scaled by the letter
             count in alphabetical order
    """

    dictKeys = words.keys()
    totalNum = 0.0
    alphDict = dict()
    myList = []


    for word in dictKeys:
        totalNum += len(word) * wordData.totalOccurrences(word,words)
        for letter in word:
            if not letter in alphDict:
                alphDict[letter.lower()] = wordData.totalOccurrences(word,words)
            else:
                alphDict[letter.lower()] += wordData.totalOccurrences(word,words)



    for num in range((ord('z') + 1) - ord('a')):
        if not chr(num + 97) in alphDict:
            myList.append(0.0)
        else:
            myList.append(alphDict[chr(num + 97)] / totalNum)

    return myList



def main():
    """
    calls the functions in the correct order, accepts the user's input, and prints results.
    """
    fileName = input("Enter word file: ")
    words = wordData.readWordFile(fileName)

    word = input("Enter word: ")

    print("Total occurrences of " + word + ": " + str(wordData.totalOccurrences(word,words)))
    myList = letterFreq(words)

    print("Letter frequencies: " + str(myList))

    letterHist.letterFreqPlot(myList)



if __name__ == '__main__':
    main()
