#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TextDemo 
# generated by Structorizer 3.30-05 
#  
# Copyright (C) 2019-10-10 Kay Gürtzig 
# License: GPLv3-link 
# GNU General Public License (V 3) 
# https://www.gnu.org/licenses/gpl.html 
# http://www.gnu.de/documents/gpl.de.html 
#  
from enum import Enum
import math
import turtle
turtle.colormode(255)
turtle.mode("logo")

# Draws a blank for font height h, ignoring the colorNo 
def blank(h, colorNo) :
    width = h/2.0
    turtle.penup()
    turtle.right(90)
    col10b8d7cd = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(width)
    turtle.left(90)
    turtle.pencolor(col10b8d7cd)

def forward(len, color) :
    if ((color) == 1) :
        col300a25b7 = turtle.pencolor(); turtle.pencolor("#000000")
        turtle.forward(len)
        turtle.pencolor(col300a25b7)
    elif ((color) == 2) :
        col23ed5649 = turtle.pencolor(); turtle.pencolor("#ff8080")
        turtle.forward(len)
        turtle.pencolor(col23ed5649)
    elif ((color) == 3) :
        colf6d1e26b = turtle.pencolor(); turtle.pencolor("#ffff80")
        turtle.forward(len)
        turtle.pencolor(colf6d1e26b)
    elif ((color) == 4) :
        colafc66775 = turtle.pencolor(); turtle.pencolor("#80ff80")
        turtle.forward(len)
        turtle.pencolor(colafc66775)
    elif ((color) == 5) :
        cola8382637 = turtle.pencolor(); turtle.pencolor("#80ffff")
        turtle.forward(len)
        turtle.pencolor(cola8382637)
    elif ((color) == 6) :
        cold7be9d84 = turtle.pencolor(); turtle.pencolor("#0080ff")
        turtle.forward(len)
        turtle.pencolor(cold7be9d84)
    elif ((color) == 7) :
        colc4b97ff1 = turtle.pencolor(); turtle.pencolor("#ff80c0")
        turtle.forward(len)
        turtle.pencolor(colc4b97ff1)
    elif ((color) == 8) :
        col50bf21d7 = turtle.pencolor(); turtle.pencolor("#c0c0c0")
        turtle.forward(len)
        turtle.pencolor(col50bf21d7)
    elif ((color) == 9) :
        colf3dfe2b4 = turtle.pencolor(); turtle.pencolor("#ff8000")
        turtle.forward(len)
        turtle.pencolor(colf3dfe2b4)
    elif ((color) == 10) :
        col80fc3a4a = turtle.pencolor(); turtle.pencolor("#8080ff")
        turtle.forward(len)
        turtle.pencolor(col80fc3a4a)


# Draws letter A in colour specified by colorNo with font height h 
# from the current turtle position. 
def letterA(h, colorNo) :
    width = h/2.0
    hypo = math.sqrt(h*h + width*width/4.0)
    rotAngle = math.degrees(math.atan(width/2.0/h))
    turtle.right(rotAngle)
    turtle.forward(hypo/2.0, colorNo)
    turtle.right(90 - rotAngle)
    turtle.forward(width/2.0, colorNo)
    turtle.penup()
    col7b28845b = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.backward(width/2.0)
    turtle.pendown()
    turtle.pencolor(col7b28845b)
    turtle.left(90 - rotAngle)
    turtle.forward(hypo/2.0, colorNo)
    turtle.left(2*rotAngle)
    turtle.forward(-hypo, colorNo)
    turtle.right(rotAngle)

# Draws letter E in colour specified by colorNo with font height h 
# from the current turtle position. 
def letterE(h, colorNo) :
    width = h/2.0
    turtle.forward(h, colorNo)
    turtle.right(90)
    turtle.forward(width, colorNo)
    turtle.right(90)
    turtle.penup()
    colc09a491b = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(h/2.0)
    turtle.right(90)
    turtle.pendown()
    turtle.pencolor(colc09a491b)
    turtle.forward(width, colorNo)
    turtle.left(90)
    turtle.penup()
    colbc035478 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(h/2.0)
    turtle.left(90)
    turtle.pendown()
    turtle.pencolor(colbc035478)
    turtle.forward(width, colorNo)
    turtle.left(90)

# Draws letter F in colour specified by colorNo with font height h 
# from the current turtle position. 
def letterF(h, colorNo) :
    width = h/2.0
    turtle.forward(h, colorNo)
    turtle.right(90)
    turtle.forward(width, colorNo)
    turtle.right(90)
    turtle.penup()
    coleca017c6 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(h/2.0)
    turtle.right(90)
    turtle.pendown()
    turtle.pencolor(coleca017c6)
    turtle.forward(width, colorNo)
    turtle.left(90)
    turtle.penup()
    col7930dfba = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(h/2.0)
    turtle.left(90)
    turtle.forward(width)
    turtle.pendown()
    turtle.pencolor(col7930dfba)
    turtle.left(90)

