"""
    main program for third task.

    implements averageWordLength, averageWordLengthYears, and
    occurencesInYear, draws average word length for a specified period
    of time based on the words in the provided dataset.

    AUTHOR: Colin Fausnaught
"""

import wordData
import simplePlot

def occurrencesInYear(word, year, words):
    """
    finds the occurrences in a year

    :param word: The word in question passed in as a str.
    :param year: The year in question. This is an int.
    :param words: The word data which is a dictionary (dict) that maps words (str).
                  to a list of YearCount’s.

    :return:The number of occurrences of the word in the year (int).
    """
    myTotal = 0
    for elm in words[word]:
        if elm.year == year:
            myTotal += elm.count

    return myTotal


def averageWordLength(year, words):
    """
    finds the average word length in the given year

    :param year: The year in question (int).
    :param words: The words data which is a dictionary (dict) that maps words (strings) to a
                  list of YearCount’s
    :return: The average word length for the year in question (float).
    """
    totalWordLen = 0
    totalInYear = 0
    for elm in words:
        for yearCount in words[elm]:
            if yearCount.year == year:
                totalWordLen += len(elm) * yearCount.count
                totalInYear += yearCount.count
    if totalInYear == 0:
        return 0.0

    return float(totalWordLen / totalInYear)

def averageWordLengthYears(startYear, endYear, words):
    """
    returns a list of word lengths using averageWordLength

    :param startYear: The start year, an (int)
    :param endYear: The end year, likewise an (int).
    :param words: The words data which is a dictionary (dict) that maps words (strings) to
                  a list of YearCount’s.
    :return: The list of float’s that contains the average word lengths by year in the increasing
             order for years between startYear and endYear – both inclusive.
    """
    myList = []

    for elm in range(startYear,endYear):
        myList.append(averageWordLength(elm,words))

    return myList


def main():
    """
    calls the functions in the correct order, accepts the user's input, and prints results.
    """
    fileName = input("Enter file name for file in data directory: ")
    words = wordData.readWordFile(fileName)

    word = input("Enter a word: ")
    year = int(input("Enter a year: "))

    occInYear = occurrencesInYear(word, year, words)

    print("The average word " + word + " occurred " + str(occInYear) + " times in the year "+\
        str(year))

    year = int(input("Enter a year: "))
    avg = averageWordLength(year,words)

    print("The average word length for the year " + str(year) + " is " + str(avg) + " letters")

    startYear = int(input("Enter a start year: "))
    endYear = int(input("Enter an end year: "))

    lengthsList = averageWordLengthYears(startYear,endYear + 1,words)

    simplePlot.averageWordLengthPlot(startYear,endYear,lengthsList)


if __name__ == '__main__':
    main()
