"""
    computer_science.py
    Colin Fausnaught
    CSCI - 141
    8/29/14
"""

from turtle import *		#Used to draw with turtle
import math			#Used for the sqrt function in this program

def main():
    """
        This program uses turtle to draw the words "COMPUTER SCIENCE"
        graphically. The program exits when the user presses the ENTER
        key.
    """
    global x
    x = 50
    setup(width=1800, height=100, startx=0, starty=0)
    setworldcoordinates(-500,-50,500,50)
    speed(0)
    draw()
    input("Press ENTER to close")
    bye()
    
def draw():
    """	
	the draw() function both sents the initial position of the turtle, and calls all the
	other functions that will make "COMPUTER SCIENCE" in sequence. 

	NOTE: To add flair, delete the # before draw_Flair()
    """
    title("computer_science.py")
    up()
    setpos(-475,25)
    draw_C()
    draw_O()
    draw_M()
    draw_P()
    draw_U()
    draw_T()
    draw_E()
    draw_R()
    draw_Space()
    draw_S()
    draw_C()
    draw_I()
    draw_E()
    draw_N()
    draw_C()
    draw_E()
    #draw_Flair()
    
def drawLine(x):
    """
	drawLine draws a straight line in turtle based on what the programmer passes
	to the function. The default for this program is 50, which is stored in the global
	variable x.
    """
    forward(x)


def space():
    """
	space() will move the turtle at the end of each letter to the starting point
	of the next letter. Each function is required to move turtle to the bottom
	right of the 50 units allocated to that letter. 

	For example, take the letter T:

			|_______________|
			|	|	|
			|	|	|
			|	|	|
			|	|	| <- this is where the turtle needs to be.
						It also needs to be facing EAST!
    """
    up()
    drawLine(10)
    left(90)
    drawLine(x)
    right(90)
    down()
    
def draw_C():
    """
	draw_C() will draw the letter C in the turtle area. This function may be reused
	wherever the programmer would like a C.
    """
    down()
    drawLine(x)
    up()
    backward(x)
    down()
    right(90)
    drawLine(x)
    left(90)
    drawLine(x)
    space()

def draw_O():
    """
	draw_O() will draw the letter O in the turtle area. This function may be reused
	wherever the programmer would like a O.
    """
    drawLine(x)
    right(90)
    drawLine(x)
    right(90)
    drawLine(x)
    right(90)
    drawLine(x)
    up()
    backward(x)
    right(90)
    drawLine(x)
    space()

def draw_M():
    """
	draw_M() will draw the letter M in the turtle area. This function may be reused
	wherever the programmer would like a M.
    """
    right(90)
    drawLine(x)
    up()
    backward(x)
    down()
    left(26.5651)
    drawLine(math.sqrt(3125))
    left(2 * 63.4349)
    drawLine(math.sqrt(3125))
    right((90-26.5651) + 90)
    drawLine(x)
    left(90)
    space()
    
def draw_P():
    """
	draw_P() will draw the letter P in the turtle area. This function may be reused
	wherever the programmer would like a P.
    """
    drawLine(x)
    right(90)
    drawLine(20)
    right(90)
    drawLine(x)
    left(90)
    backward(20)
    drawLine(x)
    up()
    left(90)
    drawLine(x)
    space()
    
def draw_U():
    """
	draw_U() will draw the letter U in the turtle area. This function may be reused
	wherever the programmer would like a U.
    """
    right(90)
    drawLine(x)
    left(90)
    drawLine(x)
    left(90)
    drawLine(x)
    up()
    backward(x)
    right(90)
    space()

def draw_T():
    """
	draw_T() will draw the letter T in the turtle area. This function may be reused
	wherever the programmer would like a T.
    """
    drawLine(x)
    up()
    backward(25)
    right(90)
    down()
    drawLine(x)
    left(90)
    up()
    drawLine(25)
    space()

def draw_E():
    """
	draw_E() will draw the letter E in the turtle area. This function may be reused
	wherever the programmer would like a E.
    """
    drawLine(x)
    up()
    backward(x)
    right(90)
    down()
    drawLine(25)
    left(90)
    drawLine(30)
    up()
    backward(30)
    down()
    right(90)
    drawLine(25)
    left(90)
    drawLine(x)
    space()

def draw_R():
    """
	draw_R() will draw the letter R in the turtle area. This function may be reused
	wherever the programmer would like a R.
    """
    drawLine(x)
    right(90)
    drawLine(20)
    right(90)
    drawLine(x)
    left(90)
    backward(20)
    drawLine(x)
    backward(30)
    left(59.0362)
    drawLine(math.sqrt(3400))
    left(30.9638)
    space()
    

def draw_Space():
    """
	draw_Space() will create a space to seperate the words "COMPUTER" and "SCIENCE".
    """
    up()
    drawLine(30)
    down()

def draw_S():
    """
	draw_S() will draw the letter S in the turtle area. This function may be reused
	wherever the programmer would like a S.
    """
    drawLine(x)
    backward(x)
    right(90)
    drawLine(25)
    left(90)
    drawLine(x)
    right(90)
    drawLine(25)
    left(90)
    backward(x)
    drawLine(x)
    space()

def draw_I():
    """
	draw_I() will draw the letter I in the turtle area. This function may be reused
	wherever the programmer would like a I.
    """
    drawLine(x)
    backward(25)
    right(90)
    drawLine(x)
    left(90)
    backward(25)
    drawLine(x)
    space()

def draw_N():
    """
	draw_N() will draw the letter N in the turtle area. This function may be reused
	wherever the programmer would like a N.
    """
    right(90)
    drawLine(x)
    backward(x)
    left(45)
    drawLine(math.sqrt(5000))
    left(135)
    drawLine(x)
    backward(x)
    right(90)
    space()

def draw_Flair():
    """
	draw_Flair() will draw a border and a smily face on the turtle screen! Remove the
	# before #drawFlair() in the draw() function use it!
    """
    up()
    speed(8)
    pensize(5)
    pencolor("SteelBlue")
    right(90)
    drawLine(70)
    down()
    right(90)
    drawLine(940)
    right(90)
    drawLine(90)
    right(90)
    drawLine(940)
    right(90)
    drawLine(90)
    up()
    pensize(3)
    pencolor("Aqua")
    drawLine(5)
    down()
    right(90)
    drawLine(942)
    right(90)
    drawLine(100)
    right(90)
    drawLine(944)
    right(90)
    drawLine(100)
    up()
    left(90)
    drawLine(25)
    left(90)
    drawLine(75)
    left(90)
    forward(15)
    down()
    pencolor("gold")
    dot(20)
    up()
    backward(25)
    down()
    dot(20)
    up()
    backward(3)
    left(90)
    drawLine(40)
    down()
    circle(-15,180)
    up()
    backward(20)
    right(90)
    drawLine(x)
    
#Call main()
main()
