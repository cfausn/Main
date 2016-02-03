"""
description: open addressing Hash Table for CS 141 Lecture
file: hashtable.py
language: python3
author: sps@cs.rit.edu Sean Strout
author: jeh@cs.rit.edu James Heliotis
author: anh@cs.rit.edu Arthur Nunes-Harwitt
author: jsb@cs.rit.edu Jeremy Brown
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
    __slots__ = ( 'table', 'size' )
    _types    = (list, int)


def createHashTable(capacity=100):
  """
  createHashTable: NatNum? -> HashTable
  """
  aHashTable = HashTable([None for _ in range(capacity)], 0)
  return aHashTable

def HashTableToStr(hashtable):
  """
  HashTableToStr: HashTable -> String
  """
  result = ""
  for i in range(len(hashtable.table)):
      e = hashtable.table[i]
      if not e == None:
          result += str( i ) + ": "
          result += EntryToStr(e) + "\n"
  return result


class Entry(rit_object):
    """
       A class used to hold key/value pairs.
    """

    __slots__ = ( "key", "value" )
    _types = (object, object)


def EntryToStr(entry):
  """
  EntryToStr: Entry -> String
  return the string representation of the entry.
  """
  return "(" + str( entry.key ) + ", " + str( entry.value ) + ")"


def hash_function( val, n ):
    """
    hash_function: K NatNum -> NatNum
    Compute a hash of the val string that is in [0 ... n).
    """
    hashcode = hash( val ) % n
    # hashcode = 0
    # hashcode = len(val) % n
    return hashcode

def keys( hTable ):
    """
    keys: HashTable(K, V) -> List(K)
    Return a list of keys in the given hashTable.
    """
    result = []
    for entry in hTable.table:
        if entry != None:
            result.append( entry.key )
    return result

def has( hTable, key ):
    """
    has: HashTable(K, V) K -> Boolean
    Return True iff hTable has an entry with the given key.
    """
    index = hash_function( key, len( hTable.table ) )
    startIndex = index # We must make sure we don't go in circles.
    while hTable.table[ index ] != None and hTable.table[ index ].key != key:
        index = ( index + 1 ) % len( hTable.table )
        if index == startIndex:
            return False
    return hTable.table[ index ] != None

def put( hTable, key, value ):
    """
    put: HashTable(K, V) K V -> Boolean

    Using the given hash table, set the given key to the
    given value. If the key already exists, the given value
    will replace the previous one already in the table.
    If the table is full, an Exception is raised.
    """
    index = hash_function( key, len( hTable.table ) )
    startIndex = index # We must make sure we don't go in circles.
    while hTable.table[ index ] != None and hTable.table[ index ].key != key:
        index = ( index + 1 ) % len( hTable.table )
        if index == startIndex:
            raise Exception( "Hash table is full." )
    if hTable.table[ index ] == None:
        hTable.table[ index ] = Entry( key, value )
        hTable.size += 1
    else:
        hTable.table[ index ].value = value
    return True

def get( hTable, key ):
    """
    get: HashTable(K, V) K -> V

    Return the value associated with the given key in
    the given hash table.

    Precondition: has(hTable, key)
    """
    index = hash_function( key, len( hTable.table ) )
    startIndex = index # We must make sure we don't go in circles.
    while hTable.table[ index ] != None and hTable.table[ index ].key != key:
        index = ( index + 1 ) % len( hTable.table )
        if index == startIndex:
            raise Exception( "Hash table does not contain key." )
    if hTable.table[ index ] == None:
        raise Exception( "Hash table does not contain key." )
    else:
        return hTable.table[ index ].value
