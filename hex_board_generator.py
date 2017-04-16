from turtle import *
#import turtle
import math
import random
import os

def SETUP():
    global size
    size = int(raw_input("Wielkosc planszy: "))
    global turtle
    turtle = Turtle()
    global wid
    wid = 800

    global side
    side = wid / ((size*2)+(size-1))
#side = 20

    global h
    h = (side*math.sqrt(3))/2

    global hig
    hig = 2*h*((size*2)-1)

    setup(width=wid, height=hig, startx=600, starty=0)
#setup(width=1024, height=800, startx=600, starty=100)
    turtle.speed(0)

    global colors
    colors = ["green", "red", "blue", "yellow", "#8888ff", "orange"]

    global q
    q = False

SETUP()

######### BOARD CREATION #########

def hexx(n):
    turtle.left(120)
    turtle.up()
    turtle.forward(n)
    turtle.down()
    turtle.right(120)
    for i in range(6):
        turtle.forward(n)
        turtle.right(60)
    turtle.up()
    turtle.right(60)
    turtle.forward(n)
    turtle.left(60)
    turtle.down()

def jumpNext(n):
    turtle.up()
    turtle.forward(n)
    turtle.right(60)
    turtle.forward(n)
    turtle.left(60)
    turtle.down()

def jumpBackRow(n):
    turtle.up()
    turtle.right(120)
    turtle.forward(n)
    turtle.right(60)
    turtle.forward(n)
    turtle.left(180)
    turtle.down()

def jumpTop(n, jumps):
    turtle.left(60)
    turtle.up()
    for i in range(jumps):
        turtle.forward(side)
        turtle.left(60)
        turtle.forward(side)
        turtle.right(60)
    turtle.down()
    turtle.right(60)

def board(boardSize, side):
    if boardSize == 1:
        turtle.fill(True)
        hexx(side)
        turtle.fill(False)
    else:
        jumpNext(side)
        for o in range(6):
            if boardSize <= 2:
                currentColor = "#cccccc"
            else:
                currentColor = colors[o]
            for i in range(boardSize-1):
                turtle.fillcolor(currentColor)
                turtle.fill(True)
                hexx(side)
                turtle.fill(False)
                if i != max(range(boardSize-1)):
                    jumpNext(side)
            turtle.right(60)
            jumpNext(side)
        jumpBackRow(side)
        board(boardSize - 1, side)
    return

def MAIN():
    turtle.setx(0)
    turtle.sety(0)
    turtle.width(1)
    turtle.hideturtle()
    jumpTop(side, size-1)
    board(size, side)
    jumpTop(side, size-1)
    jumpNext(side)
    turtle.right(30)
    turtle.width(3)
    turtle.color("#000000")
    turtle.showturtle()

MAIN()

######## KEYBOARD CONTROL ########

session = []


def k1():
    turtle.forward(h*2)
    session.append("f")

def k2():
    turtle.left(60)
    session.append("l")

def k3():
    turtle.right(60)
    session.append("r")

def k4():
    turtle.back(h*2)
    session.append("b")

def k5():
    turtle.up()
    turtle.color("#dddddd")
    session.append("u")

def k6():
    turtle.down()
    turtle.color("#000000")
    session.append("d")

def k7():
    turtle.speed(3)
    global q
    if q == True:
        q = False
        print "Miota nim jak szatan!"
    else:
        turtle.speed(0)
        q = True
        print "Ale urwal!"

    while q == True:
        z = random.choice([60, -60, 120, -120, 180])
        turtle.right(z)
        turtle.forward(h*2)

def k8():
    x = 0
    global session
##    while True:
##        mapName = "map"+str(x)
##        try:
##            with open(mapName):
##                f = open(mapName, "w")
##                print "OO"
##                break
##        except IOError:
##            print 'KK'
##            x += 1
    while True:
        mapName = "map"+str(x)
        print "1"
        if os.path.exists(mapName) == True:
            f = open(mapName, "w")
            print "2"
            break
        x += 1
    print "3"
    for i in session:
        print "4"
        f.write(session[i])
        print "5"
    print "6"
    f.close()
    
    

##def k9():
##    clearscreen()
##    resetscreen()
##    setup()
##    MAIN()
    

onkey(k1, "Up")
onkey(k2, "Left")
onkey(k3, "Right")
onkey(k4, "Down")
onkey(k5, "a")
onkey(k6, "z")
onkey(k7, "p")
onkey(bye, "e")
onkey(k8, "s")
##onkey(k9, "r")

listen()
mainloop()
