"""
    harmonograph.py
    Colin Fausnaught
    10/5/14

    uses forumulas for harmonographs to create a picture.

    The formulas are:
    
    x1 = 200*sin(f1*t + p1)*e**(-t*d1) + 200*sin(f2*t +p2)*e**(-t*d2)
    y1 = 200*sin(f3*t + p3)*e**(-t*d3) + 200*sin(f4*t +p4)*e**(-t*d4)
"""

from turtle import *
from math import *
import sys
import colorsys

def main():
    sys.setrecursionlimit(10000)
    
    f1 = 8.2
    f2 = 8.2
    f3 = 8.2
    f4 = 8.1

    #phase shifts
    p1 = 2*pi
    p2 = 2*pi
    p3 = 27*pi/16
    p4 = 2*pi

    #decay
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0

    t = 0
    dt = 0.05
    speed(0)
    clear()
    ht()
    color('red')
    title("Colin Fausnaught: Harmonograph.py")    
    up()
    recursiveDraw(f1,f2,f3,f4,p1,p2,p3,p4,d1,d2,d3,d4,t,dt, 1500)

def recursiveDraw(f1,f2,f3,f4,p1,p2,p3,p4,d1,d2,d3,d4,t,dt,depth):
    if depth == 0:
        pass
    else:
        colors = colorsys.hsv_to_rgb(depth/2000, 1.0, 1.0)
        color(colors)
        x1 = 200*sin(f1*t + p1)*e**(-t*d1) + 200*sin(f2*t +p2)*e**(-t*d2)
        y1 = 200*sin(f3*t + p3)*e**(-t*d3) + 200*sin(f4*t +p4)*e**(-t*d4)
        setpos(x1,y1)
        t += dt
        down()
        recursiveDraw(f1,f2,f3,f4,p1,p2,p3,p4,d1,d2,d3,d4,t,dt,depth-1)

main()
