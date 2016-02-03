"""
    bieberhash.py
    Colin Fausnaught

    uses a hash table to organize the contents of a file and update the tabs
    of each guest.
"""

from hashtable import *

def main():
    """
    gets the hash table size and the filename, then calls
    create_bills to organize the hashtables and to update
    the tabs
    """
    hashSize = int(input("How big a hashtable to use: "))
    filename = input("Enter file name: ")
    create_bills(hashSize, filename)
    
    

def create_bills(size, filename):
    """
    first updates the table based on the contents of a file and updates
    the value of 'tab', the running total bill for that person.

    :param size: int, the number of seats in the hashtable
    :param filename: string, the name of the file
    """
    tList = []  #empty list with contents of the filename
    mySet = set() #the names of the guests
    index = 0
    hTable = createHashTable(size) #hash table with empty values
    for line in open(filename):
        tLst = line.split(" $")
        if not tLst[0] in mySet:

            guest = createGuest(tLst[0], size, int(tLst[1]))
            mySet.add(tLst[0])
            put(hTable, guest)
            
        else:
            if hTable.table[firstSeat(tLst[0],size)].name == tLst[0]:
                hTable.table[firstSeat(tLst[0],size)].value.tab += int(tLst[1])
            elif hTable.table[secondSeat(tLst[0],size)].name == tLst[0]:
                hTable.table[secondSeat(tLst[0],size)].value.tab += int(tLst[1])
        
    #prints if an excpetion isn't raised
    for elm in mySet:
        index = indexOf(elm, hTable)
        print(hTable.table[index].name + " owes $" + \
                  str(hTable.table[index].value.tab) + " and is in seat " + str(index))

        

if __name__ == '__main__':
    main()
