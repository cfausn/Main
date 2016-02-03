"""
    findFast.py
    Colin Fausnaught
    10/5/14

    uses a slow algorithm to find the median of distances. Then finds
    the sum of the distances and returns both.
"""

import time

def medianFunc(lst):
    """
         Finds median quickly by using fastSelect(), based on whether the list passed is
         odd or even. If it is even, the median returned will be an average of the two
         values in the middle of the list.

         Pre-Conditions: No median found
                         No sum calculated

         Post-Conditions: Median has been found and returned
                          ready to find sum
    """
    if len(lst) % 2 == 1:
        median = fastSelect(lst, ((len(lst)-1) // 2))
    else:
        median = (fastSelect(lst, ((len(lst)-1) // 2)) + fastSelect(lst, (((len(lst)-1) // 2) + 1))) /2

    return median
    
def fastSelect(lst, k):
    """
         fastSelect() is crucial to this program. It uses the algorithm given in the
         lab paper to find a pivot point (the kth smallest number), which in this case
         will be the median value.

         Pre-Conditions: No median found
                         K has been passed, which signifies the kth smallest number (median index)

         Post-Conditions: Median has been returned
    """
    while lst is not []:
        pivot = lst[(len(lst)//2)]
        smallList = smallerList(lst,pivot)
        largeList = largerList(lst,pivot)
        count = lst.count(pivot)
        m = len(smallList)

        if k >= m and k < (m + count):
            return pivot
        elif m > k:
            lst = smallList
        else:
            k = k - m - count
            lst = largeList

def smallerList(lst,pivot):
    """
         Utility function used to find the value of smallList in fastSelect(). Returns all values
         that are less than the pivot point in a list.

         Post-Conditions: List of smaller numbers than pivot has been returned
    """
    x = 0
    smallList = []
    while x != len(lst):
        if lst[x] < pivot:
            smallList.append(lst[x])
        x+=1
    return smallList

def largerList(lst,pivot):
    """
         Utility function used to find the value of largeList in fastSelect(). Returns all values
         that are greater than the pivot point in a list.

         Post-Conditions: List of greater numbers than pivot has been returned
    """

    x = 0
    largeList = []
    while x != len(lst):
        if lst[x] > pivot:
            largeList.append(lst[x])
        x+=1
    return largeList


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
        return getInt(line,x+1) + line[-x]

    
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
