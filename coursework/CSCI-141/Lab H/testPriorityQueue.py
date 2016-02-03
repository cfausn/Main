"""
    testPriorityQueue.py
    Colin Fausnaught

    tests myPriorityQueue and passengerClass 
"""

from myPriorityQueue import *
from passengerClass import *

def main():
    """
         Tests myPriorityQueue.py and myNode.py
    """
    pq = createPriorityQueue()
    print("Is queue empty?" ,emptyQueue(pq) == True)
    insert(pq, Passenger("Fred", 5))
    print("Is front Fred/5?", \
          front(pq).name == "Fred" and front(pq).priority == 5)

    insert(pq, Passenger("Wilma", 7))
    print("Is size 2?", pq.size == 2)
    insert(pq, Passenger("Pebbles", 6))
    print("Is front Wilma/7", \
          front(pq).name == "Wilma" and front(pq).priority == 7)
    insert(pq, Passenger("George", 8))
    print("Is front George/8", \
          front(pq).name == "George" and front(pq).priority == 8)


    insert(pq, Passenger("Don", 3))
    print("Is size 5?", pq.size == 5)
    insert(pq, Passenger("Drake", 4))

    insert(pq, Passenger("Jamie", 10))
    print("Is front Jamie?/10", \
          front(pq).name == "Jamie" and front(pq).priority == 10)
    insert(pq, Passenger("Blane", 9))

    print("dumping queue")
    while not emptyQueue(pq):
        print(remove(pq))


    print("Queue Empty?", emptyQueue(pq) == True)

    insert(pq, Passenger("Wilma", 7))
    insert(pq, Passenger("Travis", 3))
    insert(pq, Passenger("Ted", 5))
    insert(pq, Passenger("Wilma", 9))

    print("is front Wilma/9?", \
          front(pq).name == "Wilma" and front(pq).priority == 9)

    while not emptyQueue(pq):
        print(remove(pq))

main()
