"""
A queue class. None is used to indicate the back of the queue
(as well as the front of an empty queue).

file: myPriorityQueue.py
Author: Colin Fausnaught
"""

from passengerClass import *

class Queue(rit_object):
    """
    object is specified as the type of the 'front' and
    'back' slots so that either None or a Node object
    can be used as valid assignments.
    """
    __slots__ = ( 'front', 'back', 'size' )
    _types    = ( object,  object, int    )

def createPriorityQueue():
    """
    Creates an empty Queue and returns it
    """
    return Queue(None,None,0)

def insert(queue, element):
    """
    inserts the element into the queue based on the seat the passenger is
    in. Uses nested if statements and while loops to accomplish this task.

    :param queue: the queue to insert an element into
    :param element: Passenger (Node), the element to be inserted
    """
    
    while not emptyQueue(queue):
        if queue.back == None and element.priority < queue.front.priority:
            queue.back = element
            break
        
        elif element.priority > queue.front.priority:
            newnode = queue.front
            
            newnode.next = queue.back
            queue.back = newnode
            queue.front = element
            break
        
        elif element.priority < queue.front.priority and \
            element.priority < queue.back.priority:

            newQueue = queue
            backElm = newQueue.back
            counter = 0
            while counter != queue.size:

                if newQueue.back.next == None:
                    newQueue.back.next = element
                    counter += 1
                    break
                elif element.priority < newQueue.back.priority and\
                     element.priority > newQueue.back.next.priority:
                    element.next = newQueue.back.next
                    newQueue.back.next = element
                    break
                else:
                    newQueue.back = newQueue.back.next
                
                counter += 1
            
            queue.back = backElm
            break

        elif element.priority < queue.front.priority and \
             element.priority > queue.back.priority:
            element.next = queue.back
            queue.back = element
            break
        
            
            
    if emptyQueue(queue):
        queue.front = element

    queue.size += 1
    



        
def remove(queue):
    """
    removes the top element from the queue and returns the queue

    :param queue: the queue to remove an object from

    :rtype: Queue
    :return: the queue with the removed element
    """
    if emptyQueue(queue):
        raise IndexError("remove on empty queue")
    
    if queue.back == None:
        queue.front = None
        queue.size -= 1
        return queue
    
    queue.front = Passenger(queue.back.name, queue.back.priority)
    queue.back = queue.back.next
    if emptyQueue(queue):
        queue.back = None
    queue.size -= 1
    return queue
    
def front(queue):
    """
    returns the front element of the queue without removing it.

    :param queue: the queue to return the front element of

    :rtype: Node (called in my program as Passenger)
    :return: the front element of the queue
    """
    if emptyQueue(queue):
        raise IndexError("front on empty queue") 
    return queue.front
    
    
def emptyQueue(queue):
    """
    decides if the queue is empty or not.

    :param queue: the queue test if empty

    :rtype: Boolean
    :return: True/False
    """
    return queue.front == None
