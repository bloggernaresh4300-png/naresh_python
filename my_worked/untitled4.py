# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 08:55:37 2026

@author: HP
"""
import turtle

t = turtle.Turtle()
t.speed(3)

# House base (square outline)
t.penup()
t.goto(-50, -100)   # bottom-left
t.pendown()
t.goto(50, -100)    # bottom-right
t.goto(50, 0)       # top-right
t.goto(-50, 0)      # top-left
t.goto(-50, -100)   # back to bottom-left

# Roof (triangle outline)
t.goto(0, 80)       # roof peak
t.goto(50, 0)       # top-right
t.goto(-50, 0)      # top-left
t.goto(0, 80)       # back to peak

# Door (rectangle outline)
t.penup()
t.goto(-15, -100)   # bottom-left of door
t.pendown()
t.goto(15, -100)    # bottom-right
t.goto(15, -40)     # top-right
t.goto(-15, -40)    # top-left

