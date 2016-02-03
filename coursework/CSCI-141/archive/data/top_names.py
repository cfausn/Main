"""
CSCI-141: Homework F: Top Baby Names
Author: Sean Strout (sps@cs.rit.edu)
Author: Colin Fausnaught

This program will find the top baby names for a range of years,
based on a state and gender.  It will also determine what name
in that range occurred the most times in a row.

This program, as a collection of modules, requires the rit_object
module to be installed in the same location as the other
source files.  The rit_object module is located at:

http://www.cs.rit.edu/~csci141/lib/rit_object_py.txt

Language: Python 3
"""

from rit_object import *

# constants for file format
def START_YEAR(): return 1910
def END_YEAR(): return 2013
def MALE(): return 'M'
def FEMALE(): return 'F'

class Name(rit_object):
    """
    Represents a single top baby name.
    :slot name (str): The name, e.g. 'Mary'
    :slot gender (str): The gender, e.g. 'F'
    :slot year (int): The year, e.g. 1923
    :slot state (str): The state, e.g. 'NY'
    :slot occurrences (int): The number of occurrences, e.g. 2429
    """

    __slots__ = ('name', 'gender', 'year', 'state', 'occurrences')
    _types =    ( str,    str,      int,    str,     int         )

def createName(fields):
    """
    Initialize and return a new Name object.
    :param fields (list of str): A list of strings that represent one line
        in the file, [state, gender, year, name, occurrences], e.g.
        ['AK', 'M', '2004', 'Justin', '23']
    :return: the new Name object
    :rtype: Name
    """

    state = fields[0]
    gender = fields[1]
    year = int(fields[2])
    name = fields[3]
    occurrences = int(fields[4])
    return Name(name, gender, year, state, occurrences)

def getTopNames(state, gender, startYear, endYear):
    """
    Get the top names.
    :param state (str): The state, e.g. 'NY'
    :param gender (str): The gender, e.g. 'F'
    :param startYear (int): The starting year, e.g. 1969
    :param endYear (int): The ending year, e.g. 2010
    :return: The list of top Name objects
    :rtype: list
    """
    filename = (state + ".txt")
    nameList = []
    testHold = []
    x = 0
    for line in open(filename):
        testHold += [createName(line.split(','))]
        if testHold[x].year >= startYear and testHold[x].year <= endYear and testHold[x].gender == gender:
            nameList += [testHold[x]]

        x+=1

    if nameList[-1].year == nameList[0].year:
        return [nameList[0]]

    x = 0
    topNamesList = []
    while x != (len(nameList) -1):
        if nameList[x].year != nameList[x+1].year:
            topNamesList += [nameList[0]]
            nameList = nameList[x+1:]
            x = 0
        elif nameList[-1].year == nameList[0].year:
            topNamesList += [nameList[0]]
            break
        else:
            x+=1
    
    return topNamesList

def sortByTop(nameList):
    #sort using the algorithm from lab with k being len(nameList) -1
    pass

def mostConsecutiveYears(names):
    """
    Compute which name occurs the most times consecutively in a 
    list of names.
    :param names (list of Name): A list of name objects
    :return: A tuple containing best name (str) and the count (int)
    :rtype: tuple
    """
    startYear = names[0].year
    endYear = names[-1].year
    bestName = " "
    bestRun = 1

    if startYear == endYear:
        return names[0].name, bestRun

    x = 0
    newList = []

    while x!= len(names):
        newList += [names[x].name]
        x+=1
        
    x = 0
    newList2 = []
    while x != (len(newList) - 1):
        if newList[x] != newList[x+1]:
            newList2 += [newList[:x+1]]
            newList = newList[x+1:]
            x = 0
        elif newList[x] == newList[x+1] and (x+1) == (len(newList) -1):
            newList2 += [newList]
            break
        else:
            x+=1
            
    for i in newList2:
        if bestName == " ":
            bestRun = len(i)
            bestName = i[0]
        elif len(i) > bestRun:
            bestRun = len(i)
            bestName = i[0]
        
            
    return bestName, bestRun
            


def main():
    """
    The main function.
    :return None
    :rtype: None
    """

    # prompt for all information
    state = input('Enter state: ').upper()
    gender = input('Enter gender: ').upper()
    startYear = int(input('Enter start year: '))
    endYear = int(input('Enter end year: '))

    # sanity check
    if startYear < START_YEAR():
        print('Start year must be greater than or equal to', START_YEAR())
    elif endYear > END_YEAR():
        print('End year must be less than or equal to', END_YEAR())
    elif startYear > endYear:
        print('Start year must be less than or equal to end year')
    else:
        # get/display the top names
        names = getTopNames(state, gender, startYear, endYear)
        print('Top', 'male' if gender == MALE() else 'female', 'names for',
              state, 'between', str(startYear) + '-' + str(endYear) + ': ')
        for n in names:
            print('\tIn', n.year, n.name, 'occurred the most at',
                  n.occurrences, 'times')

        # next, get/display the most consecutively occurring name
        bestName, bestCount = mostConsecutiveYears(names)
        print(bestName, 'occurred consecutively the most in this range at',
              bestCount, 'time/s')

if __name__ == '__main__':
    main()
