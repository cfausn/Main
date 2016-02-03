"""
    implements plotter letterFreqPlot

    AUTHOR: Colin Fausnaught
"""

from turtle import *

def letterFreqPlot(freqList):
    """
    called by other programs to plot the turtle histogram of letter frequencies.

    :param freqList: A list of floating points values between 0.0 and 1.0. The first entry
                    corresponds to the letter ’a’, the second entry to the letter ’b’, and so on.
    :return: The function returns None, draws a histogram of letter frequencies
    """
    maxNum = 0.0
    for elm in freqList:
        if elm > maxNum:
            maxNum = float(elm)

    setWindow(maxNum)
    yAxis(maxNum)
    xAxis(maxNum, freqList)

    input('Press Enter to Quit: ')
    bye()


def setWindow(maxNum):
    """
    sets the window size for the turtle drawing. Then draws the beginning of the
    bar graph, which will be labeled and filled in later.

    :param maxNum: the largest number in the data set. (float)
    :return: The function returns None
    """
    #set coords
    hideturtle()
    screensize(800,800)
    setworldcoordinates(-100,-(maxNum/10),700,(maxNum + maxNum / 10))

    home()
    up()
    goto(-100,(maxNum / 2))
    write("Frequency",font=("Arial", 12, "normal"))
    goto(250,-(maxNum / 11))
    write("Letter",font=("Arial", 12, "normal"))

    goto(250,maxNum)
    write("Letter Frequencies",font=("Arial", 18, "bold"))

    home()

    #make the graph

    down()
    goto(0,maxNum)
    home()
    goto(-10,0)
    up()
    goto(-25,0)
    write("0.0" ,font=("Arial", 8, "normal"))
    home()


def yAxis(maxNum):
    """
    draws the y axis, which includes labels in tenths.

    :param maxNum: the largest number in the data set. (float)
    :return: The function returns None
    """
    #draw y axis
    counter = 1
    while counter != 11:
        goto(0,(counter * (maxNum/10)))
        down()
        goto(-10,(counter * (maxNum/10)))
        up()
        goto(-25,(counter * (maxNum/10)))
        write(str("%.3f" % (counter *(maxNum/10))) ,font=("Arial", 8, "normal"))


        counter += 1

def xAxis(maxNum, freqList):
    """
    draws the x axis and plots the bar bar graph at each letter point.

    :param maxNum: the largest number in the data set. (float)
    :param freqList: A list of floating points values between 0.0 and 1.0. The first entry
                    corresponds to the letter ’a’, the second entry to the letter ’b’, and so on.
    :return: The function returns None
    """

    #draw x axis
    home()
    down()
    goto(600,0)
    home()
    up()

    counter = 1
    while counter != 27:
        up()
        goto((counter * (600/26)),0)
        down()
        goto((counter * (600/26)),-(maxNum/16))
        up()
        goto((counter * (600/26)) - 13 ,-(maxNum/16))
        write(str(chr(counter + 64)) ,font=("Arial", 8, "normal"))

        if freqList[counter - 1] != 0.0:

            fillcolor('blue')
            goto((counter * (600/26)), freqList[counter - 1])
            begin_fill()
            goto(((counter * (600/26)) - (600/26)), freqList[counter - 1])
            goto(((counter * (600/26)) - (600/26)), 0)
            goto((counter * (600/26)), 0)
            end_fill()



        counter += 1