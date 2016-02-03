"""
Author: Sean Strout (sps@cs.rit.edu)
Author: Colin Fausnaught

This class represents Greedo's satchel that can store a collection
of Metal bars.  As such, it is dependent on the Metal class for its 
internal representation.  The satchel support operations for
creation, filling the entire satchel, adding a single metal bar,
and displaying the satchel.

Language: Python 3
"""

from rit_object import *            # rit_object class

class Satchel(rit_object):
    """
    Represents a satchel that can hold up to a certain weight of metals.
    :slot name (str): The name of the satchel
    :slot capacity (int): The maximum weight the satchel can hold
    :slot weight (int): The total weight of the metals in the satchel
    :slot totalValue (int): The total value of the metals in the satchel
    :slot items (list of Metal): The metals added into the satchel
    """
    __slots__ = ('name', 'capacity', 'weight', 'totalValue', 'items')
    _types = (      str,        int,      int,          int,    list)

def createSatchel(name, capacity):
    """
    Create and return a new Satchel object.
    :param name (str): The name of the satchel
    :param capacity (int): The maximum weight the satchel can hold
    :return: A newly initialized Satchel object
    :rtype: Satchel
    """

    return Satchel("Greedo's Satchel", capacity, 0, 0, [])

def fillSatchel(satchel, metals):
    """
    Fill the satchel greedily by the metal value.  This assumes the metals
    are already sorted in descending order by value (e.g. value per bar,
    or value per weight).
    :param satchel (Satchel): The Satchel object
    :param metals (list of Metal): The list of metals
    :return: None
    :rtype: NoneType
    """
    index = 0
    while index != len(metals):
        if (metals[index].weightPerBar + satchel.weight) <= satchel.capacity and metals[index].totalBars != metals[index].barsTaken:
            satchel.weight += metals[index].weightPerBar
            metals[index].barsTaken += 1
            addItem(satchel, metals[index])
            
        else:
            index += 1

def addItem(satchel, metal):
    """
    Add a metal to the satchel.
    :param satchel (Satchel): The Satchel object
    :param metal (Metal): The metal to be added
    :return: None
    :rtype: NoneType
    """
    for x in range(len(satchel.items)):
        if satchel.items[x] == metal:
            return
        
    satchel.items += [metal]
    satchel.totalValue += metal.valuePerBar
    
def printSatchel(satchel):
    """
    Display the satchel to standard output in the format:
        Name: {name of satchel}
    	Capacity: {maximum weight of satchel}
    	Weight Held: {current weight of satchel}
    	Total Value: {total value of satchel}
    	Items:
    	    {first metal}
    	    {second metal}
    	    ...
    When displaying the individual metals, use the metal module function,
    printMetals().
    :param satchel (Satchel): The Satchel object
    :return: None
    :rtype: NoneType
    """

    print("Name: " + satchel.name + "\n" +
          "Capacity: " + str(satchel.capacity) + "\n" +
          "Weight Held: " + str(satchel.weight) + "\n" +
          "Total Value: " + str(satchel.totalValue) + "\n" +
          "Items:")
    
    for x in range(len(satchel.items)):
        print("     " + str(satchel.items[x]))
