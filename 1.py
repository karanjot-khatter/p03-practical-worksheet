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
def drawStickFigure():
    win = GraphWin("Stick figure") #200 x 200 default
    head = Circle(Point(100, 60), 20).draw(win)
    body = Line(Point(100, 80), Point(100, 120)).draw(win)
    arms = Line(Point(50,90), Point(150,90)).draw(win)
    leg1 = Line(Point(100,120), Point(70,170)).draw(win)
    leg2 = Line(Point(100,120), Point(130,170)).draw(win)
    win.getMouse()
    win.close()

drawStickFigure()

def drawCircle():
    circleInput = eval(input("What is the radius of circle? (in cm)"))
    win = GraphWin("Draw circle in center of graphics window") #default 200 x 200
    center = Point(100,100)
    circle = Circle(center,circleInput).draw(win)
    win.getMouse()
    win.close()

drawCircle()

def drawArcheryTarget():
    win= GraphWin("archery target")
    center = Point(100,100)
    blueCircle = Circle(center,60)
    blueCircle.setFill("blue")
    blueCircle.draw(win)

    redCircle = Circle(center,40)
    redCircle.setFill("red")
    redCircle.draw(win)

    yellowCircle = Circle(center,20)
    yellowCircle.setFill("yellow")
    yellowCircle.draw(win)
    win.getMouse()
    win.close()

drawArcheryTarget()

def drawRectangle():
    height,width = eval(input("Please enter the height and width (seprated by commas)"))
    win = GraphWin("Draws rectangle in centre of a graphics window")
    topLeftPoint = Point(100 - width/2, 100 - height/2)
    bottomRightPoint = Point(100 + width/2, 100 + height/2)
    rectangle = Rectangle(topLeftPoint,bottomRightPoint).draw(win)
    win.getMouse()
    win.close()

drawRectangle()

def blueCircle():

    win = GraphWin("Draw a blue circle by user click")
    text = Text(Point(100,20), "Click to draw a circle ")
    text.setFill("red")
    text.setStyle("italic")
    text.draw(win)

    #user input
    p = win.getMouse()

    circle = Circle(p,50)
    circle.setFill("Blue")
    circle.draw(win)

    text.setText("Completed!")
    text.setFill("green")

    win.getMouse()
    win.close()


blueCircle()

def drawLine():

    win = GraphWin("1 line")
    text = Text(Point(100,20), "Click for the first point")
    text.setFill("red")
    text.setStyle("italic")
    text.draw(win)
    text.setText("Click for the first point")
    click1 = win.getMouse()
    click1.draw(win)
    text.setText("Click for the second point")
    click2 = win.getMouse()
    click2.draw(win)
    line = Line(click1,click2).draw(win)

    win.getMouse()
    win.close()

drawLine()

def tenLines():

    win = GraphWin("10 lines")
    text = Text(Point(100,20), "Click for the first point")
    text.setFill("red")
    text.setStyle("italic")
    text.draw(win)

    for i in range(10):
        text.setText("Click for the first point")
        click1 = win.getMouse()
        click1.draw(win)
        text.setText("Click for the second point")
        click2 = win.getMouse()
        click2.draw(win)
        line = Line(click1,click2).draw(win)

    win.getMouse()
    win.close()

tenLines()

def tenStrings():
    win = GraphWin("10 Strings")
    textEntry = Entry(Point(100,20),20).draw(win)

    for i in range(10):
        click = win.getMouse()
        text = textEntry.getText()
        enterText = Text(Point(click.getX(), click.getY()), text).draw(win)
        textEntry.setText("")

    win.getMouse()
    win.close()

tenStrings()

def tenColouredRectangles():
    win = GraphWin("ten coloured rectangles", 300,400)
    introText = Text(Point(140,20),"Please enter a colour underneath:")
    introText.setStyle("bold")
    introText.draw(win)
    textEntry = Entry(Point(100,50),20)
    textEntry.setText("blue")
    textEntry.draw(win)
    changeText = Text(Point(150,70),"Click for the top left corner coordinate")
    changeText.setStyle("italic")
    changeText.setSize(8)
    changeText.draw(win)

    for i in range(10):
        click1 = win.getMouse()
        click1.draw(win)
        changeText.setText("Click for the bottom right corner coordinate")
        click2 = win.getMouse()
        click2.draw(win)
        changeText.setText("Click for the top left corner coordinate")
        rectangle = Rectangle(click1, click2)
        rectangle.setFill(textEntry.getText())
        rectangle.draw(win)

    win.getMouse()
    win.close()

tenColouredRectangles()

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





