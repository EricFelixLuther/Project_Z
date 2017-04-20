# -*- coding: cp1250 -*-
from turtle import *
import math
import random
import os

def SETUP():
    global size
    size = int(raw_input("Wielkosc planszy: "))
    global constructor
    constructor = Turtle()
    global wid
    wid = int(raw_input("Podaj szerokosc obrazu: "))

    global side
    side = wid / ((size*2)+(size-1))

    global h
    h = (side*math.sqrt(3))/2

    global hig
    hig = (size+(size-1))*h*2

    setup(width=wid, height=hig, startx=600, starty=0)

    global colors
    colors = ["green", "red", "blue", "yellow", "#8888ff", "orange"]

    global q
    q = False

SETUP()

######### BOARD CREATION #########

def hexx(n):
    constructor.left(120)
    constructor.up()
    constructor.forward(n)
    constructor.down()
    constructor.right(120)
    for i in range(6):
        constructor.forward(n)
        constructor.right(60)
    constructor.up()
    constructor.right(60)
    constructor.forward(n)
    constructor.left(60)
    constructor.down()

def jumpNext(n):
    constructor.up()
    constructor.forward(n)
    constructor.right(60)
    constructor.forward(n)
    constructor.left(60)
    constructor.down()

def jumpBackRow(n):
    constructor.up()
    constructor.right(120)
    constructor.forward(n)
    constructor.right(60)
    constructor.forward(n)
    constructor.left(180)
    constructor.down()

def jumpTop(n, jumps):
    constructor.left(60)
    constructor.up()
    for i in range(jumps):
        constructor.forward(side)
        constructor.left(60)
        constructor.forward(side)
        constructor.right(60)
    constructor.down()
    constructor.right(60)

def board(boardSize, side):
    if boardSize == 1:
        constructor.fill(True)
        hexx(side)
        constructor.fill(False)
    else:
        jumpNext(side)
        for o in range(6):
            if boardSize <= 2:
                currentColor = "#cccccc"
            else:
                currentColor = colors[o]
            for i in range(boardSize-1):
                constructor.fillcolor(currentColor)
                constructor.fill(True)
                hexx(side)
                constructor.fill(False)
                if i != max(range(boardSize-1)):
                    jumpNext(side)
            constructor.right(60)
            jumpNext(side)
        jumpBackRow(side)
        board(boardSize - 1, side)
    return

def MAIN():
    constructor.setx(0)
    constructor.sety(0)
    constructor.width(1)
    constructor.speed(0)
    constructor.hideturtle()
    jumpTop(side, size-1)
    board(size, side)
    jumpTop(side, size-1)
    jumpNext(side)
    constructor.right(30)
    constructor.width(3)
    constructor.color("#000000")
    constructor.showturtle()
    global session
    session = []

MAIN()

######## KEYBOARD CONTROL ########



def k1():
    constructor.forward(h*2)
    session.append("f")

def k2():
    constructor.left(60)
    session.append("l")

def k3():
    constructor.right(60)
    session.append("r")

def k4():
    constructor.back(h*2)
    session.append("b")

def k5():
    constructor.up()
    constructor.color("#dddddd")
    session.append("u")

def k6():
    constructor.down()
    constructor.color("#000000")
    session.append("d")

def k7():
    def toStart():
        constructor.up()
        constructor.setx(0)
        constructor.sety(0)
        constructor.down()
    global q
    if q == True:
        toStart()
        q = False
        print "Ale urwal!"
        constructor.speed(0)
    else:
        toStart()
        constructor.speed(4)
        q = True
        print "Miota nim jak szatan!"

    while q == True:
        z = random.choice([60, -60, 120, -120, 180])
        constructor.right(z)
        constructor.forward(h*2)

    toStart()

def save():
    x = 0
    global session
    global size
    while True:
        mapName = "map"+str(x)+".txt"
        if os.path.exists(mapName) == False:
            f = open(mapName, "w")
            break
        x += 1
    f.write(str(size) + "\n")
    for i in range(len(session)):
        f.write(session[i])
    f.close()
    
def load():
    def loadd():
        global session
        mapName = raw_input(str("Podaj nazwe mapy: "))
        f = open(mapName+".txt", "r")
        g = f.readline()
        if int(g) != size:
            print "Ta mapa jest przeznaczona dla rozmiaru", g
            print "Sprobuj jeszcze raz!"
            return
        g = f.readline()
        for i in range(len(g)):
            session.append(g[i])
        f.close()

        for i in range(len(g)):
            if g[i] == "f":
                constructor.forward(h*2)
            elif g[i] == "b":
                constructor.back(h*2)
            elif g[i] == "r":
                constructor.right(60)
            elif g[i] == "l":
                constructor.left(60)
            elif g[i] == "u":
                constructor.up()
            elif g[i] == "d":
                constructor.down()

    if session == []:
        loadd()
    else:
        resett()
        loadd()
        
def resett():
    constructor.reset()
    global size
    question = raw_input("Zmienić rozmiar mapy? T/N? ")
    if question == "T" or question == "t":
        size = int(raw_input("Wielkosc planszy: "))
    MAIN()

def clearr():
    constructor.clear()

print "Klawisze:"
print "Strzalki - poruszaj wskaznikiem"
print "A - podnies wskaznik"
print "Z - upusc wskaznik"
print "P - pozwol aby wskaznik zostal opentany przez nieczyste moce"
print "E - exit"
print "S - save / zapisz"
print "L - load / zaladuj"
print "R - reset calej mapy"
print "T - wyczysc"

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
