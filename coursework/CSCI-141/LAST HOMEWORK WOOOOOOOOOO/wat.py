"""
Demonstrates simple binary search trees. 
Implements and performs string conversion and search only.
file: bst.py
language: python3
author: A. Nunes-Harwitt
author: ben k steele
author: Sean Strout
contributor: Aaron Deever - updated for rit_object.  Using
None to represent an empty tree.
"""

from rit_object import * 

############################################################
# Class definiton
############################################################

class BinaryTree(rit_object):
   """ A non-empty BinaryTree has a left and right sub-tree
   which are both BinaryTrees, along with a slot to hold
   a value.  An empty BinaryTree is represented as None.
   """
   __slots__ = ("left", "value", "right")
   _types    = ('BinaryTree',   object,  'BinaryTree')

############################################################
# Sample trees
############################################################

exampleTree0 = None

exampleTree1 = BinaryTree( None, 1, None )

exampleTree2 = BinaryTree( BinaryTree( None, 1, None ), 3, None )

exampleTree3 = BinaryTree( None, 3, BinaryTree( None, 4, None ) )

# t2 in lecture notes
exampleTree4 = BinaryTree( BinaryTree( None, 1, None ), \
                          3,                                   \
                          BinaryTree( None, 4, None ) )

exampleTree5 = BinaryTree( BinaryTree( None, 6, None ), \
                          7,                                   \
                          BinaryTree( None, 9, None ) )

exampleTree6 = BinaryTree( exampleTree4, 5, exampleTree5 )

############################################################
# String Conversion
############################################################

def bstToString( tr ):
   """ bstToString: BinarySearchTree -> String """
   if tr == None:
       return ''
   else:
       return bstToString( tr.left )  +  \
              ( str( tr.value ) + ' ' ) +  \
              bstToString( tr.right )
   
# Tests
def test_bstToString():
    """
    test_bstToString : Void -> None
    """
    print( 'Testing bstToString' )
    print( bstToString( exampleTree0 ) == '', end=' ' )
    print( bstToString( exampleTree1 ) == '1 ', end=' ' )
    print( bstToString( exampleTree2 ) == '1 3 ', end=' ' )
    print( bstToString( exampleTree3 ) == '3 4 ', end=' ' )
    print( bstToString( exampleTree4 ) == '1 3 4 ', end=' ' )
    print( bstToString( exampleTree6 ) == '1 3 4 5 6 7 9 ' )

############################################################
# Search
############################################################

def bstSearch( tr, value ):
   """ bstSearch: BinarySearchTree * Number -> Boolean """
   if tr == None:
       return False
   else:
       if value == tr.value:
          return True
       elif value < tr.value:
          return bstSearch ( tr.left, value )
       elif value > tr.value:
          return bstSearch ( tr.right, value )
  
# Tests
def test_bstSearch():
    """
    test_bstSearch : Void -> None
    """
    print( 'Testing bstSearch' )
    print( bstSearch( exampleTree0, 3 ) == False, end=' ' )
    print( bstSearch( exampleTree1, 1 ) == True, end=' ' )
    print( bstSearch( exampleTree1, 3 ) == False, end=' ' )
    print( bstSearch( exampleTree2, 1 ) == True, end=' ' )
    print( bstSearch( exampleTree2, 3 ) == True, end=' ' )
    print( bstSearch( exampleTree2, 2 ) == False, end=' ' )
    print( bstSearch( exampleTree2, 4 ) == False, end=' ' )
    print( bstSearch( exampleTree3, 3 ) == True, end=' ' )
    print( bstSearch( exampleTree3, 4 ) == True, end=' ' )
    print( bstSearch( exampleTree3, 1 ) == False, end=' ' )
    print( bstSearch( exampleTree3, 5 ) == False, end=' ' )
    print( bstSearch( exampleTree4, 1 ) == True, end=' ' )
    print( bstSearch( exampleTree4, 3 ) == True, end=' ' )
    print( bstSearch( exampleTree4, 4 ) == True, end=' ' )
    print( bstSearch( exampleTree4, 0 ) == False, end=' ' )
    print( bstSearch( exampleTree4, 2 ) == False, end=' ' )
    print( bstSearch( exampleTree4, 3.5 ) == False, end=' ' )
    print( bstSearch( exampleTree4, 5 ) == False, end=' ' )
    print( bstSearch( exampleTree6, 1 ) == True, end=' ' )
    print( bstSearch( exampleTree6, 3 ) == True, end=' ' )
    print( bstSearch( exampleTree6, 4 ) == True, end=' ' )
    print( bstSearch( exampleTree6, 5 ) == True, end=' ' )
    print( bstSearch( exampleTree6, 6 ) == True, end=' ' )
    print( bstSearch( exampleTree6, 7 ) == True, end=' ' )
    print( bstSearch( exampleTree6, 9 ) == True, end=' ' )
    print( bstSearch( exampleTree6, 0 ) == False, end=' ' )
    print( bstSearch( exampleTree6, 2 ) == False, end=' ' )
    print( bstSearch( exampleTree6, 3.5 ) == False, end=' ' )
    print( bstSearch( exampleTree6, 4.5 ) == False, end=' ' )
    print( bstSearch( exampleTree6, 5.5 ) == False, end=' ' )
    print( bstSearch( exampleTree6, 6.5 ) == False, end=' ' )
    print( bstSearch( exampleTree6, 8 ) == False, end=' ' )
    print( bstSearch( exampleTree6, 10 ) == False )


# run tests

if __name__ == "__main__":
    test_bstToString()
    test_bstSearch()
