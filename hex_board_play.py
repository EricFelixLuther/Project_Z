from turtle import *
import math
import random
import os

############ FUNKCJE #############

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

def SETUP(size, wid):
    global constructor
    constructor = Turtle()

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

############# SETUP ##############

## Setup startowy ##
wid = int(raw_input("Podaj szerokosc obrazu: "))
mapName = raw_input(str("Podaj nazwe mapy do wczytania: "))
f = open(mapName+".txt", "r")
size = int(f.readline())
SETUP(size, wid)

## Rysuj grid ##

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

## Rysuj mape ##

g = f.readline()
for i in range(len(g)):
##    session.append(g[i])

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

f.close()

constructor.hideturtle()

## THE GAME ##

K6 = [1, 2, 3, 4, 5, 6]
K4 = [1, 2, 3, 4]
K3 = [1, 2, 3]
K62 = [1, 1, 1, 2, 2, 3]
K63 = [1, 2, 2, 3, 3, 4]

dices = [K6, K4, K3, K62, K63]

def dice(k):
    return random.choice(k)

print "Ktora koscia bedziemy rzucac?:"
for i in dices:
    print i
    
mainDice = dices[(raw_input())]
        
onkey(bye, "e")

listen()
mainloop()
