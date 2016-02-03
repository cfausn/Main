"""
Program to test queue implementation.  Assumes None is
used to indicate the back of the queue, as well as the
front of an empty queue.

file:  myQueueViaStacks.py

Modified By: Colin Fausnaught
"""

from myQueueViaStacks import *

def main():
    # begin with an empty queue
    queueCh = QueueViaStacks(push(None,None), push(None,None), 0)
    print("Creating empty queue...")
    print("Queue empty?", True == emptyQueue(queueCh))
    print("Queue size is 0?", 0 == queueCh.size)
    
    
    # add first element to first stack
    print("\nenqueue A1... to stack 1")
    enqueue(queueCh, 'A1')
    print("Queue not empty?", False == emptyQueue(queueCh))
    print("Queue size is 1?", 1 == queueCh.size)
    print("First Element of Stack 1 is A1?", 'A1' == front(queueCh))
    print("First Element of Stack 2 is None?", None == back(queueCh))
    
    # add first element to second stack
    print("\nenqueue A2... to stack 2")
    enqueue(queueCh, 'A2')
    print("First Element of Stack 1 is A1?", 'A1' == front(queueCh))
    print("First Element of Stack 2 is A2?", 'A2' == back(queueCh))
    
    # add second element to first stack
    print("\nenqueue B1... to stack 1")
    enqueue(queueCh, 'B1')
    print("Queue not empty?", False == emptyQueue(queueCh))
    print("Queue size is 3?", 3 == queueCh.size)
    print("First Element of Stack 1 is B1?", 'B1' == front(queueCh))
    print("First Element of Stack 2 is A2?", 'A2' == back(queueCh))
    
    # add second element to second stack
    print("\nenqueue B2... to stack 2")
    enqueue(queueCh, 'B2')
    print("Queue size is 4?", 4 == queueCh.size)
    print("First Element of Stack 1 is B1?", 'B1' == front(queueCh))
    print("First Element of Stack 2 is B2?", 'B2' == back(queueCh))
    
    # add third element to first stack
    print("\nenqueue C1... to stack 1")
    enqueue(queueCh, 'C1')
    print("Queue size is 5?", 5 == queueCh.size)
    print("First Element of Stack 1 is C1?", 'C1' == front(queueCh))
    print("First Element of Stack 2 is B2?", 'B2' == back(queueCh))
    
    # dequeue front element, C1
    print("\ndequeue...")
    dequeue(queueCh)
    print("Queue not empty?", False == emptyQueue(queueCh))
    print("Queue size is 4?", 4 == queueCh.size)
    print("First Element of Stack 1 is B1?", 'B1' == front(queueCh))
    print("First Element of Stack 2 is B2?", 'B2' == back(queueCh))
        
    # add third element to the second stack
    print("\nenqueue C2... to stack 2")
    enqueue(queueCh, 'C2')
    print("First Element of Stack 1 is B1?", 'B1' == front(queueCh))
    print("First Element of Stack 2 is C2?", 'C2' == back(queueCh))
    
    # Empty the queue
    print("\nEmptying the queue...")
    while not emptyQueue(queueCh):
        print("Front of queue:", front(queueCh))
        print("Back of queue:", back(queueCh))
        print("dequeue...")
        dequeue(queueCh)
        
    print("Success! Queue Emptied.")
 
main()
