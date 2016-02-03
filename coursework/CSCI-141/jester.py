"""
    jester.py
    Colin Fausnaught
    9/7/14

    This program will draw squares and circles based on the lab b "Jester"
    handout. The program uses recursion to accomplish this task.
"""

from turtle import *

def setOrigin():
    """
        setOrigin sets up the window and takes the turtle and moves it to the
        starting point of the program.

        pre-conditions: 
        post-conditions: coordinate system is (-300,-150) to (300,450)
                         turtle is at the correct start position
                         turtle is facing east
                         turtle is pen-down
        
    """
    setup(600,600)
    setworldcoordinates(-300,-150,300,450)
    home()

def drawFigure(depth, size):
    """
        drawFigure is a reticulating function that will be the 'outline'
        or skeleton of the turtle drawing. It decides which order each
        part of the program will be drawn in and will call the function
        to decide which color the pen will be. 

        pre-conditions: turtle is facing east
                        turtle is pen-down
                        turtle is in the starting position

        post-conditions: turtle has drawn the figure based on which
                            depth it was given
                         turtle is facing east
                         turtle is pen-down
                         turtle is in starting position
                         pen-color is whatever the last color chosen was (red or blue)

    """

    
    decidePenColor(depth)   #calls a function which decides the pen color based on depth
    
    if depth < 1:
        if size == 100:         #if the size hasn't been modified by other reticulations, then
                                #draw a circle with the size of 100 to match the example figures
            drawCircle(size)
        else:                   #otherwise divide the size by 2
            drawCircle(size/2)
            
    else:
        drawSquareLeft(size)            #draws the left side of the square
        
        drawFigure(depth - 1, size/2)   #reticulating function
        
        decidePenColor(depth)           #changes pen color
        
        drawSquareTop(size)             #draws the top of the square
        
        drawFigure(depth - 1, size/2)   #reticulating function
        
        decidePenColor(depth)           #changes pen color
        
        drawSquareRight(size)           #draws right side of square
        
def decidePenColor(depth):
    """
        decidePenColor decides which color the pen will be based on whether the depth
            is odd or even. If the depth is even it will be red, and if it is odd it will be
            blue.

        pre-conditions: turtle will be in varying stages of drawing when this function is called
                        first time it's called, pen-color will be black
                        any other time it's called it depends on which color was chosen last
                        turtle is pen-down
                        
        post-conditions: turtle pen-color is changed to red or blue
                         if depth % 2 is 0 (even), pen will be red
                         if depth % 2 is 1 (odd), pen will be blue
    """

    
    if (depth % 2) == 0:
        pencolor("red")
    else:
        pencolor("blue")
    
def drawSquareLeft(size):
    """
        drawSquareLeft does what it sounds like it would do, draws the left side of the
            square(s) based on which size is passed to it.

        pre-conditions: first time it's called nothing is yet drawn
                        turtle is pen-down
                        turtle is the correct pen-color
                        turtle is facing east

        post-conditions: turtle has drawn the left side of the square(s)
                         pen-colors have been selected based on decidePenColor()
                         turtle is pen-down
                         turtle is facing north-east
                         
    """

    
    lt(180)
    fd(size/2)
    rt(90)
    fd(size)
    rt(90)
    lt(45)
        
def drawSquareRight(size):
    """
        drawSquareRight does what it sounds as well, draws the right side of the square based
            on which side is passed to it.

        pre-conditions: first time it's called everything but the right sides of the square(s)
                            has been drawn.
                        turtle is pen-down
                        turtle is the correct pen-color
                        turtle is facing east
                        
        post-conditions: turtle has drawn the right side of the square(s)
                         pen-colors have been selected basde on decidePenColor()
                         turtle is pen-down
                         turtle is facing east
    """
    lt(45)
    rt(90)
    fd(size)
    rt(90)
    fd(size/2)
    rt(180)

def drawSquareTop(size):
    """
        drawSquareTop does what it sounds like it would, draws the top of the square.
            Exciting stuff.

        pre-conditions: first time it's called everything but the top of the square(s)
                            has been drawn.
                        turtle is pen-down
                        turtle is the correct pen-color
                        turtle is facing east
                        
        post-conditions: turtle has drawn the top of the square(s)
                         pen-colors have been selected based on decidePenColor()
                         turtle is pen-down
                         turtle is facing south-east
    """
    
    rt(45)
    fd(size)
    rt(45)

def drawCircle(size):
    """
        drawCircle draws a circle based on the size passed to it

        pre-conditions: if depth is 0, nothing will be drawn yet
                        turtle is pen-down
                        turtle is correct pen-color
                        turtle is facing east
                        
        post-conditions: turtle has drawn the circle
                         pen-colors have been selected based on decidePenColor()
                         turtle is pen-down
                         turtle is facing east
    """
    
    circle(size)

def main():
    """
        main will tie the program together, accept input from the user, and exit the program
            when enter is pressed.
    """
    title("jester.py")
    setOrigin()
    speed(9)
    depth = int(input("Enter a depth: "))
    drawFigure(depth, 100)
    input("Press ENTER to close: ")
    bye()

#call main
main()
