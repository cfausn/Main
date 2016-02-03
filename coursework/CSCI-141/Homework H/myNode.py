"""
File: myNode.py
Purpose: rit_object LECTURE VERSION
Author: Sean Strout <sps@cs.rit.edu>
Contributor: ben k steele <bks@cs.rit.edu>
Language: Python 3
Description:  A representation of a single linked node intended
to be used as the building blocks for a linked list.
"""

from rit_object import *

###########################################################
# NODE CLASS DEFINITIONS
###########################################################

class Node( rit_object ):
    """
    A representation of a linked list node
    slots
        data: an object reference allows any kind of element
        next: either a Node reference or None
    """
    __slots__ = ('data', 'next')
    _types = ( object, "Node" )

def test_node():
    """
    test_node tests the {NoneType, Node} type constructions
    """
    emptynode = None
    node1 = Node('first', emptynode)
    print( node1.data == 'first' and node1.next == None )
    node2 = Node( 'one-two', Node( 'two', emptynode ) )
    print( node2.data == 'one-two' )
    print( isinstance( node2.next, Node ) )
    print( node2.next.data == 'two' )
    print( node2.next.next == None )


if __name__ == "__main__":
    test_node()