# Draws letter H in colour specified by colorNo with font height h 
# from the current turtle position. 
def letterH(h, colorNo) :
    width = h/2.0
    turtle.forward(h, colorNo)
    turtle.penup()
    turtle.right(90)
    colf440156b = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(width)
    turtle.right(90)
    turtle.pendown()
    turtle.pencolor(colf440156b)
    turtle.forward(h/2.0, colorNo)
    turtle.right(90)
    turtle.forward(width, colorNo)
    turtle.penup()
    cole001a420 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.backward(width)
    turtle.left(90)
    turtle.pendown()
    turtle.pencolor(cole001a420)
    turtle.forward(h/2.0, colorNo)
    turtle.left(180)

# Draws letter I in colour specified by colorNo with font height h 
# from the current turtle position. 
def letterI(h, colorNo) :
    # Octagon edge length 
    b = h * 0.5 / (math.sqrt(2.0) + 1)
    # Cathetus of the corner triangle outside the octagon 
    c = b / math.sqrt(2.0)
    turtle.penup()
    turtle.right(90)
    col70977e3f = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(c)
    turtle.pendown()
    turtle.pencolor(col70977e3f)
    turtle.forward(b, colorNo)
    turtle.penup()
    col75c62ba8 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.backward(b/2.0)
    turtle.left(90)
    turtle.pendown()
    turtle.pencolor(col75c62ba8)
    turtle.forward(h, colorNo)
    turtle.penup()
    turtle.right(90)
    colb2adb307 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.backward(b/2.0)
    turtle.pendown()
    turtle.pencolor(colb2adb307)
    turtle.forward(b, colorNo)
    turtle.penup()
    cola85c641d = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(b/2 + c)
    turtle.left(90)
    turtle.backward(h)
    turtle.pendown()
    turtle.pencolor(cola85c641d)

# Draws letter K in colour specified by colorNo with font height h 
# from the current turtle position. 
def letterK(h, colorNo) :
    width = h/2.0
    diag = h/math.sqrt(2.0)
    turtle.forward(h, colorNo)
    turtle.penup()
    turtle.right(90)
    colc5d2385c = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(width)
    turtle.right(135)
    turtle.pendown()
    turtle.pencolor(colc5d2385c)
    turtle.forward(diag, colorNo)
    turtle.left(90)
    turtle.forward(diag, colorNo)
    turtle.left(135)

# Draws letter L in colour specified by colorNo with font height h 
# from the current turtle position. 
def letterL(h, colorNo) :
    width = h/2.0
    turtle.forward(h, colorNo)
    turtle.penup()
    col310bec3d = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.backward(h)
    turtle.right(90)
    turtle.pendown()
    turtle.pencolor(col310bec3d)
    turtle.forward(width, colorNo)
    turtle.left(90)

# Draws letter M in colour specified by colorNo with font height h 
# from the current turtle position. 
def letterM(h, colorNo) :
    width = h/2.0
    hypo = math.sqrt(width*width + h*h)/2.0
    rotAngle = math.degrees(math.atan(width/h))
    turtle.forward(h, colorNo)
    turtle.left(rotAngle)
    turtle.forward(-hypo, colorNo)
    turtle.right(2*rotAngle)
    turtle.forward(hypo, colorNo)
    turtle.left(rotAngle)
    turtle.forward(-h, colorNo)

# Draws letter N in colour specified by colorNo with font height h 
# from the current turtle position. 
def letterN(h, colorNo) :
    width = h/2.0
    hypo = math.sqrt(width*width + h*h)
    rotAngle = math.degrees(math.atan(width/h))
    turtle.forward(h, colorNo)
    turtle.left(rotAngle)
    turtle.forward(-hypo, colorNo)
    turtle.right(rotAngle)
    turtle.forward(h, colorNo)
    turtle.penup()
    colc6c41532 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.backward(h)
    turtle.pendown()
    turtle.pencolor(colc6c41532)

# Draws letter T in colour specified by colorNo with font height h 
# from the current turtle position. 
def letterT(h, colorNo) :
    width = h/2.0
    turtle.penup()
    colc9083fda = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(h)
    turtle.pendown()
    turtle.pencolor(colc9083fda)
    turtle.right(90)
    turtle.forward(width, colorNo)
    turtle.penup()
    col71110e0c = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.backward(width/2.0)
    turtle.pendown()
    turtle.pencolor(col71110e0c)
    turtle.right(90)
    turtle.forward(h, colorNo)
    turtle.left(90)
    turtle.penup()
    coldd2bb2c9 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(width/2.0)
    turtle.pendown()
    turtle.pencolor(coldd2bb2c9)
    turtle.left(90)

