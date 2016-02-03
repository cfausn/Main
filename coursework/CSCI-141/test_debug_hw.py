"""
test_debug_hw.py homework for csci141.
"""

#######################################################################
## problem 1 of 2.
#######################################################################
# There is a problem with the is_reverse_of function below.
# Assignment 1:
# 1.1. Develop a suite of tests to properly test the function.
# 1.2. Debug this faulty function to locate and correct the problem.

def is_reverse_of( st1, st2 ):
    """
    is_reverse_of : String String -> Boolean
    is_reverse_of tells if one string is the reverse of another.
    preconditions: st1 and st2 are character strings.
    """
    if len( st1 ) != len( st2 ):
        return False
    i = 0
    j = len( st2 )
    while j > 0:
        j -= 1 #have to make this subtract first so index isn't out of range
        if st1[i] != st2[j]:
            return False
        i += 1

    return True

def test_is_reverse_of():
    """
    a suite of pass/fail test cases to validate that is_reverse_of works.
    """
    # Complete this test function.
    print("test_is_reverse_of", end=": ")
    print(is_reverse_of("","") == True, end=" ")
    print(is_reverse_of("ab","ba") == True, end = " ")
    print(is_reverse_of("ab","ab") == False, end = " ") #expect True on print
    print(is_reverse_of("Fred","derF") == True, end = " ")
    print(is_reverse_of("Freddy","derF") == False, end = " ") #expect True on print
    print(".")

# DO NOT CALL YOUR TEST FUNCTIONS HERE. See end of this file for directions.

#######################################################################
## problem 2 of 2.
#######################################################################
# There is a problem with the str_search function below.
# Assignment 2:
# 2.1. Develop a suite of tests to properly test this function.
# 2.2. Debug this faulty function to find and fix the problems.
#      The function is called indirectly by main_search.
#      You can use your test suite and/or main_search for debugging.
#      Initial Hints: search for J, L, or C.
# 2.3. Document your debugging results trying to fix the str_search code.

def str_search( data, target, start, end ):
    """
    str_search : String String NatNum NatNum -> NatNum or NoneType
    Description:
    Search for a target value in a sorted data string.
    The search happens between the start and end indices inclusively.
    This starts searching in the middle. If it finds the target, it is done.
    Otherwise it decides whether to search the first half or the second half.
    preconditions: the data string is in ascending alphanumeric order.
    Parameters:
        data - a string
        target - the target value to find is a single character string e.g. 'Q'
        start - the starting index into the data
        end - the ending index into the data
    Returns:
        index of target in data, if present; otherwise None.
    """
    
    if start == end:
        return None

    mid_index = ( start + end ) // 2
    mid_value = data[mid_index]
    
    # debug statement prints the data.
    #print( "Searching for", target, ":", data[start:mid_index], 
    # "*" + str( mid_value ) + "*", data[mid_index+1:end+1] )
    
    
    if target == mid_value:
        return mid_index
    elif len(data[start:end]) == 2 and (target > data[start] and target < data[end]):
        return None
    elif len(data[start:end]) == 2 and target > data[end]:
        return None
    elif target > mid_value:
        return str_search( data, target, mid_index, end)
    else:
        return str_search( data, target, start, end - 1)

def find_target( data, target ):
    """
    find_target : String String -> NatNum or NoneType
    find_target returns the index of target in data or None if not found.
    Parameters:
        data - a string
        target - the target value to find
    Returns:
        The index of the target element in data, if present, or None.
    """

    return str_search( data, target, 0, len( data ) - 1 )

def makeString():
    """
    makeString : () -> String
    makeString returns a String
    """
    data = ""
    # append characters to make the string
    for num in range( 36, 108, 2 ):
        data += chr( num )
    return data

def main_search():
    """
    main_search : Void -> NoneType
    """

    data = makeString()
    print( "Number of elements: ", len( data ) )

    while True:
        print( "\nData: ", data )
        target = input( "Enter a character to find: " )

        if target == "":
            break
        else:
            index = find_target( data, target )
            print()
            if index != None:
                print( target, "found at index", index )
            else:
                print( target, "not found" )
    # end while

def test_str_search():
    """
    a suite of pass/fail test cases to validate that str_search works.
    """
    # Complete this test function.
    print("test_str_search", end=": ")
    print(find_target(makeString(), 'J') == 19, end=" ")
    print(find_target(makeString(), 'h') == 34, end=" ")
    print(find_target(makeString(), '$') == 0, end=" ")
    print(find_target(makeString(), "L") == 20, end=" ")
    print(find_target(makeString() , "C") == None, end=" ")
    print(find_target(makeString() , "z") == None, end=" ")
    print(find_target(" " , " ") == None, end=" ")
    print(".")

#######################################################################
# 2.3. Document your debugging results trying to fix the str_search code.
# Enter answers to the questions below inside the triple-quoted string.
"""
	Were you able to completely fix str_search?
	     Yes! I had to understand that certain string values were actually greater
	     in value than others, but once I wrapped my head around that I managed to
	     fix str_search.
	     
	If not, explain in detail the cases that still fail.
	     NA
	     
	What tool(s) did you use?
	     I used makeString() to generate the string to be tested. I also used the
	     find_target() function to both call the str_search() function and to set
	     values for start and end. I used main_search() to find the indexes of the
	     characters to search for my test_str_search() function.
	     
	What went well?
	     Once I understood that I could actually segment the strings into 'bite-sized'
	     pieces based on their value (using < to compare), the idea of the program
	     clicked in my head and I was able to figure out how to work the function.
	     It took that "Ah-Ha!" moment after struggling with it for awhile, but once
	     I got it I totally understood how the program was meant to work and fixed it.
	     
	What problems did you have?
	     I had trouble visualizing the testing suite at first, but after referring to
	     the homework worksheet and using the main_search() function I was able to
	     pick some tests that make sense to me. I also had issues with dealing with
	     cases like 'C' or 'z' being searched for. But I managed to figure out how to get
	     it to work by using an elif statements that return None, and as far as I know
	     the program should work now with anything passed to it.
"""
#######################################################################

if __name__ == "__main__":
    #
    # Run the test functions for problem 1 and problem 2.
    #
    test_is_reverse_of()
    test_str_search()
    #
    main_search()

# After finishing the problems, submit this file to the mycourses dropbox.
