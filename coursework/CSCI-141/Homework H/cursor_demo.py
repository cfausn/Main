"""
description:
Demonstration of the cursor mechanism in the myListIter module.
author: ben k steele <bks@cs.rit.edu>
"""

import myListIter as module

def demo_cursor():
    """
    Demonstrate use of cursor to iterate through a linked list.
    """
    lst =  module.createEmptyList()
    for item in ['a', 'b', 'c']:
	    module.append( lst, item )
    print( 'list is', module.toString( lst ) )

    # reset the cursor to the start of the list
    module.reset( lst )
    print( 'iterating through list using the cursor...' )
    while module.hasNext( lst ):
	    print( 'next element is', module.next( lst ) )

demo_cursor()