# Draws letter V in colour specified by colorNo with font height h 
# from the current turtle position. 
def letterV(h, colorNo) :
    width = h/2.0
    hypo = math.sqrt(h*h + width*width/4.0)
    rotAngle = math.degrees(math.atan(width/2.0/h))
    turtle.penup()
    col6e2642cf = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(h)
    turtle.left(rotAngle)
    turtle.pendown()
    turtle.pencolor(col6e2642cf)
    turtle.forward(-hypo, colorNo)
    turtle.right(2*rotAngle)
    turtle.forward(hypo, colorNo)
    turtle.penup()
    turtle.left(rotAngle)
    col3679af4b = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.backward(h)
    turtle.pendown()
    turtle.pencolor(col3679af4b)

# Draws letter W in colour specified by colorNo with font height h 
# from the current turtle position. 
def letterW(h, colorNo) :
    width = h/2.0
    width_3 = width/3.0
    hypo = math.sqrt(width_3*width_3 + h*h)
    rotAngle = math.degrees(math.atan(width_3/h))
    turtle.penup()
    col58f566eb = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(h)
    turtle.left(rotAngle)
    turtle.pendown()
    turtle.pencolor(col58f566eb)
    turtle.forward(-hypo, colorNo)
    turtle.right(2*rotAngle)
    turtle.forward(hypo, colorNo)
    turtle.penup()
    turtle.left(90+rotAngle)
    colc0205392 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(width_3)
    turtle.right(90-rotAngle)
    turtle.pendown()
    turtle.pencolor(colc0205392)
    turtle.forward(-hypo, colorNo)
    turtle.right(2*rotAngle)
    turtle.forward(hypo, colorNo)
    turtle.penup()
    turtle.left(rotAngle)
    col634f38d1 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.backward(h)
    turtle.pendown()
    turtle.pencolor(col634f38d1)

# Draws letter X in colour specified by colorNo with font height h 
# from the current turtle position. 
def letterX(h, colorNo) :
    width = h/2.0
    hypo = math.sqrt(width*width + h*h)
    rotAngle = math.degrees(math.atan(width/h))
    turtle.right(rotAngle)
    turtle.forward(hypo, colorNo)
    turtle.penup()
    turtle.left(90+rotAngle)
    colf969049f = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(width)
    turtle.right(90-rotAngle)
    turtle.pendown()
    turtle.pencolor(colf969049f)
    turtle.forward(-hypo, colorNo)
    turtle.right(rotAngle)

# Draws letter Y in colour specified by colorNo with font height h 
# from the current turtle position. 
def letterY(h, colorNo) :
    width = h/2.0
    hypo = math.sqrt(width*width + h*h)/2.0
    rotAngle = math.degrees(math.atan(width/h))
    turtle.penup()
    colc492a008 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(h)
    turtle.left(rotAngle)
    turtle.pendown()
    turtle.pencolor(colc492a008)
    turtle.forward(-hypo, colorNo)
    turtle.right(rotAngle)
    turtle.penup()
    colb3bf845a = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.backward(h/2.0)
    turtle.pendown()
    turtle.pencolor(colb3bf845a)
    turtle.forward(h/2.0, colorNo)
    turtle.right(rotAngle)
    turtle.forward(hypo, colorNo)
    turtle.left(rotAngle)
    turtle.penup()
    col4b25bc6b = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.backward(h)
    turtle.pendown()
    turtle.pencolor(col4b25bc6b)

# Draws letter Z in colour specified by colorNo with font height h 
# from the current turtle position. 
def letterZ(h, colorNo) :
    width = h/2.0
    hypo = math.sqrt(width*width + h*h)
    rotAngle = math.degrees(math.atan(width/h))
    turtle.penup()
    col8153cdbf = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(h)
    turtle.right(90)
    turtle.pendown()
    turtle.pencolor(col8153cdbf)
    turtle.forward(width, colorNo)
    turtle.left(90-rotAngle)
    turtle.forward(-hypo, colorNo)
    turtle.right(90-rotAngle)
    turtle.forward(width, colorNo)
    turtle.left(90)

