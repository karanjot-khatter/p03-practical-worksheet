#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     08/05/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from graphics import *

def plotRainfall():
    win = GraphWin("Daily rainfall over a 7 day period", 500,400)
    win.setCoords(0,0,10,14)
    win.setBackground("white")

    #bottom box
    bottomBox = Rectangle(Point(0,2),Point(14,0))
    bottomBox.setFill("green")
    bottomBox.draw(win)

    #text - instructions
    instruction = Text(Point(4,1),"Please enter the amount of rainfall (in mm) for day:")
    instruction.setStyle("italic")
    instruction.setSize(10)
    instruction.setStyle("bold")
    instruction.draw(win)
    instruction1 = Text(Point(4,0.5),"(Click after entry)")
    instruction1.setSize(10)
    instruction1.draw(win)

    #entry
    instructionE = Entry(Point(8.5,1),6)
    instructionE.setText(0)
    instructionE.draw(win)

    #x line
    x = Line(Point(2,4),Point(9,4))
    x1 = Text(Point(5.5,2.5),"Period (days)")
    x1.setSize(8)
    x1.draw(win)
    x.setWidth(2)
    x.draw(win)

    #y line
    y = Line(Point(2,4),Point(2,13))
    y1 = Text(Point(0.75,8.5),"Rainfall ").draw(win)
    y2 = Text(Point(0.75,8),"(mm) ").draw(win)
    y.setWidth(2)
    y.draw(win)

    #axises (x)
    for i in range(2,10):
        axisX = Line(Point(i,3.75), Point(i,4.25))
        axisX.setWidth(2)
        axisX.draw(win)

    #axises (y)
    for i in range(1,10):
        axisY = Line(Point(1.75,i+3), Point(2.25,i+3))
        axisY.setWidth(2)
        axisY.draw(win)

    #label x

    for i in range(0,7):
        labelX = Text(Point(i+2.5, 3.50), i+1).draw(win)

    #label y
    for i in range(0,9):
        labelY = Text(Point(1.5, i+4), i*10).draw(win)

    #user input
    for i in range(1,8):
        instruction2 = Text(Point(7.5,1),i+0)
        instruction2.setStyle("italic")
        instruction2.setSize(10)
        instruction2.setStyle("bold")
        instruction2.draw(win)
        instruction2.setText
        click1 = win.getMouse()
        rectangle = eval(instructionE.getText())
        instruction2.setText(i)
        instruction2.setText("")

        drawRectangle = Rectangle(Point(i+2, rectangle/10+4), Point(i+1, 4))
        drawRectangle.setFill("blue")
        drawRectangle.setOutline("red")
        drawRectangle.setWidth(4)
        drawRectangle.draw(win)

    bottomBox.setFill("yellow")
    instruction.setSize(12)
    instruction.setText("Finished! Click anywhere to close.")
    instruction.setStyle("bold")
    instruction1.setText("")
    instructionE.undraw()

    win.getMouse()
    win.close()

plotRainfall()