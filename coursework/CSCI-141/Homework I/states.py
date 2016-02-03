"""
    states.py
    Colin Fausnaught

    takes information from a file and calculates the average number of people
    it would take before people from the same state appeared. 
"""

import random
from rit_object import *

class HashTable(rit_object):
    """
           HashTable to store the total size and the list of State objects.

    """
    __slots__ = ( 'table', 'size' )
    _types    = (list, int)

class State(rit_object):
    """
           State is a custom object that will hold the state name, the range
           of the state's population, and the total population of the state.
    """
    __slots__ = ('name', 'range', 'population')
    _types =    (str,    list   , int)

def createState():
    """
    creates an empty state object
    """
    return State("", [], 0)

def createHashTable(capacity=51):
  """
  creates an empty HashTable object
  """
  aHashTable = HashTable([None for _ in range(capacity)], 0)
  return aHashTable

def main():
    """
    main will call all of the utility functions and will structure the program
    to accomplish the task of finding  the average
    """
    filename = input("Enter file name: ")
    tests = int(input("Tests (1-1000): " ))
    state = createState()
    hashTab = createHashTable()
    timesList = []
    
    if tests > 1000 or tests < 1:
        print("Incorrect value for tests")
        return
    
    getFromFile(filename, state, hashTab)

    
    for item in range(tests):
        appendedNum = roomPoll(0, hashTab)
        timesList.append(appendedNum)

    numSum = calcSum(timesList)

    print("Average is: " + str(numSum/tests))
            

def findState(totalPop, states, number):
    """
    findState will find the state that the random number is located in based on
    the range stored in state.range.

    :param totalPop: the total population (assignment told me to pass it, though I don't use it here.)
    :param states: a list of State objects
    :param number: a random interger from 0 to the size of the total population

    :return: the state that it was decided the random number was in.
    :rtype: string
    """
    index = 0
    while index != len(states):
        if number >= states[index].range[0] and number <= states[index].range[1]:
            return states[index].name
        else:
            index+=1

def roomPoll(counter,hashTab):
    """
    roomPoll will be used to check if the state has already been used by the program,
    and if it isn't it will loop and do this again.

    :param counter: an interger used to count how many people are not in the same state
    :param hashTab: HashTable type, used to store State elements and the total population

    :return counter: the number of people not from the same state
    :rtype: interger
    """
    mySet = set()
    while counter <= 50:
            state = findState(hashTab.size, hashTab.table, random.randint(0, hashTab.size))
            if not (state in mySet):
                counter+=1
                mySet.add(state)
            else:
                break
            
    return counter

def calcSum(lst):
    """
    adds all numbers from the list.

    :param lst: the numbers from each run, stored in a list

    :return: theSum, the sum of all the numbers in the list
    :rtype: int
    """
    theSum = 0
    for num in lst:
        theSum += num

    return theSum

def getFromFile(filename, state, hashTab):
    """
    gets the items from the file and adds them to the HashTable, doens't need to return
    anything because custom objects persist.

    :param filename: the file name specified by the user
    :param state: the empty State object
    :param hashTab: the empty HashTable object

    
    """
    tempList = []
    prevNum = 0
    index = 0
    
    for line in open(filename):
        tempList = line.split()
        state.name = tempList[0]
        if prevNum == 0:
            state.range = [prevNum, (prevNum + int(tempList[1]))]
            state.population = int(tempList[1])
            prevNum = int(tempList[1])
        else:
            state.range = [prevNum + 1, (prevNum + int(tempList[1]))]
            state.population = int(tempList[1])
            prevNum = int(tempList[1]) + prevNum
            
        hashTab.size += int(tempList[1])
        hashTab.table[index] = state
        state = createState()
        index+=1
    
main()
