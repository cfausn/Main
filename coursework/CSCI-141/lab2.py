"""
    lab2.py
"""
from turtle import *

def init():
    clear()

def main():
    left(90)
    
    init()
    """
    triangle1(100)
    input("Enter for next iteration") 
    init()
    triangle2(100)
    input("Enter for next iteration") 
    init()
    triangle3(100)
    input("Enter for next iteration") 
    init()
    triangle4(100)
    """
    depth = int(input("Enter number of iterations "))
    triangleRec(depth, 100)

def triangle0():
    pass

def triangle1(size):
    left(30)
    forward(size)
    right(120)
    forward(size)
    right(120)
    forward(size)
    right(150)

def triangle2(size):
    left(30)
    forward(size)
    right(30)
    triangle1(size/2)
    right(90)
    forward(size)
    left(90)
    triangle1(size/2)
    left(150)
    forward(size)
    right(150)

def triangle3(size):
    left(30)
    forward(size)
    right(30)
    triangle2(size/2)
    right(90)
    forward(size)
    left(90)
    triangle2(size/2)
    left(150)
    forward(size)
    right(150)

def triangleRec(depth, size):
    fd(size/2)
    lt(90)
    triangleRec(depth-1, size/2)
    rt(90)
    fd(-size)
    lt(90)
    triangleRec(depth-1, size/2)
    rt(90)
    fd(size/2)

main()
