"""
141 Tree Lab - Derp the Interpreter

These are the definitions of the node classes that
are used by the interpreter. It is meant to be imported by the main program.

Author: Sean Strout (sps@cs.rit.edu)
"""

from rit_object import *

##############################################################################
# structure definitions for parse tree
##############################################################################

class MultiplyNode(rit_object):
    """Represents a multiply operator, *"""
    
    __slots__ = ('left', 'right')
    _types    = (object, object)
    
class DivideNode(rit_object):
    """Represents an integer divide operator, //"""

    __slots__ = ('left', 'right')
    _types    = (object, object)
    
class AddNode(rit_object):
    """Represents an addition operator, +"""

    __slots__ = ('left', 'right')
    _types    = (object, object)
    
class SubtractNode(rit_object):
    """Represents a subtraction operator, -"""

    __slots__ = ('left', 'right')
    _types    = (object, object)
    
class LiteralNode(rit_object):
    """Represents an operand node"""
    
    __slots__ = ('val')
    _types    = (int)
    
class VariableNode(rit_object):
    """Represents a variable node"""
    
    __slots__ = ('name')
    _types    = (str)
