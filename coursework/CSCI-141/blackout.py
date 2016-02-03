"""
    blackout.py
"""

def compute(s):

    x = 0
    intOne = 0
    intTwo = 0
    intAcc = 0
    changeString = s

    if (s.find('x') == 0 or s.find('/') == 0 or
        s.find('+') == 0 or s.find('-') == 0):
        return None
    
    
    while x < len(s):
        
        print("ran while")
        if s[x] == "+" and (s[x-1] == "" or s[x+1] == ""):
            return None
        elif s[x] == "x" and (s[x-1] == "" or s[x+1] == ""):
            return None
        elif s[x] == "/" and (s[x-1] == "" or s[x+1] == ""):
            return None
        elif s[x] == "-" and (s[x-1] == "" or s[x+1] == ""):
            return None
        x+=1

    x = 0

    while x < len(s):
        if changeString[x] == "x":
            intOne = int(changeString[x-1])
            intTwo = int(changeString[x+1])
            if intAcc == 0:
                intAcc = intOne * intTwo
            else:
                intAcc = intAcc * intTwo
                
            changeString = str(intAcc) + changeString[:x]
            
        elif changeString[x] == "/":
            intOne = int(changeString[x-1])
            intTwo = int(changeString[x+1])
            
            if intAcc == 0:
                intAcc = intOne / intTwo
            else:
                intAcc = intAcc / intTwo
            changeString = str(intAcc) + changeString[:x]
            
        elif changeString[x] == "+":
            intOne = int(changeString[x-1])
            intTwo = int(changeString[x+1])
            if intAcc == 0:
                intAcc = intOne + intTwo
            else:
                intAcc = intAcc + intTwo
            changeString = str(intAcc) + changeString[:x]
            
        elif changeString[x] == "-":
            intOne = checkNums(changeString[:x])
            intTwo = checkNums(changeString[x+1:])
            if intAcc == 0:
                intAcc = intOne - intTwo
            else:
                intAcc = intAcc - intTwo
                
            changeString = str(intAcc) + changeString[x:]

        x+=1

    return changeString
        
def checkNums(s):
    numAcc = 0
    for c in s:
        if c.isdigit() == False:
            return numAcc
        elif numAcc == 0:
            numAcc = c
        else:
            numAcc = int(str(numAcc) + str(c))
    return numAcc
    
def evaluate():
    pass

def solve():
    pass

def main():
    print("22-11x4 =", compute("22-11x4"), " expect 44")

#call main()
main()
