# Copyright 2013, Olafur Bogason
# Conway's game of life.
# http://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
# The console print is based of http://code.activestate.com/recipes/578167-position-the-cursor-almost-anywhere-inside-standar/
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# This is a bare-bone alpha version merely coded to make a sort-of skeleton for future versions. 
# Future vesions will most definitely have OOP and a nicer console display (maybe colour! who knows).


from time import sleep
from random import uniform

# Global Variables, the names easilly give out their purpose.
SIZE = 32
TIME_DELAY = 0.5
CHANCE_OF_LIFE = 0.5

def rndmMtrx(size):
    mtrx = []
    for i in range(size):
        mtrx.append([1 if uniform(0,1) < CHANCE_OF_LIFE else 0 for x in range(size)])
    return mtrx

def clear():
    for n in range(0, 64, 1): 
        print("\r\n")

def printLine(user_string = "", hor = 0, ver = 0):
    # Fixing an error in the hor/ver starting point (somehow 0 and 1 both start in 0)
    hor += 1
    ver += 1
    # Plot the user_string at the starting at position x, y...
    print("\033[" + str(ver) + ";" + str(hor) + "f" + formatLine(user_string)) 

def formatLine(line):
    output = ""
    for i, item in enumerate(line):
        item = str(item)
        item = item.replace('1', 'X')
        if i < len(line):
            output += item + " "
        else:
            output += item + "\n"
    return output

def printMtrx(mtrx):
    clear()
    for i, sublist in enumerate(mtrx):
        printLine(sublist, 0, i)
    sleep(TIME_DELAY)

def nextMove(mtrx):
    newMtrx = mtrx
    for i, line in enumerate(mtrx):
        for j, item in enumerate(line):
            neighbours = 0
            i1 = i - 1
            if i1 < 0:
                i1 = SIZE - 1

            i2 = i + 1
            if i2 >= SIZE:
                i2 = 0

            j1 = j - 1
            if j1 < 0:
                j1 = SIZE - 1

            j2 = j + 1
            if j2 >= SIZE:
                j2 = 0

            neighbours = mtrx[i1][j2] + mtrx[i][j2] + mtrx[i2][j2] + \
                         mtrx[i1][j] + mtrx[i2][j] + \
                         mtrx[i1][j1] + mtrx[i][j1] + mtrx[i2][j1]

            if mtrx[i][j] == 1 and neighbours < 2:
                newMtrx[i][j] = 0
            elif mtrx[i][j] == 1 and (neighbours == 2 or neighbours == 3):
                newMtrx[i][j] = 1
            elif mtrx[i][j] == 1 and neighbours > 3:
                newMtrx[i][j] = 0
            elif mtrx[i][j] == 0 and neighbours == 3:
                newMtrx[i][j] = 1
            
    return newMtrx

smMtrx = rndmMtrx(SIZE)

while 1:
    printMtrx(smMtrx)
    smMtrx = nextMove(smMtrx)