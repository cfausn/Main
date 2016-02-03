"""
Node class that will hold a data value and a reference to the next node.

author:  Aaron Deever

file:  myNode.py
"""

"""
NOTES:

1) Again, we use rit_object to specify the types for each slot

2)  Sometimes, we want flexibility.  We use object as type to
indicate we want to allow anything to be put there

3) Node is a self-referential data structure.  To specify that
one of our slots is a reference to that data type being currently
defined, we use the name of the class as a string.

4) When we want to create a Node object, we call Node(pass in arguments
for the slots)

5) the . notation can be extended as far as there are objects

6) When we use 'Node' as our slot, rit_object knows we have
self-reference, and it lets us also put None in there.

"""

from rit_object import *

class Node(rit_object):
    __slots__ = ('data', 'next')
    _types    = (object, 'Node')

# creating some nodes to make a stack
#myStack = None  # start with empty stack
#myStack1 = Node(1, myStack) # but we'll see in general next is myStack
#myStack2 = Node(2, myStack1)
#myStack3 = Node(3, myStack2)
#print(myStack3)

# creating 1,2,3 stack using just one stack variable
myStack = None  # start with empty stack
myStack = Node(1, myStack) # but we'll see in general next is myStack
myStack = Node(2, myStack)
myStack = Node(3, myStack)
print(myStack)

print(myStack.data)
print(myStack.next.data)
print(myStack.next.next.data)
#print(myStack.next.next.next.data)

# another way we could have built up the stack
stack2 = Node(3, Node(2, Node(1, None)))
print(stack2)

