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
from copy import deepcopy

print "Oh holy ruler, welcome to \n"

print """    #####  #####  #####  ##   [v.01]
    ##     ##     ##  #  ##
    ##     ## ##  ##  #  ##
    #####  #####  #####  ######
        """
SIZE = int(raw_input('Please input the size of The Garden of Eden [positive integer]: '))
CHANCE_OF_LIFE = float(raw_input('Please input the chances of initial life [positive double between 0-1 ]: '))
TIME_DELAY = float(raw_input('Please specify the time period which life should develop by [positive double]: '))

def rndmMtrx(size):
    mtrx = []
    for i in range(size):
        mtrx.append([1 if uniform(0,1) <= CHANCE_OF_LIFE else 0 for x in range(size)])
    return mtrx

def clear():
    for n in range(0, 64, 1): 
        print("\r\n")

def printLine(user_string = "", hor = 0, ver = 0):
    # Fixing an error in the hor/ver starting point (somehow 0 and 1 both start in 0)
    hor += 1
    ver += 1
    # Plot the user_string at the starting at position hor, ver
    print("\033[" + str(ver) + ";" + str(hor) + "f" + formatLine(user_string)) 

def formatLine(line):
    output = ""
    for i, item in enumerate(line):
        item = str(item)
        item = item.replace('1', 'X').replace('0', ' ')
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
    newMtrx = deepcopy(mtrx)

    for i, line in enumerate(newMtrx):

        iMin = i - 1
        if iMin < 0:
            iMin = SIZE - 1

        iPlu = i + 1        
        if iPlu > SIZE - 1:
            iPlu = 0

        for j, item in enumerate(line):
            neighbours = 0

            jMin = j - 1
            if jMin < 0:
                jMin = SIZE - 1

            jPlu = j + 1
            if jPlu > SIZE - 1:
                jPlu = 0

            neib = [("mtrx["+str(iMin)+"]["+str(jMin)+"]", mtrx[iMin][jMin]), ("mtrx["+str(iMin)+"]["+str(j)+"]", mtrx[iMin][j]),  ("mtrx["+str(iMin)+"]["+str(jPlu)+"]", mtrx[iMin][jPlu]),\
                    ("mtrx["+str(i)+"]["+str(jMin)+"]", mtrx[i][jMin]), ("mtrx["+str(i)+"]["+str(jPlu)+"]", mtrx[i][jPlu]),\
                    ("mtrx["+str(iPlu)+"]["+str(jMin)+"]", mtrx[iPlu][jMin]), ("mtrx["+str(iPlu)+"]["+str(j)+"]", mtrx[iPlu][j]), ("mtrx["+str(iPlu)+"]["+str(jPlu)+"]",mtrx[iPlu][jPlu])]

            neighbours = mtrx[iMin][jMin] + mtrx[iMin][j] + mtrx[iMin][jPlu] + mtrx[i][jMin] + mtrx[i][jPlu] + mtrx[iPlu][jMin] + mtrx[iPlu][j] + mtrx[iPlu][jPlu]
            
            if item == 1 and neighbours < 2:
                newMtrx[i][j] = 0
            elif item == 1 and (neighbours == 2 or neighbours == 3):
                newMtrx[i][j] = 1
            elif item == 1 and neighbours > 3:
                newMtrx[i][j] = 0
            elif item == 0 and neighbours == 3:
                newMtrx[i][j] = 1

    return newMtrx

smMtrx = rndmMtrx(SIZE)

while 1:
    printMtrx(smMtrx)
    smMtrx = nextMove(smMtrx)
