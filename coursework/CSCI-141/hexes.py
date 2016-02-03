"""
	hexes.py
	Colin Fausnaught
	CSCI - 141
	8/25/14, rev. 8/27/14
"""

import turtle


def main():
	"""
		This program creates a hexagon using 
		turtle graphics, and exits when the user presses
		the ENTER key. 
	"""
	global x
	x = 60
	draw()
	input("Press ENTER to close")
	turtle.bye()
	
	
def draw():
	"""
		This function directs the other functions in the 
		proper order in order to create the hexagon shapes.
	"""
	movePositionOne()
	movePositionTwo()
	movePositionThree()
	movePositionFour()
	movePositionFive()
	movePositionSix()


def drawStraight():
	"""
		This function is used to draw a straight 
		line. This will be used to make the sides
		of the hexagons.
	"""
	turtle.down()
	turtle.forward(100)

def moveStraight():
	"""
		This function is used to move the pointer
		without drawing. This will help move the 
		pointer to the starting point of each hexagon.
	"""
	turtle.up()
	turtle.forward(100)

def turnRight(x):
	"""
		This function will turn the pointer to the right. The 
		programmer may pass variables and values to this
		function in order to make the program simpler and
		more efficient.
	"""
	turtle.right(x)

def turnLeft(x):
	"""
		This function will turn the pointer to the left. The 
		programmer may pass variables and values to this
		function in order to make the program simplerand
		more efficient.
	"""
	turtle.left(x)
	
	
def movePositionOne():
	"""
		This function both sets the title "Hexagons"
		and moves the pointer to the correct starting
		position, then calls drawHex() to draw the first hexagon.
	"""	
	turtle.title("Hexagons")
	turtle.up()
	turtle.forward(50)
	drawHex()

def drawHex():
	"""
		This function is used to draw a hexagon. It will
		draw a hexagon no matter where the pointer is placed,
		so the programmer must move the cursor to where he would
		like the hexagon drawn.
	"""
	drawStraight()
	turnRight(x)
	drawStraight()
	turnRight(x)
	drawStraight()
	turnRight(x)
	drawStraight()
	turnRight(x)
	drawStraight()
	turnRight(x)
	drawStraight()
	turnRight(x)

def movePositionTwo():
	"""
		This function moves the pointer to the correct position
		so the drawHex() function will draw the second hexagon
		in the correct place.
	"""
	turnLeft(120)
	moveStraight()
	turnRight(x)
	moveStraight()
	turnRight(x)
	drawHex()

def movePositionThree():
	"""
		This function moves the pointer to the correct position
		so the drawHex() function will draw the third hexagon
		in the correct place.
	"""
	turnLeft(120)
	moveStraight()
	turnLeft(x)
	moveStraight()
	turnLeft(180)
	drawHex()

def movePositionFour():
	"""
		This function moves the pointer to the correct position
		so the drawHex() function will draw the fourth hexagon
		in the correct place.
	"""
	turnRight(120)
	moveStraight()
	turnRight(x)
	moveStraight()
	turnRight(180)
	drawHex()

def movePositionFive():
	"""
		This function moves the pointer to the correct position
		so the drawHex() function will draw the fifth hexagon
		in the correct place.
	"""
	turnRight(120)
	moveStraight()
	turnLeft(x)
	moveStraight()
	turnLeft(x)
	drawHex()

def movePositionSix():
	"""
		This function moves the pointer to the correct position
		so the drawHex() function will draw the six hexagon
		in the correct place.
	"""
	moveStraight()
	turnRight(x)
	moveStraight()
	turnLeft(x)
	drawHex()

#Call main

main()
