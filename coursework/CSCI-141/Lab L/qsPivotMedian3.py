"""
file: qsPivotMedian3.py
version: python3
author: Sean Strout
author: Colin Fausnaught
purpose: Implementation of the quick-sort algorithm (not in-place).  The 
    pivot is chosen always to be the median-of-3 (the median of
    the first, middle and last values)
"""

import testSorts        # run (for individual test run)

def medianOf3(lst):
    """
    From a lst of unordered data, find and return the the median value from
    the first, middle and last values.
    """
    if len(lst) == 1:
        return lst[0]
    elif len(lst) == 2:
        if lst[0] < lst[1]:
            return lst[0]
        else:
            return lst[1]
    elif len(lst) == 3:
        if lst[0] < lst[1] < lst[2]:
            return lst[1]
        elif lst[2] < lst[1] < lst[0]:
            return lst[1]
        elif lst[1] < lst[0] < lst[2]:
            return lst[0]
        else:
            return lst[2]
    else:
        mid = len(lst)//2
        if lst[0] < lst[mid] and lst[mid] < lst[len(lst)-1]:
            return lst[mid]
        elif lst[mid] < lst[0] and lst[0] < lst[len(lst)-1]:
            return lst[0]
        elif lst[len(lst)-1] < lst[0] < lst[mid]:
            return lst[0]
        elif lst[len(lst) -1] < lst[mid] < lst[0]:
            return lst[mid]
        else:
            return lst[len(lst)-1]

def quickSort(lst):
    """
    quickSort: List(lst) -> List(result)
        Where the return 'result' is a totally ordered 'lst'.
        It uses the median-of-3 to select the pivot

    e.g.  quickSort([1,8,5,3,4]) == [1,3,4,5,8]
    """
    if lst == []:
        return []
    else:
        pivot = medianOf3(lst)
        (less, same, more) = partition(pivot,lst)
        return quickSort(less) + same + quickSort(more)

def partition(pivot,lst):
    """
    used to get the three partions for the quick sort, less same and more.

    :param pivot: the value to pivot about
    :param lst: the main list to be looked through

    :return: (less, same, more) three list objects with corresponding values.
    """
    (less, same, more) = ([], [], [])

    for elm in lst:
        if elm < pivot:
            less.append(elm)
        elif elm > pivot:
            more.append(elm)
        else:
            same.append(elm)
    return (less,same,more)

if __name__ == "__main__":
    testSorts.run('qsPivotMedian3')
