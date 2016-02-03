"""
EyecuBST tester program.  Two test programs are provided.  One
can be used to confirm that tree insertion is correct and producing
a valid binary search tree.  The second test program tests the entire
set of requirements.

Author:  Aaron Deever

File: eyecuTester.py
"""

from random import shuffle, seed
import time
from eyecuFunc import *

def testInsert():
    """ Test function confirms after each insert that the tree is
    a correctly formed BST and that it has the target number of elements.

    returns None.  Raises ValueError if insert fails.
    """
    num = int(input("Input number of elements to put in BST: "))
    liszt = list(range(num))
    seed(42) # gives us 'randomness', but same randomness every time
    shuffle(liszt)

    tr = None
    for idx in range(num):
        tr = insert(tr, liszt[idx])
        if not confirmBST(tr, idx+1):
            msg = "Error: Not expected BST with " + str(idx+1) + " elements"
            raise ValueError(msg)

    print("Insert worked correctly.")

def confirmBST(tr, num):
    """ Checks that the provided BST is in fact a binary search tree
    with the target number of elements.
    Returns True / False.
    """

    # converts tree into an in-order list
    liszt = buildBSTlist(tr)
    # return False if input tree has wrong number of elements
    if len(liszt) != num:
        return False
    # return False if input tree does not satisfy BST ordering property
    for idx in range(1,len(liszt)):
        if(liszt[idx-1] > liszt[idx]):
            return False
    # otherwise return True for passing these tests    
    return True

def buildBSTlist(tr):
    """ Recursive function similar to bstToString that converts the BST
    into a list.
    Returns list corresponding to ordered values of BST.
    """
    if tr == None:
        return []
    else:
        return buildBSTlist(tr.left) + [tr.value] + buildBSTlist(tr.right)
    
    
def testAll():
    """ Test all requirements. Elements are inserted into the tree.
    After each insertion, height, size and imbalance are measured
    for a provided target node.  The simulation stops when either all
    elements have been inserted, or the height, size or imbalance
    exceeds input limits.  Timing results are given.

    NOTE: target number should be in range 0 to num-1, inclusive.
    However, -1 can be input to choose the target to be whatever
    number ends up being the root of the tree.
    """
    
    num = int(input("Input number of elements to put in BST: "))
    target = int(input("Input specific target number to evaluate: "))
    maxHt = int(input("Input maximum height of target tree to allow: "))
    maxIm = int(input("Input maximum imbalance of target tree to allow: "))
    liszt = list(range(num))
    seed(42) # gives us 'randomness', but same randomness every time
    shuffle(liszt)
    starttime = time.clock()
    
    tr = None
    targetInTreeYet = False
    for el in liszt:
        tr = insert(tr, el)
        # only need to identify target node location once
        if not targetInTreeYet:
            if target == -1:  # target is root of tree
                targetNode = tr
                target = el  # value at root is the target
                targetInTreeYet = True
            elif el == target: # target just put in tree, locate for future use
                targetNode = findNode(tr, target)
                targetInTreeYet = True
        # only bother computing if we know target is in the tree
        if targetInTreeYet:
            h = treeHeight(targetNode)
            s = treeSize(targetNode)
            i = treeImbalance(targetNode)

            if(h > maxHt):
                break
            if(i > maxIm):
                break
            if(s == target):
                break
         
    endtime = time.clock()
    print("Test terminated after", treeSize(tr), "nodes entered into tree.")
    print("Elapsed time: ", endtime-starttime, "seconds")
    print("Target Value:", target)
    if targetInTreeYet:
        print("Height of tree rooted at target:", h)
        print("Size of tree rooted at target:", s)
        print("Imbalance of tree rooted at target:", i)
    else:
        print("Target node never entered in tree!")

# Uncomment one of these lines to test your insert or test entire program    
#testInsert()
testAll()
