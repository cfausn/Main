"""
    tower.py

    Colin Fausnaught

    uses given code to make stacks of items from 1 to N (the user's input). These stacks are then used to solve
    the "tower" puzzle found in tower_animate.py.
"""

from myStack import *
from tower_animate import *

def main():

    """
    uses stacks to solve the "tower" puzzle laid out in the lab. Accepts intergers
    from 1 to N to solve this puzzle.

    :param number: User's interger input
    :param lst: Main list to hold the stacks
    :param stack1: Main stack holding, in decending order, the user's input and n-1
    :param stack2and3: Empty stacks to be added on to later
    :param num: number of moves required to solve puzzle
    """
    number = int(input("Enter number of disks: ")) #User's input
    animate_init(number) #sets up animation window

    
    lst = []
    stack1 = createStack(number,None)
    stack2and3 = createStack(0,None)
    
    lst += [stack1]
    lst += [stack2and3]
    lst += [stack2and3]

    num = move(number, 0, 2, lst)
    print("Moves Required: " +str(num)) 

    input("Press Enter to Quit: ") #exit verification
    animate_finish() #exits


def createStack(number, oldNode):
    """
    Used to quickly create a stack from the user's input.

    :param myStack: the stack to be returned once filled
    :param oldNode: the node of the previous stack. When called it should be given the value None
    :param number: the number that the user entered

    :return: myStack; the finished stack
    :rtype: stack of Node()s
    """
    
    myStack = oldNode
    
    while number != 0:
        myStack = push(oldNode, number)
        oldNode = myStack
        number -= 1

    return myStack
        
    
    
def move(count, frm, to, lst):
    """
    moves the stack both through animation and list manipulation, then returns how many moves
    it was required to solve the puzzle.

    :param count: the number the user entered
    :param frm: where move() is sending the data from (in the list)
    :param to: where move() is sending the data to (in the list)
    :param lst: a running list of all the stacks
    :param otherval: the "other value", the index which isn't accounted for in to and frm.
    :param moves: the total number of moves required to finish the puzzle
    
    :return: moves
    :rtype: int
    
    """
    if count == 0:
        return 0
    
    else:
                    
        otherval = other(frm, to)
       
        moves = move(count -1,frm, otherval, lst)

        #have to put it here to meet recursion specifications. Took me awhile to figure that out!
        lst[to] = push(lst[to],top(lst[frm]))
        lst[frm] = pop(lst[frm])
        animate_move(lst,frm,to)
        
        moves += 1
        moves += move(count -1, otherval, to, lst)
        
        return moves

def other(frm, to):
    """
    takes to ints and, based on the ints passed, will return the third, "missing", int.

    :param frm: an int
    :param to: an int

    :return: 0, 1, or 2 depending on which two values were passed
    :rtype: int
    """
    if frm + to == 1:
        return 2
    elif frm + to == 2:
        return 1
    elif frm + to == 3:
        return 0

main()
