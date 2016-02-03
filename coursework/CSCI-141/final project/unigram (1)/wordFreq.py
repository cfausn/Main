"""
    main program for second task

    implements wordFreqencies, which calculates the word frequencies
    to produce the ranking of word occurecnes in the provided dataset,
    and draws the log-log plot to reveal Zipf's Law

    AUTHOR: Colin Fausnaught
"""

import simplePlot
import wordData


def wordFrequencies(words):
    """
    gets the frequencies of the words and returns them in descending order in a list.
    uses insertion sort to accomplish this efficiently

    :param words:The word data, which is a dictionary (dict) that maps words (strings) to a
                 list of YearCount’s.

    :return:A list of WordCount objects in decreasing order from most to least frequent.
    """
    keyList = words.keys()
    newList = []

    for word in keyList:
        newList.append(wordData.WordCount(word,wordData.totalOccurrences(word,words)))

    for index in range(1,len(newList)):
        indexVal = newList[index]
        ind = index
        while ind > 0 and newList[ind-1].count < indexVal.count:
            newList[ind] = newList[ind-1]
            ind-=1
        newList[ind] = indexVal

    return newList


def main():
    """
    calls the functions in the correct order, accepts the user's input, and prints results.
    """

    fileName = input("Enter word file: ")
    rank = int(input("Enter rank (1-3): "))
    words = wordData.readWordFile(fileName)
    myList = wordFrequencies(words)

    print("Rank " + str(rank) + ": " + str(myList[rank - 1]))
    simplePlot.wordFreqPlot(myList)


if __name__ == '__main__':
    main()