# Draws nEdges edges of a regular n-polygon with edge length a 
# counter-clockwise, if ctrclkws is true, or clockwise if ctrclkws is false. 
def polygonPart(a, n, ctrclkws, nEdges, color) :
    rotAngle = 360.0/n
    if (ctrclkws):
        rotAngle = -rotAngle

    for k in range(1, nEdges+1, 1):
        turtle.right(rotAngle)
        turtle.forward(a, color)


# Draws a dummy character (small centered square) with font height h and 
# the colour encoded by colorNo 
def charDummy(h, colorNo) :
    width = h / 2.0
    # Octagon edge length (here: edge lengzh of the square) 
    b = width / (math.sqrt(2.0) + 1)
    # Cathetus of the corner triangle outside the octagon 
    c = (width - b) / 2.0
    d = b / math.sqrt(2.0)
    turtle.penup()
    colfb81f47b = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(h/2.0-b/2.0)
    turtle.right(90)
    turtle.forward(c)
    turtle.right(90)
    turtle.pendown()
    turtle.pencolor(colfb81f47b)
    # Draws the square with edge length b 
    polygonPart(b, 4, true, 4, colorNo)
    turtle.penup()
    turtle.left(90)
    col1c4d3c74 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(b + c)
    turtle.left(90)
    turtle.backward(h/2.0-b/2.0)
    turtle.pendown()
    turtle.pencolor(col1c4d3c74)

# Draws a comma in colour specified by colorNo with font height h 
# from the current turtle position. 
def comma(h, colorNo) :
    # Achteck-Kantenlänge 
    b = h * 0.5 / (math.sqrt(2.0) + 1)
    # Eckenlänge außen am Achteck 
    c = b / math.sqrt(2.0)
    rotAngle = math.degrees(math.atan(0.5))
    hypo = c * math.sqrt(1.25)
    turtle.penup()
    turtle.right(90)
    col98392fcd = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward((c+b)/2.0 + c)
    turtle.pendown()
    turtle.pencolor(col98392fcd)
    # Counterclockwise draw 3 edges of a square with edge length c 
    # in the colour endcoded by colorNo 
    polygonPart(c, 4, true, 3, colorNo)
    turtle.left(90)
    turtle.forward(c/2.0, colorNo)
    turtle.right(90)
    turtle.forward(c, colorNo)
    turtle.left(180 - rotAngle)
    turtle.forward(hypo, colorNo)
    turtle.penup()
    turtle.right(90 - rotAngle)
    col4dbf2995 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward((c + b)/2.0)
    turtle.left(90)
    turtle.pendown()
    turtle.pencolor(col4dbf2995)

# Draws an exclamation mark in the colour encoded by colorNo with font height h 
# from the current turtle position. 
def exclMk(h, colorNo) :
    # Achteck-Kantenlänge 
    b = h * 0.5 / (math.sqrt(2.0) + 1)
    # Eckenlänge außen am Achteck 
    c = b / math.sqrt(2.0)
    width = h/2.0
    length1 = h - (b+c)/2.0
    length2 = length1 - 2*c
    hypo = math.sqrt(width*width/16.0 + length2*length2)
    # 360°/8 
    rotAngle = 45
    rotAngle2 = math.degrees(math.atan(width/4.0/length2))
    turtle.penup()
    col8a2c5c32 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(length1)
    turtle.right(90)
    turtle.forward(width/2.0)
    turtle.left(90 + rotAngle)
    turtle.pendown()
    turtle.pencolor(col8a2c5c32)
    # Clockwise draw 5 edges of an octagon with edge length b/2 
    # in the colour endcoded by colorNo 
    polygonPart(b/2.0, 8, false, 5, colorNo)
    turtle.right(rotAngle2)
    turtle.forward(hypo, colorNo)
    turtle.left(2*rotAngle2)
    turtle.forward(-hypo, colorNo)
    turtle.penup()
    col349e8c59 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(hypo)
    turtle.right(rotAngle2)
    turtle.forward(c)
    turtle.left(90)
    turtle.forward(c/2.0)
    turtle.pendown()
    turtle.pencolor(col349e8c59)
    # Counterclockwise draw all 4 edges of a squarfe with edge length c 
    # in the colour endcoded by colorNo 
    polygonPart(c, 4, false, 4, colorNo)
    turtle.penup()
    col84bb9f06 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward((c + b)/2.0)
    turtle.left(90)
    turtle.backward(c)
    turtle.pendown()
    turtle.pencolor(col84bb9f06)

