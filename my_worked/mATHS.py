# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 09:17:13 2026

@author: HP
"""

#wap to reverse a 3 digit number (371 -> 173)
a = 173
rem_1 = a%10
quo_1 = a//100
rem_2 = (a//10)%10
print(rem_1*100+rem_2*10+quo_1)

#%%
import math
a = 1
b = -5
c = 6
d = b**2 - 4*a*c
if d > 0:
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d))/(2*a)
    print("Roots:",x1,x2)
elif d == 0:
    x = -b / (2*a)
else:
    print("complexroots") 
    