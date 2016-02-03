"""
file: qsPivotFirst.py
version: python3
author: Sean Strout
author: Colin Fausnaught
purpose: Implementation of the quicheSort algorithm (not in place),
    It first uses quickSort, using the median-of-3 pivot, until it
    reaches a recursion limit bounded by int(math.log(N,2)).
    Here, N is the length of the initial list to sort.
    Once it reaches that depth limit, it switches to using heapSort instead of
    quicksort.
"""

import heapSort             # heapSort
import math                 # log2 (for quicksort depth limit)
import qsPivotMedian3
import testSorts            # run (for individual test run)

def quipSortRec(lst, limit):
    """
    A non in-place, depth limited quickSort, using median-of-3 pivot.
    Once the limit drops to 0, it uses heapSort instead.

    :param lst: a list to be sorted
    :param limit: the log base 2 limit to recurse

    :return: a sorted list
    """
    if 0 >= limit:
        return heapSort.heapSort(lst)
    elif lst == []:
        return []
    else:
        pivot = qsPivotMedian3.medianOf3(lst)
        (less,same,more) = qsPivotMedian3.partition(pivot,lst)
        return quipSortRec(less, limit-1) + same + quipSortRec(more, limit-1)


def quipSort(lst):
    """
    The main routine called to do the sort.  It should call the
    recursive routine with the correct values in order to perform
    the sort

    :param lst: unsorted list

    :return: a sorted list using quipSortRec()
    """

    return quipSortRec(lst, math.log(len(lst), 2))

if __name__ == "__main__":
    testSorts.run('quipSort')
