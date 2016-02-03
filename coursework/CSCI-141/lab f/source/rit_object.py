"""
$Id: rit_object.py,v 1.3 2014/10/03 16:22:41 jeh Exp $

An alternative to the namedtuple construct in the Python collections module.
This module creates classes with a fixed set of slots

For historical reasons, this library is known as the "quick class" library.
There are however two ways to build a class in this framework:
1. Inherit the rit_object class defined here.
2. Create a class by calling the quickClass function.

The only differences between using a quick class and a normal class
definition are as follows.

1. The __slots__ class variable is always defined. If the programmer does
   not do so, there will be an empty slots list.
2. A default constructor is provided that takes positional or keyword
   arguments to initialize the slots declared.
3. The types of the class's slots (attributes) can optionally be defined
   (via the _types class variable in a class declaration or additional
   arguments to the quickClass function) and checked at run time.

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

def _modifyTypeList( types, classType ):
    """ (library internal function)
        Convert a mixed list of type names and real, abstract classes.
        to all real, abstract classes.

        types: A list of types, with the exception that an element
               of the list may be a string if that string is the name
               of the classType parameter
        classType: The main type. The idea is that the main type has
                   just been created, and some of its slots are to be of
                   that type, e.g. for linked structures like graphs.
        
        The type list is fixed so that the string references to classType
        are replaced by a single abstract type. That abstract type has
        two concrete descendants: classType and NoneType.

        Precondition: Each element of the types list must be a type
                      or the string name of classType.

        Implementation Note: The precondition is necessary because currently
                             this package does not allow typed slots to
                             be assigned None. An exception is made when
                             the programmer creates an abstract class to
                             group together several concrete classes. That
                             same trick is used here to allow None to be
                             assigned to a self-referencing type. An abstract
                             type is created by appending a '+' to the
                             original type's name. (See description above.)
                             Since there is no guarantee that other quick
                             classes have had this done to them, the
                             precondition above is checked.
    """
    abstractType = None
    for i in range( len( types ) ):
        t = types[ i ]
        if isinstance( t, str ):
            if t != classType.__name__:
                raise TypeError( "The type string name given was '" + \
                                 className + "'. Only '" + \
                                 classType.__name__ + "' is allowed here." )
            if not abstractType:
                # Create a new abstract class with a name that is
                # impossible to specify in a normal class declaration.
                abstractType = makeAbstractClass( t + '+' )
                abstractType.addClasses( classType, type( None ) )
            types[ i ] = abstractType
        elif not isclass( t ):
            raise TypeError( str( t ) + " is not a type." )

class rit_object( object ):
    """ The base class for all classes created using this framework.
        Note that the methods contained herein apply to classes inheriting
        rit_object; it is not expected that classes declared as inheriting
        rit_object would define their own methods, much less redefine
        these.
        That being said, since rit_object's subclasses will not explicitly
        contain their own constructors, programmers of those subclasses must
        be familiar with the API for the constructor defined here.
    """

    # Initially the new class's slots may have some of its types
    # specified as strings. These need to be converted to real types. (See
    # _modifyTypeList.) The class-level boolean variable _typesScanned
    # indicates whether this class's type list has been scanned yet
    # for str's. It's done in the constructor.
    _typesScanned = False

    # NOTE: In Python, each class defines its own __slots__ variable,
    # so the declaration below has no bearing on subclasses.
    __slots__ = ()

    def __init__( self, *args, **kwargs ):
        """ Initialize a new instance of a quickClass class. The
            constructor call argument list should contain a value for
            each attribute of the class, presented either in the same
            order as the __slots__ declaration, or with keyword names
            that match the slot names. These two approaches may not
            be mixed.
            args: a sequence of values for each slot declared in the subclass
            kwargs: a dictionary of values for each slot declared in
                    the subclass. The keys in the dictionary match the
                    names of the slots.
        """
        # Save the id and name of the subclass being instantiated.
        thisClass = self.__class__
        className = thisClass.__name__

        if not thisClass._typesScanned:
            # If no __slots__ declared (incredibly unlikely),
            # create an empty declaration.
            #
            if "__slots__" not in dir( thisClass ):
                thisClass.__slots__ = ()

            # __slots__ will be a string if only one slot name was
            # given and the '(T,)' approach was not used.
            # Make a tuple out of it.
            #
            if isinstance( thisClass.__slots__, str ): # <-- single slot
                thisClass.__slots__ = ( thisClass.__slots__, )

            slots = thisClass.__slots__

            # If there are no types specified, create an effective
            # no-type-checking situation by stating that all slot types
            # "must" be objects.
            #
            if "_types" not in dir( thisClass ):
                thisClass._types = len( slots ) * ( object, )
            else:
                try:
                    # Some types may have to be modified, so make it a list.
                    #
                    types = list( iter( thisClass._types ) )
                except TypeError: # <-- if only one type given
                    types = [ thisClass._types ]

                if len( slots ) != len( types ):
                    raise TypeError( "No. of slots differs from no. of types" )

                # Fix any type specified as a string and check for non-types.
                #
                _modifyTypeList( types, thisClass )

                # The types are new finalized. Freeze the list.
                #
                thisClass._types = tuple( types )

            # The above code is only exectuted the first time an object is
            # created from the new class.
            thisClass._typesScanned = True

        # Make a copy of the slots' names so that it is easy to check if
        # each slot is given a value exactly once.
        #
        slots = list( thisClass.__slots__ )
        # slots = list( thisClass.__dict__[ "__slots__" ] )
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
                    raise TypeError( "Constructor call for " + className +\
                                     "did not get initialization values " +\
                                     "for " + str( slots ) )
        else:
            if len( args ) != len( slots ):
                raise TypeError( "Constructor call for " + className +\
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
            using its class's name followed by a listing the values of
            all of its slots.
            Precondition: the object must not contain circular references.
                If it does, this method must be redefined in the subclass.
        """
        thisClass = self.__class__
        className = thisClass.__name__
        slots = tuple( thisClass.__slots__ )
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
        slots = tuple( thisClass.__slots__ )
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
        slots = tuple( thisClass.__slots__ )
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


