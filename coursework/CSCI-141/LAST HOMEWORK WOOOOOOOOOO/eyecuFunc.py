"""
Program for binary search tree homework.

Author: Aaron Deever
Author: Colin Fausnaught

file: eyecuFunc.py
"""

from rit_object import *
import math

class EyecuBST(rit_object):
    """ this binary search tree will support inserts, height
    of tree from given element, subtree size from a given element,
    imbalance measurement.
    left:  EyecuBST representing the left sub-tree of this node.
    right: EyecuBST representing the right sub-tree of this node.
    parent: EyecuBST representing the parent node of this node.
    All nodes have a parent node, except for root of the tree (uses None).
    value: the data value associated with this node.
    height: the height of the subtree associated with this node.
    The height is defined as the maximum of the height of the
    left and right subtrees, plus 1.  A leaf node has a height of 0.
    An empty tree as represented by None is defined to have a height
    of -1.
    size: the number of nodes contained in this binary tree.
    imbalance: the difference in the height of the
    left and right subtrees.

    """
    __slots__ = ('left', 'right', 'parent',
                 'value', 'height', 'size', 'imbalance')
    _types    = ('EyecuBST', 'EyecuBST', 'EyecuBST',
                 int, int, int, int)

def createEyecuBST(el, parent):
    """ creates a BST containing just this node, and connected
    to the given parent node, which is None if this is the root.
    Returns the tree node.
    """
    return EyecuBST(None, None, parent, el, 0, 1, 0)

def eyecuToString(tr):
    """ takes an EyecuBST tree and generates a string containing
    an inorder processing of the nodes of the tree.  For each
    node, the string contains the following information:
    value, height, size, imbalance.
    Returns the string
    """

    if tr == None:
        return ""
    else:
        thisNodeStr = "Value: " + str(tr.value) + ", Height: " + \
        str(tr.height) + ", Size: " + str(tr.size) + ", Imbalance: " + \
        str(tr.imbalance) + "\n"
        
        return eyecuToString(tr.left) + thisNodeStr + eyecuToString(tr.right)

def insert(tr, el):
    """ function to insert an element into a binary search tree
    following the rules of binary search trees.

    
    
    return: an updated tree
    precondition: assumed all elements unique
    """
    
    if tr == None:
        tr = createEyecuBST(el, tr)
        return tr

    
    if el > tr.value:
        
        if tr.right != None:
            tr.size += 1
            tr.right = insert(tr.right, el)
        else:
            tr.size +=1
            tr.right = createEyecuBST(el, tr)
        
    elif el < tr.value:
        if tr.left != None:
            tr.size += 1
            tr.left = insert(tr.left, el)
        else:
            tr.size +=1
            tr.left = createEyecuBST(el, tr)

    if tr.right == None and tr.left == None:
        pass
    
    elif tr.right != None and tr.left == None:
        if tr.right.height >= tr.height:
            tr.height = tr.right.height + 1

    elif tr.left != None and tr.right == None:
        if tr.left.height >= tr.height:
            tr.height = tr.left.height + 1

    elif tr.right != None and tr.left != None:
        if tr.right.height > tr.left.height:
            tr.height = tr.right.height + 1
        elif tr.right.height < tr.left.height:
            tr.height = tr.left.height + 1
        else:
            tr. height = tr.left.height + 1
            
    tr.imbalance = treeImbalance(tr)
   
    
        
    return tr
        
def treeHeight(tr):
    """ 
    Returns the height of the tree rooted at this node. Returns -1
    if input tr is an empty tree (None).
    """
    
    if tr == None:
        return -1
    else:
        return tr.height

def treeSize(tr):
    """ 
    Returns the size of the tree rooted at target node. Returns 0
    is input tr is an empty tree (None)
    """
    if tr == None:
        return 0

    return tr.size

def treeImbalance(tr):
    """ 
    Returns the imbalance of the tree rooted at target node. Returns 0
    is input tr is an empty tree (None)
    """
    if tr == None:
        return 0
    elif tr.left == None and tr.right == None:
        return 0
    elif tr.left == None and tr.right != None:
        return tr.right.imbalance + 1
    elif tr.left != None and tr.right == None:
        return tr.left.imbalance + 1
    elif tr.left != None and tr.right != None:
        return int(math.fabs(tr.left.height - tr.right.height))
    

def findNode(tr, val):
    """ finds the target node in the tree.  Returns the node reference.
    Returns None if the node is not in the tree.

    precondtion:  val is non-negative integer.
    
    """
    if tr == None:
        return None
    else:
        if tr.value == val:
            return tr
        elif tr.value > val:
            return findNode(tr.left, val)
        elif tr.value < val:
            return findNode(tr.right, val)
    

# YOU MAY ADD ADDITIONAL FUNCTIONS AS NECESSARY



