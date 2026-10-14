# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 08:32:34 2026

@author: HP
"""
"""
wap to check whether a number is either divisible by  or 5 or by both """

a = 100

if a%3 == 0:
    print(" number is divisible by 3")
    
elif a%5 == 0:
    print(" number is divisible by 5")
      
elif a%5 == 0 and a%3 == 0:
     print(" number is divisible by both")
     
else:
     print(" number is not divisible by both")

#%%
     
a = 50

if a >= 85:
    print('A')
elif a>=50 and a<85:    
  print('B')
elif a>=30 and a<50:
    print('C')
else:
    print ('fail')   