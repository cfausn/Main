"""
$Id: rit_object.py,v 1.2 2014/09/13 00:13:03 jeh Exp $

An alternative to the namedtuple construct in the Python collections module.
This module creates classes with a fixed set of slots

For historical reasons, this library is known as the "quick class" library.
There are two ways to build a quick class:
1. Inherit the rit_object class defined here.
2. Create a class by calling the QuickClass function.

The only differences between using a quick class and a normal class
definition are as follows.

1. The __slots__ class variable is always defined.
2. A default constructor is provided that takes positional or keyword
   arguments.
3. Optionally, the types of the class's slots (attributes) can be defined
   (via the _types class variable in a class declaration or alternate
   arguments to the QuickClass function) and checked at run time.

The differences between a class created through this package and one created
through collections.namedtuple are as follows.

1. Objects created via this library are not iterable.
2. The attributes in objects created by this library are writable.
"""

# Reasons for doing this:

# Less code to define a class and no need for a maker function means it
# is far less error prone.

# Type checking makes debugging easier since execution halts at the
# source of the problem (the assignment violation) versus later on (when
# accessed/used as an unexpected type).

# Built in "to string" representation (__str__ method) also makes
# debugging easier.

# As with manually declaring classes with a __slots__ class variable,
# objects enforce their predefined slot attributes and those attributes
# are still mutable.

import abc # abstract base class library
from inspect import isclass

def _makeAbstractType( className, classType ):
    """ Create an abstract type for classes that represent the same
        high-level abstration.
    """
    if classType.__name__ != className:
        raise TypeError( "The type string name given was '" + className + \
                         "'. Only '" + classType.__name__ + "' is allowed." )
    nullable = makeAbstractClass( className + '+' )
    nullable.addClasses( classType, type( None ) )
    return nullable

def _modifyTypeList( types, classType ):
    """ Convert a mixed list of type names and real, abstract classes.
        to all real, abstract classes.
    """
    for i in range( len( types ) ):
        t = types[ i ]
        if isinstance( t, str ):
            # Name of class, not class itself, and type list is mutable
            types[ i ] = _makeAbstractType( t, classType )
        elif not isclass( t ):
            raise TypeError( str( t ) + " is not a type." )

class rit_object( object ):
    """ The base class for all quick classes.
        Since rit_object's subclasses will not explicitly contain their
        own constructors, users of those subclasses must be familiar with
        the API for the constructor defined here.
    """

    # This class's type list hasn't yet been scanned for str's.
    _typesScanned = False

    __slots__ = ()

    def __init__( self, *args, **kwargs ):
        """ Initialize a new instance of a QuickClass class.
            It assumes a value for each attribute of the class, presented
            either in order or with keyword names that match the attribute
            names.
            args: a sequence of values for each slot declared in the subclass
            kwargs: a dictionary of values for each slot declared in
                    the subclass. The keys in the dictionary match the
                    names of the slots.
            Only one of the above arguments should be provided, and the one
            that is provided must be complete, i.e., it must contain values
            for every slot declared in the subclass.
        """
        thisClass = self.__class__
        className = thisClass.__name__

        if not thisClass._typesScanned:
            if "__slots__" not in dir( thisClass ):
                thisClass.__slots__ = ()
            if isinstance( thisClass.__slots__, str ): # <-- single slot
                thisClass.__slots__ = [ thisClass.__slots__ ]
            slots = thisClass.__slots__
            if "_types" not in dir( thisClass ):
                thisClass._types = len( slots ) * ( object, )
            else:
                try:
                    types = list( iter( thisClass._types ) )
                except TypeError: # <-- if only one type given
                    types = [ thisClass._types ]
                if len( slots ) != len( types ):
                    raise TypeError( "No. of slots differs from no. of types" )
                _modifyTypeList( types, thisClass )
                thisClass._types = tuple( types )
            thisClass._typesScanned = True

        slots = list( thisClass.__dict__[ "__slots__" ] )
        if len( kwargs ) != 0:
            if len( args ) != 0:
                raise TypeError( "NamedTuples cannot be initialized with " +\
                                 "a combination of regular and " +\
                                 "keyword arguments" )
            else:
                for key in kwargs:
                    if key not in slots:
                        raise AttributeError( "'" + className + "' object " +\
                                              "has no attribute named '" +\
                                              key + "'" )
                    else:
                        attrValue = kwargs[ key ]
                        setattr( self, key, attrValue )
                        slots.remove( key )
                if slots != []:
                    raise TypeError( "Constructor " + className + "() " +\
                                     "did not get initialization values " +\
                                     "for " + str( slots ) )
        else:
            if len( args ) != len( slots ):
                raise TypeError( "Constructor " + className + "() " +\
                                 "expected " + str( len( slots ) ) +\
                                 " arguments but got " + str( len( args ) ) )
            else:
                i = 0
                for key in slots:
                    setattr( self, key, args[ i ] )
                    i += 1

    def __str__( self ):
        """ (DO NOT call this function directly; access it via the str
             global function.)
            Return a string representation of the value of this object
            through its class's name followed by a listing the values of
            all of its slots.
            Precondition: the object must not contain circular references.
                If it does, this method must be defined in the subclass.
        """
        thisClass = self.__class__
        className = thisClass.__name__
        slots = list( thisClass.__dict__[ "__slots__" ] )
        if len( slots ) != 0:
            result = className + "( "
            lastSlot = slots[ -1 ]
            for slot in slots:
                result += slot + ': ' + str( getattr( self, slot ) )
                if slot != lastSlot:
                    result += ", "
            result += " )"
        else:
            result = className + "()"
        return result

    def __repr__( self ):
        """ (DO NOT call this function directly; access it via the repr
             global function.)
            Return a string that, if evaluated, would re-create this object.
            Precondition: The object must not contain circular references!!
                If it does, this method must be defined in the subclass.
        """
        thisClass = self.__class__
        className = thisClass.__name__
        slots = list( thisClass.__dict__[ "__slots__" ] )
        if len( slots ) != 0:
            result = className + "( "
            lastSlot = slots[ -1 ]
            for slot in slots:
                result += slot + '=' + repr( getattr( self, slot ) )
                if slot != lastSlot:
                    result += ", "
            result += " )"
        else:
            result = className + "()"
        return result

    def __setattr__( self, name, value ):
        """ This is a private function. Do NOT directly call it.
            It checks attribute (slot) references for type validity.
        """
        thisClass = self.__class__
        slots = list( thisClass.__dict__[ "__slots__" ] )
        if name not in slots:
            raise AttributeError( repr( thisClass.__name__ ) + \
                         " object has no attribute " + repr( name ) )
        slotIndex = slots.index( name )
        paramType = thisClass._types[ slotIndex ]
        if isinstance( value, paramType ):
            object.__setattr__( self, name, value )
        else:
            raise TypeError( "Type of " + name + \
                             " should be " + paramType.__name__ + \
                             ", not " + type( value ) .__name__ )


