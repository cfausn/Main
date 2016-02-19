
#played with Golbach's weak conjecture, got a program that can run and
#returns 3 prime numbers from any given odd number.

def isprime(n):

    
    for m in range(2, int(n**0.5)+1):
        if not n%m:
            return False
    return True 


def main(p, theDict):
    time = 0
    pS = str(p)
    s = 0
    n = 0
    
    for num in pS:
        s+= int(num)
        
    
                

    #print("processing...")
    while True:
        
        if (s + n) % 2 == 0 and (s + n) != 2:
            pass
        elif ( p == (s + n) + ((p - s) - n)):
            if isprime(s + n) and ((p-s) - n) % 2 == 0 and isprime(((p-s) - n)/2):
                s = str(pS + " = " + str(s + n) + " + " + str(int(((p-s) - n)/2)) + " + " + str(int(((p-s) - n)/2)))
            
                if not (n in theDict.keys()):
                    theDict[n] = [s]
                else:
                    theDict[n].append(s)
                break
            
        elif( s - n ) >= 2:    
            if ( p == (s - n) + ((p - s) + n)):
                if isprime(s - n ) and ((p-s) + n) % 2 == 0 and isprime(((p-s) + n)/2):
                    s = str(pS + " = " + str(s - n) + " + " + str(int((p-s) + n)/2) + " + " + str(int(((p-s) + n)/2)))
                    
                    if not theDict[n]:
                        theDict[n] = [s]
                    else:
                        theDict[n].append(s)
                                    
                    break
        n+=1




            


theDict = dict()

print("A working model for Golbach's weak conjecture. Returns 3 prime numbers \nwhich add up to any odd number given")
main(int(input("Enter an odd number greater than or equal to 11: ")),theDict)
  


print("")
print("")
print("")

print("------------------------ DICT CONTENTS: ----------------------------")


for key in theDict.keys():
    print("KEY : " + str(key))
    for s in theDict.get(key):
        print(s)
    print("")
    print("")

input('Press enter to quit')
