'''
file: testSorts.py
version: python3
author: Sean Strout
author: James Heliotis
purpose:  A test program for the various sorting algorithms.  All
    functions are assumed to be non-mutating (return a newly
    sorted list):
    - qsPivotFirst: quicksort, pivot is first element in list
    - qsPivotMedian3: quicksort, pivot is median of first, middle, last
    - heapSort: heapsort, based on heap priority queue from lecture
    - quipSort: hybrid qsPivotMedian3 + heapSort
'''

import random
import qsPivotFirst
import qsPivotMedian3
import heapSort
import quipSort
import time
import collections
from decimal import *


# all sorts are non-mutating and are stored in a named tuple
def constructSorts():
    """
    Constructs and returns a namedtuple, SortType, containing
    information about the sorts, inclusing their name, function
    and the maximum N they can be run with.
    (Named tuples are classes constructed in a simple way.)
    """
    SortType = collections.namedtuple('SortType', 'name function maxN')
    return \
        SortType('qsPivotFirst', qsPivotFirst.quickSort, 10**5), \
        SortType('qsPivotMedian3', qsPivotMedian3.quickSort, 10**5), \
        SortType('heapSort', heapSort.heapSort, 10**6), \
        SortType('quipSort', quipSort.quipSort, 10**6)

def constructDataSets(N):
    """
    Constructs and returns a namedtuple, DataSet, containing
    information about various test data sets, including the data (tuple),
    and a descrption (string)
    """
    randomData = [i for i in range(N)]
    random.shuffle(randomData)
    randomData = tuple(randomData)

    ascendingData = (i for i in range(N))
    descendingData = (i for i in range(N-1,-1,-1))

    evenData = (i for i in range(0,N,2))
    oddData = (i for i in range(1,N,2))
    evenOddData = tuple(evenData) + tuple(oddData)

    DataSet = collections.namedtuple('DataSet', 'data msg')
    return \
        DataSet(tuple(randomData), 'Random data, N:' + str(N)), \
        DataSet(tuple(ascendingData), 'Ascending data, N:' + str(N)), \
        DataSet(tuple(descendingData), 'Descending data, N:' + str(N)), \
        DataSet(tuple(evenOddData), 'EvenOdd data, N:' + str(N))

def performSort(sortType, dataSet, N):
    """
    Performs a single sort on a data sample of size N.  If it can
    run it, it displays the time results
    """
    print('\t', dataSet.msg, end=' -> ')
    try:
        if N <= sortType.maxN:
            start = time.clock()
            result = sortType.function(dataSet.data)
            runTime = time.clock() - start

        else:
            runTime = 0
            print("N is too large to test!")

    except RuntimeError as exc:
        print("\n\t\tRUNTIME ERROR:", str(exc)[:32]+'...')
    except MemoryError as exc:
        print("MEMORY ERROR:", str(exc))
    else:
        if N <= sortType.maxN:
           print('Time: %3.5s' % Decimal(runTime) , ', Sorted?', \
                sorted(dataSet.data) == result)
           # print('Time:', ( "%1.3e" % runTime ), ', Sorted?', \
           #    sorted(dataSet.data) == result)

def run(sortName=None):
    """
    Run all the sorts (if sortName is None), otherwise runs
    only the sort that matches the sortName.  Data set
    sizes are fixed at 1, 10, 100, 1000, 10000, 100000, 1000000
    """
    for N in [10**i for i in range(7)]:
        dataSets = constructDataSets(N)
        if sortName == None:
            print('Testing all sorts with N:' + str(N))
        else:
            print('Testing', sortName, 'with N:' + str(N))
        for sortType in constructSorts():
            if sortName == None:
                print(sortType.name + ":")
            for data in dataSets:
                if sortName == None or sortType.name == sortName:
                    performSort(sortType, data, N)
        if sortName == None:
            print("----------------------------------")

if __name__ == '__main__':
    run()