def quickClass( name, *slotDecls ):
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

    # Since classes declared explitly don't have the opportunity to
    # set up the slots and types this early, let the ones created
    # here work the same way. Besides, if the steps below do not
    # happen until rit_object.__init__, we might some day be able to
    # TODO accommodate more types as string names (mutually recursive).
    #
    # _modifyTypeList( types, result )
    # result._types = tuple( types )
    # result._typesScanned = True

    # Make sure types are legal.
    # for i in range( len( types ) ):
    #     t = types[ i ]
    #     if isinstance( t, str ) and isinstance( types, list ):
    #         # Name of class, not class itself, and type list is mutable
    #         if t == name:
    #             nullable = makeAbstractClass( name + '+' )
    #             nullable.addClasses( result, type( None ) )
    #             types[ i ] = nullable # for self-referencing types
    #         else:
    #             raise TypeError( "The type string name given was '" + t + \
    #                              "'. Only '" + name + "' is allowed." )
    #     elif not isclass( t ):
    #         raise TypeError( str( t ) + " is not a type." )
    # result._types = tuple( types )
    return result

def makeAbstractClass( className ):
    """ Create and return an abstract class.
        This is used for the run-time type checking that rit_object provides.

        For more details on abstract base classes, see ABCMeta in package abc.

        When this function returns, the created abstract class
        has as yet no 'concrete' classes that conform to it.
        Here is an example of how you use it:
            Master = makeAbstractClass( "Master" )
            ... Create classes C1, C2, and C3 using rit_object or quickClass.
            ... On the other hand, any of them could be regular types, too.
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