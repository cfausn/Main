"""
file: heapSort.py
version: python3
author: Sean Strout
author: Colin Fausnaught
purpose: Implementation of the heapsort algorithm, not
    in-place, (lst is unmodified and a new sorted one is returned)
"""

import heapq    # mkHeap (for adding/removing from heap)
import testSorts    # run (for individual test run)

def heapSort(lst):
    """
    heapSort(List(Orderable)) -> List(Ordered)
        performs a heapsort on 'lst' returning a new sorted list
    Postcondition: the argument lst is not modified
    """
    h = []
    for value in lst:
        heapq.heappush(h, value)

    return [heapq.heappop(h) for i in range(len(h))]

if __name__ == "__main__":
    testSorts.run('heapSort')
