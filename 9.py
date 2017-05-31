#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     07/05/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from graphics import *
import math
def fiveClickStickFigure():
    win = GraphWin("5 click stick figure",300,500)
    win.setBackground("white")
    introBox = Rectangle(Point(0,400),Point(300,500))
    introBox.setFill("green")
    introBox.draw(win)

    introText = Text(Point(100,425), "Stick figure builder says:")
    introText.setStyle("italic")
    introText.draw(win)
    commandText = Text(Point(150,450),"Click the first point for the head")
    commandText.setSize(8)
    commandText.setStyle("bold")
    commandText.draw(win)

    click1 = win.getMouse()
    click1.draw(win)
    commandText.setText("Click the second point for the outter head")
    click2 = win.getMouse()
    click2.draw(win)

    x1 = click1.getX()
    x2 = click2.getX()
    y1 = click1.getY()
    y2 = click2.getY()

    distance =((x2-x1)**2) + ((y2-y1) **2)
    sqrt = math.sqrt(distance)

    head = Circle(click1,sqrt).draw(win)

    #third point
    commandText.setText("Click the third point for the body")
    click3 = win.getMouse()
    click3.draw(win)
    x = click3.getX()
    y = click3.getY()

    body = Line(Point(x1, y1 + sqrt),Point(x,y)).draw(win)

    #fourth point

    commandText.setText("Click the fourth point for the arms ")
    click4 = win.getMouse()
    click4.draw(win)
    cx = click4.getX()
    cy = click4.getY()
    distance = cx - x
    line1 = Line(Point(cx,cy), Point(x,cy)).draw(win)
    Line2 = Line(Point(x,cy), Point(x - distance,cy)).draw(win)

    #fifth point
    commandText.setText("Click the last point for the legs ")
    click5 = win.getMouse()
    click5.draw(win)
    cx5 = click5.getX()
    cy5 = click5.getY()
    distanceX = cx5 - x
    distanceY = cy5 - y
    Line1 = Line(Point(x,y),Point(cx5,cy5)).draw(win)
    Line2 = Line(Point(x,y),Point(x - distanceX, y + distanceY)).draw(win)

    introBox.setFill("red")
    commandText.setText("Completed! ")

    win.getMouse()
    win.close()





fiveClickStickFigure()