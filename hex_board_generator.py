from turtle import *
import math
import random
import os

def SETUP():
    global size
    size = int(raw_input("Wielkosc planszy: "))
    global turtle
    turtle = Turtle()
    global wid
    wid = 500

    global side
    side = wid / ((size*2)+(size-1))

    global h
    h = (side*math.sqrt(3))/2

    global hig
    hig = wid*(math.sqrt(3))

    setup(width=wid, height=hig, startx=600, starty=0)
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
    turtle.up()
    turtle.setx(0)
    turtle.sety(0)
    turtle.down()
    turtle.speed(3)
    global q
    if q == True:
        q = False
        print "Ale urwal!"
    else:
        turtle.speed(0)
        q = True
        print "Miota nim jak szatan!"

    while q == True:
        z = random.choice([60, -60, 120, -120, 180])
        turtle.right(z)
        turtle.forward(h*2)

def save():
    x = 0
    global session
    while True:
        mapName = "map"+str(x)
        if os.path.exists(mapName) == False:
            f = open(mapName, "w")
            break
        x += 1
    for i in range(len(session)):
        f.write(session[i])
    f.close()
    
def load():
    global session
    session = []
    mapName = raw_input(str("Podaj nazwe mapy: "))
    f = open(mapName, "r")
    g = f.read()
    for i in range(len(g)):
        session.append(g[i])
    f.close()

    for i in range(len(g)):
        if g[i] == "f":
            turtle.forward(h*2)
        elif g[i] == "b":
            turtle.back(h*2)
        elif g[i] == "r":
            turtle.right(60)
        elif g[i] == "l":
            turtle.left(60)
        elif g[i] == "u":
            turtle.up()
        elif g[i] == "d":
            turtle.down()

def resett():
    turtle.reset()
    turtle.speed(0)
    MAIN()

def clearr():
    turtle.clear()

def k9():
    turtle.clearscreen()

def k10():
    turtle.resetscreen()
    

onkey(k1, "Up")
onkey(k2, "Left")
onkey(k3, "Right")
onkey(k4, "Down")
onkey(k5, "a")
onkey(k6, "z")
onkey(k7, "p")
onkey(bye, "e")
onkey(save, "s")
onkey(load, "l")
onkey(resett, "r")
onkey(clearr, "t")

listen()
mainloop()
