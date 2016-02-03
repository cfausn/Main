"""
   airExpress.py
   Colin Fausnaught

   opens a file, creates priority queue, gets data from a input file, then adds
   the data to the queue.
"""
from myPriorityQueue import *
from passengerClass import *

def main():
    """
    opens a file, creates a priority queue, then either adds the data from the file
    to the priority queue or simulates boarding and removes them from the queue.
    """
    name = input("Enter file name: ")
    file = open(name)
    checkinLine = createPriorityQueue()
    tempArray = []
    
    for line in file:
        tempArray = line.split(" ")
        if tempArray[0] == 'checkin':
            insert(checkinLine, Passenger(tempArray[1], int(tempArray[2])))
        elif tempArray[0] == 'board':
            boardPlane(checkinLine, int(tempArray[1]))
    
    print("\n~~~~~~~~~~~~~~~~~~ Gate is closed. (end of simulation) ~~~~~~~~~~~~~~~~~~")
    while not emptyQueue(checkinLine):
        print(front(checkinLine).name + " was left at the gate.")
        remove(checkinLine)

    file.close()
    print("\nSIMULATION OVER")

def boardPlane(pq, num):
    """
    boards the plane based on the number passed and the priority of the passenger,
    then removes the value from the priority queue.

    :param pq: Queue, the priority queue
    :param num: int, the number that the boarding stops at
    """
    print("\n~~~~~~~~~~~~~~~~~~ Now boarding seats 600 down to " + str(num)\
          + " ~~~~~~~~~~~~~~~~~~")
    while front(pq).priority >= num:
        print(front(pq).name + " is now boarding for seat " + str(front(pq).priority))
        remove(pq)
        
main()