# Draws a full stop in colour specified by colorNo with font height h 
# from the current turtle position. 
def fullSt(h, colorNo) :
    # Achteck-Kantenlänge 
    b = h * 0.5 / (math.sqrt(2.0) + 1)
    # Eckenlänge außen am Achteck 
    c = b / math.sqrt(2.0)
    turtle.penup()
    turtle.right(90)
    col999bb7f0 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward((c+b)/2.0 + c)
    turtle.pendown()
    turtle.pencolor(col999bb7f0)
    # Counterclockwise draw all 4 edges of a squarfe with edge length c 
    # in the colour endcoded by colorNo 
    polygonPart(c, 4, true, 4, colorNo)
    turtle.penup()
    col47d03850 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward((c + b)/2.0)
    turtle.left(90)
    turtle.pendown()
    turtle.pencolor(col47d03850)

# Draws letter B in colour specified by colorNo with font height h 
# from the current turtle position. 
def letterB(h, colorNo) :
    # Octagon edge length 
    b = h * 0.5 / (math.sqrt(2.0) + 1)
    # Cathetus of the outer corner triangle of the octagon 
    c = b / math.sqrt(2.0)
    turtle.forward(h, colorNo)
    turtle.right(90)
    turtle.forward(c+b, colorNo)
    # Clockwise draw 4 edges of an octagon with edge length b 
    polygonPart(b, 8, false, 4, colorNo)
    turtle.forward(c, colorNo)
    turtle.penup()
    turtle.left(180)
    col9bc9c949 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(b + c)
    turtle.pendown()
    turtle.pencolor(col9bc9c949)
    # Clockwise draw 4 edges of an octagon with edge length b 
    polygonPart(b, 8, false, 4, colorNo)
    turtle.forward(c, colorNo)
    turtle.penup()
    turtle.left(180)
    col61837cd4 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(b + 2*c)
    turtle.pendown()
    turtle.pencolor(col61837cd4)
    turtle.left(90)

# Draws letter C in the colour encoded by colorNo with font height h 
# from the current turtle position. 
def letterC(h, colorNo) :
    # Octagon edge length 
    b = h * 0.5 / (math.sqrt(2.0) + 1)
    # Cathetus of the outer trinagle at the octagon corner 
    c = b / math.sqrt(2.0)
    # 360°/8 
    rotAngle = 45
    turtle.penup()
    col2feefdf = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(c)
    turtle.pendown()
    turtle.pencolor(col2feefdf)
    turtle.right(180)
    # Clockwise draws 3 edges of an octagon with edge length b in the colour 
    # encoded by colorNo 
    polygonPart(b, 8, true, 3, colorNo)
    turtle.left(rotAngle)
    turtle.penup()
    colf84191c = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(2*b + 2*c)
    turtle.pendown()
    turtle.pencolor(colf84191c)
    # Counterclockwise draws 4 edges of an octagon with edge length b 
    # iin the colour encoded by colorNo 
    polygonPart(b, 8, true, 4, colorNo)
    turtle.forward(b + 2*c, colorNo)
    turtle.penup()
    col8f240550 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(c)
    turtle.left(90)
    turtle.pencolor(col8f240550)
    turtle.forward(b + 2*c, colorNo)
    turtle.pendown()
    turtle.left(90)

# Draws letter D in colour specified by colorNo with font height h 
# from the current turtle position. 
def letterD(h, colorNo) :
    # Achteck-Kantenlänge 
    b = h * 0.5 / (math.sqrt(2.0) + 1)
    # Eckenlänge außen am Achteck 
    c = b / math.sqrt(2.0)
    turtle.forward(h, colorNo)
    turtle.right(90)
    turtle.forward(c+b, colorNo)
    # Clockwise draw 2 edges of an octagon with edge length b in the colour 
    # encoded by colorNo 
    polygonPart(b, 8, false, 2, colorNo)
    turtle.forward(b + 2*c, colorNo)
    # Clockwise draw 2 edges of an octagon with edge length b in the colour 
    # encoded by colorNo 
    polygonPart(b, 8, false, 2, colorNo)
    turtle.forward(c, colorNo)
    turtle.penup()
    turtle.left(180)
    col870b36dd = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(b + 2*c)
    turtle.pendown()
    turtle.pencolor(col870b36dd)
    turtle.left(90)

