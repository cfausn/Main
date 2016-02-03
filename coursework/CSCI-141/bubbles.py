"""
    bubbles.py
    Colin Fausnaught
    9/12/14, revised 9/14/14

    Draws a group of bubbles within a box, both using recursion and iteration.
"""
from turtle import *
import random

def BOUNDING_BOX(draw):
    """
         BOUNDING_BOX works in two different ways. If the draw variable is passed True, then
         the function will set the pen speed, hide the turtle, and draw the bounding box. If
         False is passed to the function, then the function will simply return 200, the absolute
         value of the box's x or y value.

         Pre-Conditions (if draw == True):  The turtle window is empty
                                            The turtle is pen down
                                            No bubbles are drawn
                                            The user has been prompted for numBub in the main()

         Post-Conditions (if draw == True): The bounding box has been drawn
                                            The pen is down
                                            Turtle is at the starting position (0,0)
                                            Turtle is facing east
                                            
         Pre-Conditions (if draw == False):  The program requires the absolute value of the box's
                                                x or y value.

         Post-Conditions (if draw == False): BOUNDING_BOX() has returned 200

         If there is a problem with me using a constant function to draw, please let me know! I
         didn't think it'd be a huge issue because it doesn't return anything if draw == True, but if
         I should refrain from doing this in the future please tell me! Thanks.
    """
    if draw == True:
        speed(9)
        hideturtle()
        up()
        fd(200)
        lt(90)
        down()
        fd(200)
        lt(90)
        fd(400)
        lt(90)
        fd(400)
        lt(90)
        fd(400)
        lt(90)
        fd(200)
        rt(90)
        up()
        bk(200)
        down()
    else:
        return 200

def MAX_DISTANCE():
    """
         The MAX_DISTANCE() constant is the maximum distance the turtle may travel
         between each bubble.
    """
    return 20

def MAX_RADIUS():
    """
         The MAX_RADIUS() constant is the maximum radius the turtle may draw the
         circles with.
    """
    return 20

def MAX_ANGLE():
    """
         The MAX_ANGLE() constant is the maximum angle the turtle may turn
         between each bubble before going forward.
    """
    return 30

    
def MAX_BUBBLES():
    """
         The MAX_BUBBLES() constant is the maximum bubbles allowed entered from the
         user.
    """
    return 500

def drawRec(numBub):
    """
         drawRec() will draw the bubbles using recursion. It uses the variables angle,
         distance, radius, red, green, and blue, each of which are generated randomly
         using random. It also uses the variable numBub, which has been passed to it.
         Each variable that can only be within a certain range uses the correct constants
         in order to stay within those ranges.

         Pre-Conditons: No bubbles are drawn
                        The pen is down
                        The Bounding Box has been drawn
                        The user has entered the number of bubbles

         Post-Conditions: All bubbles have been drawn
                          The pen is down
                          The turtle is facing a randomly generated direction
                          The turtle is in a randomly generated location
                          The sum of the radii has been calculated and returned
    """
    angle = random.randint(-MAX_ANGLE(),MAX_ANGLE())
    distance = random.randint(1,MAX_DISTANCE())
    radius = random.randint(1,MAX_RADIUS())
    red = random.random()
    green = random.random()
    blue = random.random()
    
    up()
    rt(angle)
    fd(distance)
    
    """
                                      ----------NOTE----------
    Because the lab required us to use 200 as the constant in BOUNDING_BOX() (2.1 Constants), the
         bubbles may overlap with the box/go outside of the box slightly. In the Requirements section
         this is stated to be okay. In order to make it a bit cleaner I would have added a bit of padding,
         maybe make the value 180 or 160 to prevent this issue. Just a reminder.
         Please don't take off points ;)
    """
    #check to see if the turtle is out of range
    if (xcor() >= BOUNDING_BOX(False) or xcor() <= -BOUNDING_BOX(False)
    or ycor() >= BOUNDING_BOX(False) or ycor() <= -BOUNDING_BOX(False)):
        bk(distance)
        lt(180)         #Just turns the opposite direction and moves that way instead
        fd(distance)
    
    if numBub == 0:
        return 0
    else:
        down()
        pencolor(red,green,blue)
        color(red,green,blue)
        begin_fill()
        circle(radius)
        end_fill()
        return radius + drawRec(numBub - 1)
        
        

def drawIter(numBub):
    """
         drawIter draws the bubbles using a while loop instead of recursion. It uses the
         same variables as drawRec, with one exception. This function uses radiusACC to
         calculate the total radii of all the bubbles drawn by this function.

         Pre-Conditons: No bubbles are drawn
                        The pen is down
                        The Bounding Box has been drawn
                        The user has entered the number of bubbles

         Post-Conditions: All bubbles have been drawn
                          The pen is down
                          The turtle is facing a randomly generated direction
                          The turtle is in a randomly generated location
                          The sum of the radii has been calculated and returned
    """
    radiusACC = 0
    
    while numBub != 0:
        angle = random.randint(-MAX_ANGLE(),MAX_ANGLE())
        distance = random.randint(1,MAX_DISTANCE())
        radius = random.randint(1,MAX_RADIUS())
        red = random.random()
        green = random.random()
        blue = random.random()
        
        up()
        rt(angle)
        fd(distance)
        if (xcor() >= BOUNDING_BOX(False) or xcor() <= -BOUNDING_BOX(False)
        or ycor() >= BOUNDING_BOX(False) or ycor() <= -BOUNDING_BOX(False)):
            bk(distance)
            lt(180)
            fd(distance)
        down()
        pencolor(red,green,blue)
        color(red,green,blue)
        begin_fill()
        circle(radius)
        end_fill()
        numBub -= 1
        radiusACC += radius
        
    return radiusACC
        

def main():
    """
         The main function ties everything together! It will error-check the user's input
         to make sure it is between 0 and 500. It will draw the bounding box when needed.
         It will display drawRec's returned value and drawIter's returned value. Then it
         will add them together and display them at the end of the program.
         
    """
    title("bubbles.py")
    numBub = int(input("Bubbles (0-500): "))
    #Error checking, if the user entered an invalid number it will kill the program.
    if numBub > MAX_BUBBLES() or numBub < 0:
        print("Bubbles must be between 0 and 500 inclusive.")
        return
    
    BOUNDING_BOX(True)
    drawRecSum = drawRec(numBub)
    
    #I added this just for some aestetic purposes and because it helped with testing.
    print("For the recursive function, the total radius was %d units."%drawRecSum)
    
    input("Press ENTER to continue: ")
    
    reset()
    BOUNDING_BOX(True)
    drawIterSum = drawIter(numBub)

    #Added this for the same reason as above.
    print("For the iterative function, the total radius was %d units."%drawIterSum)
    
    input("Press ENTER to continue: ")
    
    print("The bubbles' total radius is %d units."%(drawRecSum + drawIterSum))
    bye()

    
#call main()
main()
