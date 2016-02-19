"""
    FizzBuzz.py
    Colin Fausnaught
    1/28/15
    
    Runs a program that goes through numbers 1-100 and prints either the number
    or a string based on the given requirments. 
"""

    
def fizzBuzz():
    """
        Prints either 'Fizz', 'Buzz', 'FizzBuzz', or the number depending
        on the given requirements.
    """
    for num in range(1,101):
        if (num % 5) == 0 and (num % 7) == 0:
            print("FizzBuzz")
        elif (num % 5) == 0:
            print("Fizz")
        elif (num % 7) == 0:
            print("Buzz")
        else:
            print(num)

def main():
    """
        Runs the fizzBuzz() function, which prints 'Fizz', 'Buzz', 'FizzBuzz',
        or an interger.
    """
    fizzBuzz()
    
main()

