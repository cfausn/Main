#!/usr/local/bin/python3

"""
File: myListIter.py
Author: Sean Strout <sps@cs.rit.edu>
Contributor: ben k steele <bks@cs.rit.edu>
             Colin Fausnaught
Language: Python 3
Description:  An iterative implementation of a node based single linked list
data structure.
Purpose: 
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




############################## - STUDENT CODE - ######################################

def count(lst, value):
    """
    Returns the count of a value in the list

    Parameters:
         lst (MyList) - the list to be counted from
         value (any type) - the data to be counted

    Preconditions:
         value either exists in list or doesn't, counter will be returned either way
         
    Returns:
         counter, which holds the total number of times the value was found
    """
    counter = 0
    sizes = lst.size
    prev = lst.head
    
    if lst.head == None:
        return counter
    
    while True:
        if lst.head == None:
            break
        
        if lst.head.data == value:
            counter += 1

        lst.head = lst.head.next
        
    lst.head = prev
    return counter

def myListToPyList(lst):
    """
    Returns a python list object from a MyList object

    Parameters:
         lst (MyList) - the list to be counted from Mylist to Python List

    Preconditions:
         lst is a MyList object, needs to be converted
         
    Returns:
         newList, a python list from the MyList object
    """
    newList = []
    
    prev = lst.head
    sizes = lst.size
    
    while lst.size != 0:
        newList += lst.head.data
        lst.size -= 1
        lst.head = lst.head.next

    lst.head = prev
    lst.size = sizes
    return newList

def pyListToMyList(pylst):
    """
    Returns a MyList object from a python list object.

    Parameters:
         pylst (List) - the list to be turned into a MyList Object

    Preconditions:
         list has been passed to be converted
         
    Returns:
         lst, a MyList version of pylst
    """
    lst = createEmptyList()
    sizes = 0

    if len(pylst) == 0:
        return lst
    
    while sizes != len(pylst) :
        append(lst, pylst[sizes])
        sizes+=1

    lst.size = sizes
    return lst

def remove(lst, value):
    """
    Removes a value from a MyList object and then returns True or False

    Parameters:
         lst (MyList) - the list to have an object removed
         value (any type) - the data to be removed

    Preconditions:
         value either exists in list or doesn't, a value will be returned either way
         
    Returns:
         True or False, based on whether the function removed something or not.
    """
    if lst.head == None:
        return False
    
    prev = lst.head
    current = prev
    indexs = index(lst, value)
    sizes = lst.size
    while True:
        if current.data == value:
            if lst.head.data == current.data:
                lst.head = prev.next
                sizes -= 1
                lst.size = sizes
                return True
            else:
                pop(lst,indexs)
                sizes -= 1
                lst.size = sizes
                return True
        
        
        current = current.next

