#!/usr/bin/env python

import math
import sys
import time
import random

import scrollphat




def pos1():
    scrollphat.set_pixel(7,0,1)
    scrollphat.set_pixel(6,0,1)
    scrollphat.set_pixel(5,0,1)
    scrollphat.set_pixel(4,0,1)

def pos2():
    scrollphat.set_pixel(7,0,1)
    scrollphat.set_pixel(7,1,1)
    scrollphat.set_pixel(7,2,1)

def pos3():
    scrollphat.set_pixel(7,2,1)
    scrollphat.set_pixel(7,3,1)
    scrollphat.set_pixel(7,4,1)

def pos4():
    scrollphat.set_pixel(7,4,1)
    scrollphat.set_pixel(6,4,1)
    scrollphat.set_pixel(5,4,1)
    scrollphat.set_pixel(4,4,1)

def pos5():
    scrollphat.set_pixel(4,4,1)
    scrollphat.set_pixel(4,3,1)
    scrollphat.set_pixel(4,2,1)

def pos6():
    scrollphat.set_pixel(4,2,1)
    scrollphat.set_pixel(4,1,1)
    scrollphat.set_pixel(4,0,1)

def pos7():
    scrollphat.set_pixel(4,2,1)
    scrollphat.set_pixel(5,2,1)
    scrollphat.set_pixel(6,2,1)
    scrollphat.set_pixel(7,2,1)

def numone():
    pos5()
    pos6()

def numtwo():
    pos1()
    pos2()
    pos7()
    pos5()
    pos4()

def numthree():
    pos1()
    pos2()
    pos7()
    pos4()
    pos3()

def numfour():
    pos6()
    pos7()
    pos2()
    pos3()

def numfive():
    pos1()
    pos6()
    pos7()
    pos3()
    pos4()

def numsix():
    pos1()
    pos6()
    pos5()
    pos7()
    pos4()
    pos3()

def numseven():
    pos1()
    pos2()
    pos3()

def numeight():
    pos1()
    pos2()
    pos3()
    pos4()
    pos5()
    pos6()
    pos7()

def updaterelax():
    scrollphat.set_brightness(20)
    scrollphat.update()
    time.sleep(1)
    scrollphat.clear()

def hardblink():
    scrollphat.set_brightness(20)
    scrollphat.update()
    time.sleep(.3)
    scrollphat.clear()
    time.sleep(.7)

def randdice():
    dicearray = [numone,numtwo,numthree,numfour,numfive,numsix]
    roll = random.randint(1,6)
    roll = roll - 1
    newroll = dicearray[roll]()    
    scrollphat.set_brightness(20)
    scrollphat.update()
    time.sleep(10)
    scrollphat.clear()

def flashingdice():
    dicearray = [numone,numtwo,numthree,numfour,numfive,numsix]
    x = 0
    while x < 20:
        roll = random.randint(1,6)
        roll = roll - 1
        newroll = dicearray[roll]()    
        scrollphat.set_brightness(20)
        scrollphat.update()
        time.sleep(.1)
        scrollphat.clear()
        x += 1
    



