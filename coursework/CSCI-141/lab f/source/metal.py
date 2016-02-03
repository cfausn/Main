"""
Author: Sean Strout (sps@cs.rit.edu)
Author: Colin Fausnaught

This class represents the types of metal bars that Greedo can
store in his satchel.  Each type of bar is a separate Metal
object.  This module also has routines that work with metals,
e.g. creation, reading from a file, and sorting based on 
various criteria.

Language: Python 3
"""
import os
from rit_object import *            # rit_object class

class Metal(rit_object):
    """
    Represents a single metal type, composed of:
    :slot name (str): The name of the metal
    :slot totalBars (int): The total number of bars
    :slot weightPerBar (int): The weight of a single bar
    :slot valuePerBar (int): The value of a single bar
    :slot valuePerWeight (float): The value per weight of the metal
    :slot barsTaken (int): The number of bars added to the satchel
    """
    __slots__ = ('name', 'totalBars', 'weightPerBar', 'valuePerBar', 'valuePerWeight', 'barsTaken')
    _types = (      str,         int,            int,           int,            float,         int)

def createMetal(name, totalBars, weightPerBar, valuePerBar):
    """
    Create and return a new Metal object.
    :param name (str): The name of the metal
    :param totalBars (int): The total number of bars
    :param weightPerBar (int): The weight of a single bar
    :param valuePerBar (int): The value of a single bar
    :return: A newly initialized Metal object
    :rtype: Metal
    """
    valuePerWeightLocal = valuePerWeight(weightPerBar,valuePerBar)
    barsTaken = 0
    return Metal(name, totalBars, weightPerBar, valuePerBar, valuePerWeightLocal, barsTaken)

def readMetals(fileName):
    """
    Read the metals from a file whose format is:
        metalName totalBars weightPerBar valuePerBar
    :param fileName (str): The name of the file
    :return: A list of Metal objects
    :rtype: list
    """
    directoryString = os.getcwd()
    directoryString += "\\data\\"

    metalList = []
    tempList = []
    
    for line in open(directoryString + fileName):
        tempList += (line.split(" "))
        valPerBar = tempList.pop()
        valPerBar = valPerBar.replace('\n' , '')
        valuePerBar = int(valPerBar)
        weightPerBar = int(tempList.pop())
        totalBars = int(tempList.pop())
        name = str(tempList.pop())
        metalList += [createMetal(name, totalBars, weightPerBar, valuePerBar)]

    return metalList
    
def valuePerWeight(weightPerBar, valuePerBar):
    """
    Gets the value per weight for the bar

    :param weightPerBar: weight of the bar
    :param valuePerBar: value of of the bar
    :return: value per weight of the bar
    :rtype: float
    """
    
    return (valuePerBar / weightPerBar)

def sortMetalsByValuePerBar(metals):
    """
    Sort the metals by value per bar using insertion sort.  The list of
    metals is modified in place to be ordered by value per bar.
    :param metals (list of Metal): The list of metals
    :return: None
    :rtype: NoneType
    """

    for index in range(1, len(metals)):
        indexVal = metals[index]
        i = index
        while i > 0 and metals[i - 1].valuePerBar < indexVal.valuePerBar:
            metals[i] = metals[i-1]
            i-=1
        metals[i] = indexVal
    

def sortMetalsByValuePerWeight(metals):
    """
    Sort the metals by value per weight using insertion sort.  The list of
    metals is modified in place to be ordered by value per weight.
    :param metals (list of Metal): The list of metals
    :return: None
    :rtype: NoneType
    """

    for index in range(1, len(metals)):
        indexVal = metals[index]
        i = index
        while i > 0 and metals[i - 1].valuePerWeight < indexVal.valuePerWeight:
            metals[i] = metals[i-1]
            i-=1
        metals[i] = indexVal

def printMetals(metals):
    """
    Display the metals to standard output.
    :param metals (list of Metal): The list of metals
    :return: None
    :rtype: NoneType
    """

    for x in range(len(metals)):
        print(metals[x])

