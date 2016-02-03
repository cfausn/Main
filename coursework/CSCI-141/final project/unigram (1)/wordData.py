"""
    Implements the functions readWordFile and totalOccurences, as well as
    the classes YearCount and WordCount

    AUTHOR: Colin Fausnaught
"""
from rit_object import *


class YearCount(rit_object):
    """
        YearCount object. Extends rit_object to create this object.

        contains slots 'year' and 'count', both of which are integers.
    """
    __slots__ = ('year', 'count')
    _types = (int, int)

class WordCount(rit_object):
    """
        WordCount object. Extends rit_object to create this object.

        contains slots 'word' and 'count', word is string and count is an integer
    """
    __slots__ = ('word', 'count')
    _types = (str, int)

def readWordFile(fileName):
    """
    reads the file with the given file name, all of the files must be in
    the 'data\' directory.

    :param fileName :A string giving the name of a unigram csv file
    :return: A dictionary mapping words to lists of YearCount objects
    """
    myDict = dict()
    tempList = []

    for line in open(str("data\\"  + fileName)):
        tempList = line.split(',')
        if not tempList[0] in myDict:
            myDict[tempList[0]] = [YearCount(int(tempList[1]),int(tempList[2]))]
        else:
            myDict[tempList[0]].append(YearCount(int(tempList[1]),int(tempList[2])))

    return myDict

def totalOccurrences(word, words):
    """
    gets total occurrences of a word in the words dictionary.

    :param word: The word for which to calculate the count. Not guaranteed to exist in words
    :param words: A dictionary mapping words to lists of YearCount objects.
    :return: number of times that a word has appeared (int)
    """
    myTotal = 0

    if word in words:
        for elm in words[word]:
            myTotal += elm.count

    return myTotal