# Draws letter G in colour specified by colorNo with font height h 
# from the current turtle position. 
def letterG(h, colorNo) :
    # Octagon edge length 
    b = h * 0.5 / (math.sqrt(2.0) + 1)
    # Cathetus of the corner triangle outside the octagon. 
    c = b / math.sqrt(2.0)
    turtle.penup()
    col733da46a = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(c)
    turtle.pendown()
    turtle.pencolor(col733da46a)
    turtle.right(180)
    # Counterclockwise draw 4 edges of an octagon with edge length b in 
    # the colour encoded by colorNo 
    polygonPart(b, 8, true, 4, colorNo)
    turtle.forward(c, colorNo)
    turtle.left(90)
    turtle.forward(b/2.0 + c, colorNo)
    turtle.penup()
    colbcd75c8 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.backward(b/2.0 + c)
    turtle.right(90)
    turtle.forward(b + c)
    turtle.pendown()
    turtle.pencolor(colbcd75c8)
    # Counterclockwise draw 4 edges of an octagon with edge length b in 
    # the colour encoded by colorNo 
    polygonPart(b, 8, true, 4, colorNo)
    turtle.forward(b + 2*c, colorNo)
    turtle.penup()
    cola8ccd51f = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(c)
    turtle.left(90)
    turtle.pencolor(cola8ccd51f)
    turtle.forward(b + 2*c, colorNo)
    turtle.pendown()
    turtle.left(90)

# Draws letter J in colour encoded by colorNo with font height h 
# from the current turtle position. 
def letterJ(h, colorNo) :
    # Achteck-Kantenlänge 
    b = h * 0.5 / (math.sqrt(2.0) + 1)
    # Eckenlänge außen am Achteck 
    c = b / math.sqrt(2.0)
    # 360°/8 
    rotAngle = 45
    turtle.penup()
    colb8f10d88 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(c)
    turtle.pendown()
    turtle.pencolor(colb8f10d88)
    turtle.right(180)
    # Counterclockwise draw 3 edges of an octagon with edge length b in 
    # the colour encoded by colorNo 
    polygonPart(b, 8, true, 3, colorNo)
    turtle.left(rotAngle)
    turtle.forward(h - c, colorNo)
    turtle.penup()
    col12596e70 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.backward(h)
    turtle.pendown()
    turtle.pencolor(col12596e70)

# Draws letter O in colour specified by colorNo with font height h 
# from the current turtle position. 
def letterO(h, colorNo) :
    # Octagon edge length 
    b = h * 0.5 / (math.sqrt(2.0) + 1)
    # Cathetus of the corner triangle outside the octagon 
    c = b / math.sqrt(2.0)
    turtle.penup()
    col76418d5f = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(c)
    turtle.pendown()
    turtle.pencolor(col76418d5f)
    turtle.right(180)
    # Counterclockwise draw 4 edges of an octagon with edge length b 
    # in the colour endcoded by colorNo 
    polygonPart(b, 8, true, 4, colorNo)
    turtle.forward(b + 2*c, colorNo)
    # Counterclockwise draw 4 edges of an octagon with edge length b 
    # in the colour endcoded by colorNo 
    polygonPart(b, 8, true, 4, colorNo)
    turtle.forward(b + 2*c, colorNo)
    turtle.penup()
    col5864ac9e = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(c)
    turtle.left(90)
    turtle.forward(b + 2*c)
    turtle.pendown()
    turtle.pencolor(col5864ac9e)
    turtle.left(90)

# Draws letter P in colour specified by colorNo with font height h 
# from the current turtle position. 
def letterP(h, colorNo) :
    # Octagon edge length 
    b = h * 0.5 / (math.sqrt(2.0) + 1)
    # Cathetus of the corner triangle outside the octagon 
    c = b / math.sqrt(2.0)
    turtle.forward(h, colorNo)
    turtle.right(90)
    turtle.forward(c+b, colorNo)
    # Clockwise draw 4 edges of an octagon with edge length b 
    # in the colour endcoded by colorNo 
    polygonPart(b, 8, false, 4, colorNo)
    turtle.forward(c, colorNo)
    turtle.penup()
    col20e8daa4 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.backward(b + 2*c)
    turtle.left(90)
    turtle.forward(b + 2*c)
    turtle.pendown()
    turtle.pencolor(col20e8daa4)
    turtle.left(180)

# Draws letter Q in colour specified by colorNo with font height h 
# from the current turtle position. 
def letterQ(h, colorNo) :
    # Achteck-Kantenlänge 
    b = h * 0.5 / (math.sqrt(2.0) + 1)
    # Eckenlänge außen am Achteck 
    c = b / math.sqrt(2.0)
    # 360°/8 
    rotAngle = 45
    turtle.penup()
    colddde07d5 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(c)
    turtle.pendown()
    turtle.pencolor(colddde07d5)
    turtle.right(180)
    # Counterclockwise draw 4 edges of an octagon with edge length b 
    # in the colour endcoded by colorNo 
    polygonPart(b, 8, true, 4, colorNo)
    turtle.forward(b + 2*c, colorNo)
    # Counterclockwise draw 4 edges of an octagon with edge length b 
    # in the colour endcoded by colorNo 
    polygonPart(b, 8, true, 4, colorNo)
    turtle.forward(b + 2*c, colorNo)
    turtle.penup()
    col24fe30c1 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(c)
    turtle.left(90)
    turtle.forward(b + 2*c)
    turtle.pencolor(col24fe30c1)
    turtle.right(rotAngle)
    colf154c574 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.backward(b)
    turtle.pendown()
    turtle.pencolor(colf154c574)
    turtle.forward(b, colorNo)
    turtle.left(90 + rotAngle)

