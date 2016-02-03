"""
myQueueViaStacks.py

Author: Colin Fausnaught

creates a queue via stacks, using the myNode and rit_object files.
"""
from rit_object import *
from myNode import *
from myStack import *

class QueueViaStacks(rit_object):
    """
    custom object, stack1 is the 'front' object and stack2 is the 'back' object.
    They are defined as objects so None can be assigned to them.
    """
    __slots__ = ('stack1','stack2','size')
    _types = (object, object, int)

def enqueue(que, element):
    """
    Inserts an element into the queue based on how the element is named, if
    a 1 preceedes it then it will go in stack 1, if a 2 then stack 2.

    :param que: the running queue
    :param element: the inserted element

    :rtype: None
    """
    newNode = push(None,element)
    if emptyQueue(que):
        que.stack1 = newNode
    elif not emptyQueue(que) and que.stack2.data == None:
        que.stack2 = newNode
    elif element[-1] == '1':
        que.stack1 = push(que.stack1 ,element)
    elif element[-1] == '2':
        que.stack2 = push(que.stack2, element)
        
    que.size += 1

def dequeue(que):
    """
    Removes the front element from the queue. Also will restructure the stacks
    by bringing data from stack2 into stack1 as stack1 is emptied.

    :param que: the running queue

    :return: When the queue is completely empty it will return None to exit
    :rtype: None
    
    
    """
    if emptyQueue(que):
        raise IndexError("dequeue on empty queue")
    
    que.stack1 = que.stack1.next
    
    if que.stack1 == None:
        if emptyStack(que.stack1) and emptyStack(que.stack2):
            que.stack1 = Node(None, None)
            que.size -=1
            return
            
        que.stack1 = Node(top(que.stack2), None)   
        if que.stack2 != None:
            que.stack2 = que.stack2.next
            
    elif emptyQueue(que):
        que.stack2 = None
        
    que.size -=1

def front(que):
    """
    Access and returns the first element of the queue without removal.

    :param que: The running queue

    :return: the first element's data
    :rtype: str
    """
    return que.stack1.data

def back(que):
    """
    Access and returns the last element of the queue without removal.

    :param que: the running queue

    :return: the last element's data
    :rtype: str
    
    :return: None if stack2 is empty
    :rtype: None
    """
    if que.stack2 == None:
        return None
    
    return que.stack2.data

def emptyQueue(que):
    """
    Checks to see if queue is empty, if so returns True

    :param que: the running queue

    :return: Whether the stack is empty or not
    :rtype: Bool
    """
    
    
    return que.size == 0

