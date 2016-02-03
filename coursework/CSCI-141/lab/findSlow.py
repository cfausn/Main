"""
    findSlow.py
    Colin Fausnaught
    10/5/14

    uses a slow algorithm to find the median of distances. Then finds
    the sum of the distances and returns both.
"""

import time

#Lecture Code used to Sort
def swap( lst, i, j ):
    """
    swap: List NatNum NatNum -> None
    swap the contents of list at pos i and j.
    Parameters:
        lst - the list of data
        i   - index of one datum
        j   - index of the other datum
    """
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

def insert( lst, mark ):
    """
    insert: List(Orderable) NatNum -> None
    Move the value at index mark+1 so that it is in its proper place.
    Parameters:
        lst - the list of data 
        mark - represents cutting the list between 
               index mark and index mark+1
    pre-conditions:
      lst[0:mark+1] is sorted.
    post-conditions:
      lst[0:mark+2] is sorted.
    """
    index = mark
    while index > -1 and lst[index] > lst[index+1]:
        swap( lst, index, index+1 )
        index = index - 1

def insertion_sort( lst ):
    """
    insertion_sort : List(Orderable) -> None
    Perform an in-place insertion sort on a list of orderable data.
    Parameters:
        lst - the list of data to sort
    post-conditions:
        The data list has been sorted.
    """
    for mark in range( len( lst ) - 1 ):
        insert( lst, mark )
        
#End of Lecture Code
        
def medianFunc(lst):
    """
         finds the median slowly by using the insertion_sort() code from
         the lecture, then finding the median based on whether the
         length of the list is odd or even.

         Pre-Conditions: list is unsorted
                         no median found yet
                         no sum calculated
                         
         Post-Conditions: List has been sorted
                          median has been found
                          ready to find the sum
    """
    insertion_sort(lst)
    length = len(lst)
    median = 0
    if length % 2 == 1:
        median = lst[length//2]
    else:
        median = (lst[length//2] + lst[(length//2) - 1]) / 2

    return median


def sumFunc(lst, opt):
    """
         used to find the sum of the distances between the optimal
         location and all other distances.

         Pre-Conditions: Median has been found

         Post-Conditions: Sum of the distances has been calculated and returned.
    """
    sumS = 0
    for x in lst:
        if x == opt:
            pass
        elif x > opt:
            sumS += (x - opt)
        else:
            sumS += (opt - x)
    return sumS

def getInt(line,x):
    """
         utlilty function used to convert parts of the string input into
         an int to be stored in the list.

         Pre-Conditions: Full string of line has been passed

         Post-Conditions: The number values of the line have been returned
                              in STRING format (has to be converted in the
                              calling function)
    """
    if line[-x] == ' ':
        return ""
    else:
        return getInt(line,x+1) + line[-x ]

    
def fileManagement():
    """
         Used to get the filename input from the user. Also creates a list
         based on the file's stored values.

         Pre-Conditions: main() has called fileManagment
                         no data has been entered

         Post-Conditions: File has been opened and closed
                          Contents of file has been read
                          contents of file has been converted to list
                          list has been returned
    """
    filename = input("Enter filename: ")
    f = open(filename, encoding='utf-8')
    lst = []
    x = 1
    for line in f:
        lst += [int(getInt(line,x))]
        
    f.close()
    return lst
    
def main():
    """
         Used to structure the program. Calls other function to get list, median,
         sum of distances and then prints them.
    """
    lst = fileManagement()
    starttime = time.clock()
    median = medianFunc(lst)
    sums = sumFunc(lst,median)
    print("Optimal Location: " + str(median))
    print("Sum of distance traveled: " + str(sums))
    print("Runtime: " + str(time.clock() - starttime))

main()

