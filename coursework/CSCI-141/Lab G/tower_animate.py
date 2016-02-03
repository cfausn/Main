"""
This program animates the Tower of Hanoi puzzle.  It has an animate_init()
function to create the initial setup based on the number of disks
input.  Then it has a animate_move() function, which takes the list of
stacks and integers indicating the from and to stacks, and adjusts
the animation accordingly.

NOTE:  students need to follow the interface for these functions,
that is provide the expected inputs to the functions, 
but do not need to change anything in the functions.  

Author:  Aaron Deever

file:  tower_animate.py
"""

from turtle import *
from myStack import *

def drawRec(width):
    for i in range(2):
        fd(width)
        lt(90)
        fd(1)
        lt(90)
        
def animate_init(disks):
    """
    This function initializes the canvas for the Tower of Hanoi animation.
    input:  disks:  number of disks in the initial tower.
    """
    
    setup(900,450)
    scale_factor = disks + 2 # make top disk have width 3
    setworldcoordinates(-2,-1,4*scale_factor+2,2*scale_factor+1)
    speed(0)
    hideturtle()

    # draw the bases of the piles
    up()
    fd(scale_factor / 6)
    lt(90)
    fd(scale_factor / 2)
    rt(90)
    down()
    for i in range(2):
        fd(scale_factor)
        up()
        fd(scale_factor / 3)
        down()
    fd(scale_factor)
    up()
    fd(-scale_factor * 11/3)
    down()

    # draw the Tower
    for i in range(scale_factor, 2, -1):
        drawRec(i)
        lt(90)
        fd(1)
        rt(90)
        fd(.5)

    # return to home + offset equal to disks, pen up, facing east for each move
    # offset is used so animate_move() calls can deduce worldcoordinates
    # without having to be passed the disks argument
    up()
    home()
    fd(disks)

def animate_move(stackList, fromPile, toPile):
    """
    Precondition - move is legal.
    Precondition:  THIS FUNCTION ASSUMES THAT THE STACKS HAVE ALREADY
    BEEN ADJUSTED ACCORDING TO THE MOVE THAT
    IT IS ABOUT TO ANIMATE.  IT DOES NOT ADJUST THE STACKS!!!
    THIS FUNCTION SHOULD BE CALLED
    IMMEDIATELY AFTER THE MOVE IS PERFORMED. 

    Precondition - the turtle is offset horizontally from home by
    disks units.  This allows us to know the worldcoordinates without
    having to pass disks as an argument.  Turtle is up, facing east.
    
    This function identifies the size of the disk that was
    at the top of the fromPile, and erases it, and moves it to the toPile.

    Postcondition = turtle is placed in original state
    """

    # deduce disks from the width of the window
    disks,y = position()
    fd(-disks) # back to 0,0

    scale_factor = disks + 2

    # erase from fromPile
    fd(scale_factor / 6)
    fd(scale_factor*4/3 * fromPile)
    lt(90)
    fd(scale_factor/2)
    rt(90)
    
    fromPileSize = size(stackList[fromPile])
    diskSize = top(stackList[toPile])
    fd((disks-diskSize) * .5)
    lt(90)
    fd(fromPileSize)
    down()
    color("white")
    pensize(1)  # looks like same pen size erases effectively
    fd(1)
    rt(90)
    fd(diskSize+2)
    rt(90)
    fd(1)
    pensize(1)
    up()
    color("black")
    lt(90) # face east
    home()
    
    # add it to toPile
    fd(scale_factor / 6)
    fd(scale_factor*4/3 * toPile)
    lt(90)
    fd(scale_factor/2)
    rt(90)

    toPileSize = size(stackList[toPile])-1
    fd((disks-diskSize) * .5)
    lt(90)
    fd(toPileSize)
    down()
    fd(1)
    rt(90)
    fd(diskSize+2)
    rt(90)
    fd(1)
    up()
    lt(90) # face east
    home()
    # move forward levels
    fd(disks)
    

def animate_finish():
    bye()
    
    
