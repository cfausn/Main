#!/usr/local/bin/python3

"""
File: myListRec.py
Author: Sean Strout <sps@cs.rit.edu>
Contributor: ben k steele <bks@cs.rit.edu>
Language: Python 3
Description:  A recursive implementation of a node based singly linked list
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
    _types    = (object, int,    object)
    
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
    
    return '[' + toStringRec(lst.head) + ']'
    
def toStringRec(node):
    """
    Converts our linked list into a string form that is similar to Python's
    printed list.
    
    Restrictions: Intended for internal use (not for client)
    Parameters:
        node (Node or None) - The current node in the list
    Returns:
        A string representation of the list (e.g. '[1,2,3]')
    """
    
    if node == None :
        return ''
    elif node.next == None :
        return str(node.data)
    else:
        return str(node.data) + ', ' + toStringRec(node.next)
                                    
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
        lst.head = Node(value, None )
    else:
        appendRec(lst.head, value)
        
    lst.size += 1
        
def appendRec(node, value):
    """
    Add a node containing the data to the end of the list.  This is the 
    helper function intended to be called directly by the client. 

    Restrictions: Intended for internal use (not for client)
    Parameters:
        node (Node or None) - The current node in the list
        value (any type) - The data to append to the end of the list
    Returns:
        None
    """
    if node.next == None :
        node.next = Node(value, None )
    else:
        appendRec(node.next, value)
        
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
        insertRec(lst.head, index-1, value)
        
    lst.size += 1
        
def insertRec(node, index, value):
    """
    Insert a new element before the index.
    
    Restrictions: Intended for internal use (not for client)
    Parameters:
        node (Node or None) - The current node in the list
        index (int) - The 0 based index to insert before
        value (any type) - The data to be inserted into the list
    Returns:
        A Node representing the head of the list
    """
    
    if index == 0:
        node.next = Node(value, node.next)
    else:
        insertRec(node.next, index-1, value)
        
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
        
    return getRec(lst.head, index)
    
def getRec(node, index):
    """
    Returns the element that is at index in the list.
    
    Restrictions: Intended for internal use (not for client)
    Parameters:
        head (Node or None) - The head of the list
        index (int) - The 0 based index to get    
    Returns:
        A Node (or Empty Node) representing the head of the list    
    """    
    
    if index == 0:
        return node.data
    else:
        return getRec(node.next, index-1)
        
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

    setRec(lst.head, index, value)

def setRec(node, index, value):
    """
    Sets the element that is at index in the list to the value.

    Parameters:
        node (Node) - the current node 
        index (int) - The 0 based index to set
        value (any type)   
    Preconditions:
        0 <= index <= lst.size, raises IndexError exception   
    Returns:
        None
    """    
    
    if index == 0:
        node.data = value
    else:
        return setRec(node.next, index-1, value)
        
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
        value = popRec(lst.head, index-1)
    
    lst.size -=1
    return value
        
def popRec(node, index):
    """
    Remove the element at index.
    
    Restrictions: Intended for internal use (not for client)
    Parameters:
        node (Node or None) - The current node in the list
        index (int) - The 0 based index to remove   
    Returns:
        The value (any type) being popped
    """
    if index == 0:
        value = node.next.data
        node.next = node.next.next
        return value
    else:
        return popRec(node.next, index-1)
        
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
    return indexRec(lst.head, value, 0)
        
def indexRec(node, value, index):
    """
    Returns the index of the first occurrence of a value in the list
    
    Restrictions: Intended for internal use (not for client)
    Parameters:
        node (Node or None) - The current node in the list
        value (any type) - The data being searched for 
    Preconditions:
        value exists in list, otherwise raises ValueError exception
    Returns:
        The index (int) of value or None if value is not present in the list
    """    
    
    if node == None :
        raise ValueError(str(value) + " is not in list")
    elif node.data == value:
        return index
    else:
        return indexRec(node.next, value, index+1)

