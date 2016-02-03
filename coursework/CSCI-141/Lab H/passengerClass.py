"""
File: passengerClass.py
Purpose: rit_object LECTURE VERSION
Author: Sean Strout <sps@cs.rit.edu>
Contributor: ben k steele <bks@cs.rit.edu>
             Colin Fausnaught
Language: Python 3
Description:  A representation of a single linked node intended
to be used as the building blocks for a linked list.
"""

from rit_object import *

###########################################################
# NODE CLASS DEFINITIONS
###########################################################

class Node( rit_object ):
    """
    A representation of a linked list node
    slots
        name: the name of the passenger
        priority: the seat that the passenger is in
        next: either a Node reference or None
    """
    __slots__ = ('name','priority','next')
    _types = ( str, int, object)

def Passenger(name, priority):
    """
    MUST CALL THIS TO CREATE THE PASSENGER NODE!!!!
    The reason this is a function and not a class is so
    the program can call Passenger with just a name and the priority.

    :rtype: Node
    :return: A node with the name and priority in it
    """
    return Node(name,priority,None)