# Zeichnet den Buchstaben R von der Turtleposition aus 
# mit Zeilenhöhe h 
def letterR(h, colorNo) :
    # Achteck-Kantenlänge 
    b = h * 0.5 / (math.sqrt(2.0) + 1)
    # Eckenlänge außen am Achteck 
    c = b / math.sqrt(2.0)
    # 360°/8 
    rotAngle = 45
    turtle.forward(h, colorNo)
    turtle.right(90)
    turtle.forward(c+b, colorNo)
    # Clockwise draw 4 edges of an octagon with edge length b 
    # in the colour endcoded by colorNo 
    polygonPart(b, 8, false, 4, colorNo)
    turtle.forward(c, colorNo)
    turtle.left(90 + rotAngle)
    turtle.forward(math.sqrt(2.0)*(b + 2*c), colorNo)
    turtle.left(90 + rotAngle)

# Draws letter S in colour specified by colorNo with font height h 
# from the current turtle position. 
def letterS(h, colorNo) :
    # Achteck-Kantenlänge 
    b = h * 0.5 / (math.sqrt(2.0) + 1)
    # Eckenlänge außen am Achteck 
    c = b / math.sqrt(2.0)
    # 360°/8 
    rotAngle = 45
    turtle.penup()
    colc22195ed = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(c)
    turtle.pendown()
    turtle.pencolor(colc22195ed)
    turtle.right(180)
    # Counterclockwise draw 6 edges of an octagon with edge length b 
    # in the colour endcoded by colorNo 
    polygonPart(b, 8, true, 6, colorNo)
    # Clockwise draw 5 edges of an octagon with edge length b 
    # in the colour endcoded by colorNo 
    polygonPart(b, 8, false, 5, colorNo)
    turtle.right(rotAngle)
    turtle.penup()
    col56aea2ee = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(2*b + 3*c)
    turtle.pendown()
    turtle.pencolor(col56aea2ee)
    turtle.left(180)

# Draws letter U in colour specified by colorNo with font height h 
# from the current turtle position. 
def letterU(h, colorNo) :
    # edge length of a regular octagon 
    b = h * 0.5 / (math.sqrt(2.0) + 1)
    # Eckenlänge außen am Achteck 
    c = b / math.sqrt(2.0)
    # 360°/8 
    rotAngle = 45
    turtle.penup()
    colf9c2ed70 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(c)
    turtle.pendown()
    turtle.pencolor(colf9c2ed70)
    turtle.forward(h - c, colorNo)
    turtle.penup()
    col17833c87 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.backward(h-c)
    turtle.pendown()
    turtle.pencolor(col17833c87)
    turtle.right(180)
    # Counterclockwise draw 3 edges of an octagoin with edge length b in colour specified by colorNo 
    polygonPart(b, 8, true, 3, colorNo)
    turtle.left(rotAngle)
    turtle.forward(h - c, colorNo)
    turtle.penup()
    colb8cd8cf4 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.backward(h)
    turtle.pendown()
    turtle.pencolor(colb8cd8cf4)

# Draws a question mark in colour specified by colorNo with font height h 
# from the current turtle position. 
def qstnMk(h, colorNo) :
    # Achteck-Kantenlänge 
    b = h * 0.5 / (math.sqrt(2.0) + 1)
    # Eckenlänge außen am Achteck 
    c = b / math.sqrt(2.0)
    # 360°/8 
    rotAngle = 45
    turtle.penup()
    col181e7715 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(h-c)
    turtle.pendown()
    turtle.pencolor(col181e7715)
    # Counterclockwise draw 5 edges of an octagon with edge length b 
    # in the colour endcoded by colorNo 
    polygonPart(b, 8, false, 5, colorNo)
    turtle.forward(c, colorNo)
    turtle.left(rotAngle)
    turtle.forward(b/2.0, colorNo)
    turtle.penup()
    coldc6d9de1 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward(c)
    turtle.left(90)
    turtle.forward(c/2.0)
    turtle.pendown()
    turtle.pencolor(coldc6d9de1)
    # Counterclockwise draw all 4 edges of a squarfe with edge length c 
    # in the colour endcoded by colorNo 
    polygonPart(c, 4, false, 4, colorNo)
    turtle.penup()
    colfeb730e9 = turtle.pencolor(); turtle.pencolor("#000000")
    turtle.forward((c + b)/2.0)
    turtle.left(90)
    turtle.backward(c)
    turtle.pendown()
    turtle.pencolor(colfeb730e9)

