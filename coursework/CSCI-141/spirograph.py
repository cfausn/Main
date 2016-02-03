"""
    spirograph.py
    Colin Fausnaught
    9/11/14

    This program will draw a spirograph based on the equations
    
    x = (R-r)*cos(t) - (r+p)*cos((R-r)/r*t)
    and
    y = (R-r)*sin(t) - (r+p)*sin((R-r)/r*t)
    
"""

from turtle import *
from math import *

def main():
    """
        The main function is the basic outline for the program. It will
            set some constants and ask for a user's input. If the user
            inputs the wrong number the program will close. If the program
            runs successfully it will draw the spirograph and exit when
            finished.

        The constants are

        R = 100
        r = 4

        the user's input has to be between 10-100 or else the program will
            close
            
    """
    p = int(input("Enter a number from 10-100: "))
    R = 100
    r = 4
    
    if p < 10 or p > 100:
        input("Incorrect value for p! Press ENTER to exit")
        return

    draw(p,R,r)
    input("Press ENTER to exit: ")
    bye()

def draw(p,R,r):
    """
        draw will draw the spirograph based on which values are passed from
            the main function. If the programmer wishes to change the constants
            besides R and r they may, but the user has to enter p.

        pre-conditions: Nothing is drawn let
                        The variables p, R, and r are passed
                        turtle is facing east
                        turtle is at origin

        post-conditions: spirograph is drawn
                         pen is facing east
                         turtle is pen-down
                         turtle has drawn the correct colors
        
    """
    
    t = 2*pi        #t variable which is used in the spirograph
    tf = True       #sentinal value for the while loop
    counter = 0     #counter to call the sentinal value (tf)
    colormode(255)  #used to change the colors of the turtle
    red = 1         #color values
    green = 101
    blue = 201
    up()
    pensize(2)
    speed(8)
    
    while tf == True:
        down()

        #Increasing the color values so the color changes 
        red = red + 1
        green = green + 1
        blue = blue + 1

        #colormode only goes up to 255, so we need this or it won't work
        #correctly.
        if blue == 255:
            blue = 1
        if red == 255:
            red = 1
        if green == 255:
            green = 1

        
        if(t == 2*pi): #This is just for the first time the program
                       #runs. This will move it to the starting point
                       #of the actual spirograph
            up()
            goto(xValue(R,r,p,t),(yValue(R,r,p,t)))
            pencolor(red, green, blue)
            down()
            t = t - 0.01
            goto(xValue(R,r,p,t),(yValue(R,r,p,t)))
        else:
            pencolor(red, green, blue)
            t = t - 0.01
            goto(xValue(R,r,p,t),(yValue(R,r,p,t)))
            
        if counter == 627: #I wasn't sure how the sentinal was supposed to
                           #work so I just programmed this based on how
                           #the spirograph looked in the end.
            tf = False
        counter = counter + 1
            

def xValue(R,r,p,t):
    """
        xValue will take the values R, r, p, and t and calculate
        the latest x value used in the draw() function. It will then return
        the value of x as calculated by the given equation.

        pre-conditions: draw() is passing info to xValue()

        post-conditions: x value has been calculated
                         x value has been returned
    """
    x = (R-r)*cos(t) - (r+p)*cos((R-r)/r*t)
    return x

def yValue(R,r,p,t):
    """
        yValue will take the values R, r, p, and t and calculate
        the latest y value used in the draw() function. It will then return
        the value of y as calculated by the given equation.

        pre-conditions: draw() is passing info to yValue()

        post-conditions: y value has been calculated
                         y value has been returned
    """

    y = (R-r)*sin(t) - (r+p)*sin((R-r)/r*t)
    return y

#call main
main()
