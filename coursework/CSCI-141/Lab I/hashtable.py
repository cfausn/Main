"""
description: open addressing Hash Table for CS 141 Lecture
file: hashtable.py
language: python3
author: sps@cs.rit.edu Sean Strout
author: jeh@cs.rit.edu James Heliotis
author: anh@cs.rit.edu Arthur Nunes-Harwitt
author: jsb@cs.rit.edu Jeremy Brown
author: Colin Fausnaught
"""
from rit_object import *

class HashTable(rit_object):
    """
           The HashTable data structure contains a collection of values
       where each value is located by a hashable key.
       No two values may have the same key, but more than one
       key may have the same value.
       table is the list holding the hash table
       size is the number of elements in occupying the hashtable

    """
    __slots__ = ( 'table', 'size')
    _types    = (    list,    int)


class Guest(rit_object):
    """
         A class used to hold the guest's primary seat, secondary seat,
         and the tab owed.
    """
    __slots__ = ('primary', 'secondary', 'tab')
    _types    = (      int,         int,   int)

class Entry(rit_object):
    """
       A class used to hold name/value pairs.
    """

    __slots__ = ( "name", "value")
    _types = (       str,  object)

    
def createHashTable(capacity):
    """
    creates a hash table based on the passed capacity

    :param capacity: int, the size of the hash table

    :return: aHashTable, the empty hash table
    :rtype: HashTable
    """
    aHashTable = HashTable([None for _ in range(capacity)], 0)
    return aHashTable

def createGuest(name, capacity, tab):
    """
    creates a guest entry based on the passed name and tab.
    Uses capacity to call the firstSeat and secondSeat values.

    :param name: string, the name of the guest
    :param capacity: int, the number of seats
    :param tab: int, the owed amount

    :return: Entry with all fields filled
    :rtype: Entry
    """
    return Entry(name, Guest(firstSeat(name,capacity), secondSeat(name,capacity),tab))


def put( hTable, guest ):
    """
    Using the given hash table, set the given key to the
    given value. If the key already exists, the given value
    will replace the previous one already in the table.

    :param hTable: HashTable, holds a list of Entry objects and the total size
    :param guest: Entry, an entry object holding all the guest's information

    :return: True or raises an exception
    :rtype: Bool
    """
    index = guest.value.primary
        
        
    if has(hTable, index) == False:
        hTable.table[ index ] = guest
        hTable.size += 1
    else:
        newIndex = guest.value.secondary
        if has(hTable, newIndex) == False:
            hTable.table[newIndex] = guest
            hTable.size +=1
        elif get(hTable, newIndex).value.secondary == newIndex:
            raise Exception("Could not seat everyone")
        else:
            newGuest = get(hTable,newIndex)
            hTable.table[newIndex] = guest
            return put(hTable, newGuest)
            
    return True

def hash_function( val, n ):
    """
    hash_function: K NatNum -> NatNum
    Compute a hash of the val string that is in [0 ... n).
    """
    hashcode = hash( val ) % n
    # hashcode = 0
    # hashcode = len(val) % n
    return hashcode

def has( hTable, key ):
    """
    checks to see if the table index exists

    :param hTable: HashTable, holds a list of Entry objects and the total size
    :param key: int, the index to check
    
    :return: True if hTable has an entry with the given key
    :rtype: Bool
    """
    return hTable.table[ key ] != None

def get( hTable, key ):
    """
    gets the value at a given index

    Precondition: has(hTable, key)

    :param hTable: HashTable, holds a list of Entry objects and the total size
    :param key: int, the index to check

    :return: Entry object at a given index
    :rtype: Entry
    """
    if hTable.table[ key ] == None:
        raise Exception( "Hash table does not contain key." )
    else:
        return hTable.table[ key ]

def firstSeat(name, capacity):
    """
    finds the first seat based on the lab algorithm.

    :param name: string, the name of the guest
    :param capacity: int, total number of seats

    :return: the primary seat of the guest
    :rtype: int
    """
    acc = 1
    for char in name:
        acc *= ord(char.upper()) - (ord('A') + 1)
    return acc % capacity

def secondSeat(name, capacity):
    """
    finds the second seat based on the lab algorithm.

    :param name: string, the name of the guest
    :param capacity: int, total number of seats

    :return: the secondary seat of the guest
    :rtype: int
    """
    acc = 0
    for char in name:
        acc += ord(char.upper()) - (ord('A') +1)
    return acc % capacity

def indexOf(name, hTable):
    """
    finds the index of the passed guest name.

    :param name: string, the name of the guest
    :param hTable: HashTable, holds a list of Entry objects and the total size

    :return: either the index or None
    :rtype: int or None
    """
    index = 0
    while index != len(hTable.table):
        if hTable.table[index] == None:
            pass
        elif hTable.table[index].name == name:
            return index
        
        index += 1

    return None
