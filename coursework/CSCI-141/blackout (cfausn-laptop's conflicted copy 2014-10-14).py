"""
    blackout.py
    Colin Fausnaught
    9/24/14
    
    Takes equations in the form of strings and decides if they are equal
    or what their value is, depending on which function is called
"""

#import antigravity

def compute(s):
    """
         compute() will take a string version of an equation without an '=' sign
         and decide what its value is. It uses the checkNums() function to make sure
         that digits with more than one string index are used correctly.

         Pre-Conditions: Function has called compute()
                         String has been passed

         Post-Conditions: The equation has been solved
                          The value of the equation has been returned
    """
    x = 0
    intOne = 0
    intTwo = 0
    intAcc = 0
    changeString = s
    if s == " " or s == "":
        return None
    
    if (s.find('x') == -1 and s.find('/') == -1 and
        s.find('+') == -1 and s.find('-') == -1 and s.find('=') == -1):
        return None
    
    if (s.find('x') == 0 or s.find('/') == 0 or
        s.find('+') == 0 or s.find('-') == 0) or s.find('=') == 0:
        return None
    
    
    while x < len(s):
        if s[len(s) - 1] == "+":
            return None
        elif s[len(s) - 1] == "x":
            return None
        elif s[len(s) - 1] == "/":
            return None
        elif s[len(s) - 1] == "-":
            return None
        elif s[len(s) - 1] == "=":
            return None
        
        x+=1

    x = 0
    #When are we learning switches? These elifs are giving me a headache!
    
    while x < len(changeString):
        if changeString[x] == "x":
            intOne = checkNums(changeString[:x])
            intTwo = checkNums(changeString[x+1:])
            if intAcc == 0:
                intAcc = intOne * intTwo
            else:
                intAcc = intAcc * intTwo
                
            changeString = changeString[x+1:]
            x = 0
            
        elif changeString[x] == "/":
            intOne = checkNums(changeString[:x])
            intTwo = checkNums(changeString[x+1:])
            
            if intTwo == 0:
                return None
            
            if intAcc == 0:
                intAcc = intOne / intTwo
            else:
                intAcc = intAcc / intTwo
            changeString = changeString[x+1:]
            x = 0

            
        elif changeString[x] == "+":
            intOne = checkNums(changeString[:x])
            intTwo = checkNums(changeString[x+1:])
            if intAcc == 0:
                intAcc = intOne + intTwo
            else:
                intAcc = intAcc + intTwo
            changeString = changeString[x+1:]
            x = 0

            
        elif changeString[x] == "-":
            intOne = checkNums(changeString[:x])
            intTwo = checkNums(changeString[x+1:])
            if intAcc == 0:
                intAcc = intOne - intTwo
            else:
                intAcc = intAcc - intTwo
                
            changeString = changeString[x+1:]
            x = 0


        x+=1

    return intAcc
        
def checkNums(s):
    """
         checkNums() is used to make sure the values passed to it are correctly
         represented in whatever function calls it.
         For example:
              s = '223'

              this function will make sure that the value in s is correctly
              translated to an int value which can be used in functions like
              compute(), so the return value in this case will be 223.

         Pre-Conditions: Program has called checkNums() to get the int value of a string
                         String has been passed

         Post-Conditions: String has been converted to an int
                          Int value (numAcc) has been returned
         
    """
    numAcc = 0
    for c in s:
        if c.isdigit() == False:
            return numAcc
        elif numAcc == 0:
            numAcc = int(c)
        else:
            numAcc = int(str(numAcc) + str(c))
    return numAcc
    
def evaluate(s):
    """
         evaluate() takes an equation, or two expressions, and decides
         if they are equal to each other. If they are it returns True,
         if they aren't it returns False, and if it is invalid it returns
         None.

         Pre-Conditions: Function has called evaluate to check two expression's equality
                         Function has been passed a string equation

         Post-Conditions: Equality has been decided
                          If the expressions were equal, True has been returned
                          If the expressions were not equal, False has been returned
                          if the expression(s) were invalid, None has been returned
    """
    x = 0
    while x < len(s):
        if s[x] == '=':
            left = compute(s[:x])
            right = compute(s[x+1:])

            if left == right and left != None and right != None:
                return True
            elif left == None:
                return None
            elif right == None:
                return None
            else:
                return False
        x += 1
        
    return None
            

def solve(s):
    """
         solve() takes an equation which requires "blacking-out" and decides which
         indexes need to be "blacked-out" in order to make the equation equal. If the
         equation doesn't need to be blacked-out then it returns a "No Blackout Error".
         Otherwise it blacks out squares until the expressions are equal.

         Pre-Conditions: Function has called solve()
                         String has been passed

         Post-Conditions: solve() has blacked out the correct squares, or returned an error/None
                          If valid, the corrected blackout puzzle has been returned
         
    """
    x = 0
    equalIndex = 0
    
    while x < len(s):
        if s[x] == '=':
            equalIndex = x
            break
        x += 1
        

    x = 0
    y = 0

    if evaluate(s) == True:
        return "Error, didn't need to blackout!"

    while x < len(s):
        if x == equalIndex:
            x+=1
            pass
        
        tempString = s[:x] + s[x+1:]
        while y < len(s):
            if y == equalIndex:
                y+=1
                pass
            tempString2 = tempString[:y] + tempString[y+1:]

            if evaluate(tempString2) == True and evaluate(tempString2) != None:
                return tempString2
            y+=1
        y = 0
        x+=1
            

def main():
    """
         The main() is a totaly radical function that tests all of my other functions.

         Feel free to add your own tests.
    """
    print("COMPUTE FUNCTION:")
    print("22-11x4 =", compute("22-11x4"), " (expect 44)")
    print("10+5x5 =", compute("10+5x5"), " (expect 75)")
    print("+11x4 =", compute("+11x4"), " (expect None)")
    print("=22+4 =", compute("=22+4"), " (expect None)")
    print("0 =", compute("0"), " (expect None (not a valid equation))")
    print("' ' =", compute(" "), " (expect None)")
    print("'' =", compute(""), " (expect None)")
    print(" ")
    
    print("EVALUATE FUNCTION:")
    print("22-11x4 ?= 7x5+9", evaluate("22-11x4=7x5+9"), " (expect True)")
    print("2-11x4 ?= 7x5+9", evaluate("2-11x4=7x5+9"), " (expect False)")
    print("+1-11x4 ?= 7x5+9", evaluate("+1-11x4=7x5+9"), " (expect None)")
    print("1-11x4 ?= +7x5+9", evaluate("1-11x4=+7x5+9"), " (expect None)")
    print("22+3x5 ?= 5x5x5", evaluate("22+3x5=5x5x5"), " (expect True)")
    print("1 = 0", evaluate("1=0"), " (expect None (not a valid equation))")
    print("1x0", evaluate("1x0"), " (expect None (not a valid equation))")
    print("' '", evaluate(" "), " (expect None)")
    print("''", evaluate(""), " (expect None)")
    print(" ")
    
    print("SOLVE FUNCTION:")
    print("solving 288/24x6=18x13x8 :", solve("288/24x6=18x13x8"), " (expect 288/4x6=18x3x8)")
    print("solving 22+3x5=55x4+5 :", solve("22+3x5=55x4+5"), " (expect 2+3x5=5x4+5)")
    print("solving 2+3x5=6665x4+5 :", solve("2+3x5=6665x4+5"), " (expect None)")
    print("solving 22-11x4=7x5+9", solve("22-11x4=7x5+9"), " (expect No-Blackout Error)")
    print("solving 0=1", solve("0=1"), " (expect None (not a valid equation))")
    print("solving ' ' :", solve(" "), " (expect None)")
    print("solving '' :", solve(""), " (expect None)")
    print(" ")
    

#call main()
main()
