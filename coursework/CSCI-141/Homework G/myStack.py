"""
Stack operations.

author: Aaron Deever

file: myStack.py
"""

"""
NOTE : we can alert to errors using the raise keyword, and specifying
what type of error it is (and providing a message)
(IndexError is a special keyword type of error).
This will tell our program to terminate.
"""

from myNode import *

def push(node, el):
    """ node is reference to current top of stack, el is data to add.
    this funtion is changing the reference to the top of the stack
    and needs to return this new reference. """
    newNode = Node(el, node)
    return newNode

def emptyStack(node):
    """ needs to just determine if empty """
    return node == None

def top(node):
    """ takes current stack, return data at top of stack """
    if(emptyStack(node)):
        raise IndexError("Top on empty stack")
    
    return node.data

def pop(node):
    """ takes current stack, pops off top element and returns new stack top"""
    if(emptyStack(node)):
        raise IndexError("Pop on empty stack")

    return node.next

def size(node):
    """ recursively computes """
    if (node == None):
        return 0

    else:
        1 + size(node.next)
