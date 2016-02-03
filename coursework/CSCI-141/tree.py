"""
 tree.py
"""

from turtle import *

def init():
	clear()
	left( 90 )

def drawTree0():
	pass

def drawTree1( size ):
	forward( size )
	forward( -size )

def drawTree2( size ):
	forward( size )
	left( 45 )
	drawTree1( size / 2 )
	right( 60 )
	drawTree1( size / 2 )
	left( 60 )
	forward( -size )

def drawTree3( size ):
	forward( size )
	left( 45 )
	drawTree2( size / 2 )
	right( 90 )
	drawTree2( size / 2 )
	left( 45 )
	forward( -size )

def drawTreeRecursive( depth, size ):
	if depth == 0:
		pass
	else:
		forward( size )
		left( 45 )
		drawTreeRecursive( depth - 1, size / 2 )
		right( 90 )
		drawTreeRecursive( depth - 1, size / 2 )
		left( 45 )
		forward( -size )

def main():
	init()
	drawTree1( 100 )
	input( 'hit enter for the next one' )
	init()
	drawTree2( 100 )
	input( 'hit enter for the next one' )
	init()
	drawTree3( 100 )
	input( 'hit enter for the next one' )
	init()
	depth = int( input( "number of segments: " ) )
	drawTreeRecursive( depth, 100 )
	input( 'hit enter for the next one' )
	bye()

main()
