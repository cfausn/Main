#!/usr/local/bin/python3

"""
File: myListIter.py
Author: Sean Strout <sps@cs.rit.edu>
Contributor: ben k steele <bks@cs.rit.edu>
Language: Python 3
Description:  An iterative implementation of a node based single linked list
data structure.
Purpose: LECTURE VERSION
"""

from myNode import *  # by extension, rit_object

###########################################################
# LINKED LIST CLASS DEFINITION                                
###########################################################

class MyList( rit_object ):
    """A class that encapsulates a node based linked list"""
    __slots__ = ('head', 'size', 'cursor')
    _types    = (object, int, object)
    
###########################################################
# LINKED LIST CLASS BUILDER                                
###########################################################

def createEmptyList():
    """
    Constructs and returns an empty list.

    Parameters:
        None
    Returns: 
        An empty list
    """
    
    lst = MyList( None, 0, None )
    return lst
    
###########################################################
# LINKED LIST CURSOR FUNCTIONS                                
###########################################################    
    
def reset(lst):
    """
    Resets the cursor to the start of the list
    
    Parameters:
        lst (MyList) - the linked list
    Returns:
        None
    """
    
    lst.cursor = lst.head
    
def hasNext(lst):
    """
    Returns True if the list has more elements.
    
    Parameters:
        lst (MyList) - the linked list
    Returns:
        True (bool) if the cursor is value
    """
        
    return not lst.cursor == None
    
def next(lst):
    """
    Returns the next element in the iteration.
    
    Parameters:
        lst (MyList) - the linked list
    Preconditions:
        If cursor is invalid, raises an IndexError exception
    Returns:
        The value (any type) referenced by the cursor
    """
    
    if lst.cursor == None :
        raise IndexError("cursor is invalid")
    
    val = lst.cursor.data
    lst.cursor = lst.cursor.next
    return val
    
###########################################################
# LINKED LIST FUNCTIONS                                
###########################################################
    
def clear(lst):
    """
    Make a list empty.
    Parameters:
        lst (MyList) - the linked list
    Returns:
        None
    """
    
    lst.head = None
    lst.size = 0
    lst.cursor = None
    
def toString(lst):
    """
    Converts our linked list into a string form that is similar to Python's
    printed list. 
    
    Parameters:
        lst (MyList) - The linked list
    Returns:
        A string representation of the list (e.g. '[1,2,3]')
    """
    
    result = '['
    curr = lst.head
    while not curr == None :
        if curr.next == None :
            result +=  str(curr.data)
        else:
            result += str(curr.data) + ', ' 
        curr = curr.next
    result += ']'
    
    return result
                                        
def append(lst, value):
    """
    Add a node containing the value to the end of the list. 

    Parameters:
        lst (MyList) - The linked list
        value (any type) - The data to append to the end of the list
    Returns:
        None
    """
    
    if lst.head == None :
        lst.head = Node(value, None)
    else:
        curr = lst.head
        while not curr.next == None :
            curr = curr.next
        curr.next = Node(value, None)
    
    lst.size += 1
            
def insertAt(lst, index, value):
    """
    Insert a new element before the index.

    Parameters:
        lst (MyList) - The list to insert value into
        index (int) - The 0 based index to insert before
        value (any type) - The data to be inserted into the list
    Preconditions:
            0 <= index <= lst.size, raises IndexError exception
    Returns:
        None
    """

    if index < 0 or index > lst.size:
        raise IndexError(str(index) + ' is out of range.')

    if index == 0:
        lst.head = Node(value, lst.head)
    else:
        prev = lst.head
        while index > 1:
            prev = prev.next
            index -= 1
        prev.next = Node(value, prev.next)
        
    lst.size += 1
    
def get(lst, index):
    """
    Returns the element that is at index in the list.

    Parameters:
        lst (MyList) - The list to insert value into
        index (int) - The 0 based index to get   
    Preconditions:
        0 <= index <= lst.size, raises IndexError exception   
    Returns:
        None
    """

    if index < 0 or index >= lst.size:
        raise IndexError(str(index) + ' is out of range.')

    curr = lst.head
    while index > 0:
        curr = curr.next
        index -= 1
    return curr.data
    
def set(lst, index, value):
    """
    Sets the element that is at index in the list to the value.

    Parameters:
        lst (MyList) - The list to insert value into
        index (int) - The 0 based index to set
        value (any type)   
    Preconditions:
        0 <= index <= lst.size, raises IndexError exception   
    Returns:
        None
    """

    if index < 0 or index >= lst.size:
        raise IndexError(str(index) + ' is out of range.')

    curr = lst.head
    while index > 0:
        curr = curr.next
        index -= 1
    curr.data = value
    
def pop(lst, index):
    """
    Remove and return the element at index.

    Parameters:
        lst (MyList) - The list to insert value into
        index (int) - The 0 based index to remove   
    Preconditions:
        0 <= index <= lst.size, raises IndexError exception   
    Returns:
        The value (any type) being popped
    """

    if index < 0 or index >= lst.size:
        raise IndexError(str(index) + ' is out of range.')

    lst.cursor = None
    if index == 0:
        value = lst.head.data
        lst.head = lst.head.next
    else:
        prev = lst.head
        while index > 1:
            prev = prev.next
            index -= 1
        value = prev.next.data
        prev.next = prev.next.next

    lst.size -=1
    return value

def index(lst, value):
    """
    Returns the index of the first occurrence of a value in the list

    Parameters:
        lst (MyList) - The list to insert value into
        value (any type) - The data being searched for 
    Preconditions:
        value exists in list, otherwise raises ValueError exception
    Returns:
        The index (int) of value or None if value is not present in the list
    """
    
    pos = 0
    curr = lst.head
    while not curr == None :
        if curr.data == value:
            return pos
        pos += 1
        curr = curr.next
        
    raise ValueError(str(value) + " is not present in the list")