# Has the turtle draw the given string 'text´ with font height 'h´ (in 
# pixels) and the colour coded by integer 'c´ from the current Turtle 
# position to the Turtle canvas. If the turtle looks North then 
# the text will be written rightwards. In the event, the turtle will be 
# placed behind the text in original orientation (such that the next text 
# would be written like a continuation. Colour codes: 
# 1 = black 
# 2 = red 
# 3 = yellow 
# 4 = green 
# 5 = cyan 
# 6 = blue 
# 7 = pink 
# 8 = grey 
# 9 = orange 
# 10 = violet 
# All letters (ASCII) will be converted to uppercase, digits cannot 
# be represented, the set of representable special characters is: 
# '.', ',', '!', '?'. Other characters will be shown as a small 
# centred square (dummy character). 
def drawText(text, h, c) :
    gap = h/10.0
    for k in range(1, length(text)+1, 1):
        letter = uppercase(copy(text, k, 1))
        if (letter == ","):
            comma(h,c)
        else:
            # "," cannot be chacked against because the comma is misinterpreted 
            # as selector list separator. 
            if ((letter) == "A") :
                letterA(h,c)
            elif ((letter) == "B") :
                letterB(h,c)
            elif ((letter) == "C") :
                letterC(h,c)
            elif ((letter) == "D") :
                letterD(h,c)
            elif ((letter) == "E") :
                letterE(h,c)
            elif ((letter) == "F") :
                letterF(h,c)
            elif ((letter) == "G") :
                letterG(h,c)
            elif ((letter) == "H") :
                letterH(h,c)
            elif ((letter) == "I") :
                letterI(h,c)
            elif ((letter) == "J") :
                letterJ(h,c)
            elif ((letter) == "K") :
                letterK(h,c)
            elif ((letter) == "L") :
                letterL(h,c)
            elif ((letter) == "M") :
                letterM(h,c)
            elif ((letter) == "N") :
                letterN(h,c)
            elif ((letter) == "O") :
                letterO(h,c)
            elif ((letter) == "P") :
                letterP(h,c)
            elif ((letter) == "Q") :
                letterQ(h,c)
            elif ((letter) == "R") :
                letterR(h,c)
            elif ((letter) == "S") :
                letterS(h,c)
            elif ((letter) == "T") :
                letterT(h,c)
            elif ((letter) == "U") :
                letterU(h,c)
            elif ((letter) == "V") :
                letterV(h,c)
            elif ((letter) == "W") :
                letterW(h,c)
            elif ((letter) == "X") :
                letterX(h,c)
            elif ((letter) == "Y") :
                letterY(h,c)
            elif ((letter) == "Z") :
                letterZ(h,c)
            elif ((letter) == " ") :
                blank(h,c)
            elif ((letter) == "!") :
                exclMk(h,c)
            elif ((letter) == "?") :
                qstnMk(h,c)
            elif ((letter) == ".") :
                fullSt(h,c)
            else:
                charDummy(h,c)

        turtle.right(90)
        turtle.penup()
        col83b874b2 = turtle.pencolor(); turtle.pencolor("#000000")
        turtle.forward(gap)
        turtle.pendown()
        turtle.left(90)
        turtle.pencolor(col83b874b2)


# Demo program for routine drawText() 
# Asks the user to enter a text, a wanted text height and colour, 
# and then draws this string onto the turtle screen. Places every 
# entered text to a new line. 
print("This is a demo program for text writing with Turleizer.", sep='')
turtle.showturtle()
turtle.pendown()
y = 0
while True:
    text = input("Enter some text (empty string to exit)")
    # Make sure the content is interpreted as string 
    text = "" + text
    if (text != ""):
        while True:
            height = input("Height of the text (pixels)")
            if height >= 5:
                break

        while True:
            colour = input("Colour (1=black, 2=red, 3=yellow, 4=green, 5=cyan, 6=blue, 7=pink, 8=gray, 9=orange, 10=violet)")
            if colour >= 1  and  colour <= 10:
                break

        y = y + height + 2
        turtle.goto(0, y - 2)
        drawText(text, height, colour)

    if text == "":
        break

turtle.goto(0, y + 15)
drawText("Thank you, bye.", 10, 4)
turtle.hideturtle()
# turtle.bye()	# TODO: re-enable this if you want to close the turtle window. 