def QuickClass( name, *slotDecls ):
    """ Return a new class that has the provided name and slots (attributes).
    
        (This is an alternative to the explicit class declaration using the
         base class rit_object.)

        slotDecls: a sequence of slot declarations
        Each slot declaration provided is a 2-tuple, with the slot's type
        first and the slot's name second.
        The one exception is that, instead of a type one may use the string
        name of the class being built. This is the way one refers to the
        type one is building for structurally recursive types.

        Note that mutually recursive types are not (yet) supported.

        The class returned can be constructed using the provided name and
        either positional or keyword arguments. See the __init__ method
        for QuickBaseClass.
    """
    types = [ s[ 0 ] for s in slotDecls ]
    slots = tuple( s[ 1 ] for s in slotDecls )
    result = type( name, ( rit_object, ), \
                   { '__slots__': slots, '_types': types } )

    # TODO If the operation below were delayed, until rit_object.__init__,
    # we might be able to accommodate more types as names.
    #
    _modifyTypeList( types, result )
    result._types = tuple( types )
    result._typesScanned = True

    # Make sure types are legal.
    for i in range( len( types ) ):
        t = types[ i ]
        if isinstance( t, str ) and isinstance( types, list ):
            # Name of class, not class itself, and type list is mutable
            if t == name:
                nullable = makeAbstractClass( name + '+' )
                nullable.addClasses( result, type( None ) )
                types[ i ] = nullable # for self-referencing types
            else:
                raise TypeError( "The type string name given was '" + t + \
                                 "'. Only '" + name + "' is allowed." )
        elif not isclass( t ):
            raise TypeError( str( t ) + " is not a type." )
    result._types = tuple( types )
    return result

def makeAbstractClass( className ):
    """ Create and return an abstract class.
        This is used for the run-time type checking that rit_object provides.

        For more details on abstract base classes, see ABCMeta in package abc.

        When this function returns, the created abstract class
        has as yet no 'concrete' classes that conform to it.
        Here is an example of how you use it:
            Master = makeAbstractClass( "Master" )
            ... Create classes C1, C2, and C3 using rit_object or QuickClass.
            Master.addClasses( C1, C2, C3 )
            C1, C2, and C3 are now subclasses of Master.
    """
    class AbstractClass( metaclass=abc.ABCMeta ):
        @classmethod
        def addClasses( self, *classes ):
            """ Establish the classes provided as arguments to this
                function as 'concrete' classes that conform to this
                abstract class.
            """
            for cls in classes:
                self.register( cls )
    AbstractClass.__name__ = className
    return AbstractClass

