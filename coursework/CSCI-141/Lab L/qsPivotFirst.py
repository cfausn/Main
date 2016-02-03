"""
file: qsPivotFirst.py
version: python3
author: Arthur Nunes-Harwitt, 
author: Ivona Bezakova
author: Sean Strout
purpose: Implementation of the quick-sort algorithm (not in-place).  The 
    pivot is chosen always to be the first value in lst.
"""

import testSorts    # run (for individual test run)

def quickSort(lst):
   """
   quickSort: List(lst) -> List(result)
        Where the return 'result' is a totally ordered 'lst'.
		It uses the first element in the lst as the pivot, always.
        
   e.g.  quickSort([1,8,5,3]) == [1,3,5,8]
   """
   if len(lst) == 0:
      return list()
   else:
      pivot = lst[0]        # here we select the first element as the pivot
      less, same, more = partition(pivot, lst)
      return quickSort(less) + same + quickSort(more)

def partition( pivot, lst ):
   """
   partition: pivot (element in lst) * List(lst) -> 
        tuple(List(less), List(same, List(more))).  
   Where:
        List(Less) has values less than the pivot
        List(same) has pivot value/s, and
        List(more) has values greater than the pivot
        
   e.g. partition(5, [11,4,7,2,5,9,3]) == [4,2,3], [5], [11,7,9]
   """
   less, same, more = list(), list(), list()
   for val in lst:
      if val < pivot:
         less.append(val)
      elif val > pivot:
         more.append(val)
      else:
         same.append(val)
   return less, same, more

if __name__ == "__main__":
    testSorts.run('qsPivotFirst')
