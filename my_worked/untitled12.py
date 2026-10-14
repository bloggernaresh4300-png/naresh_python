# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 08:43:20 2026

@author: HP
"""

a = 10.5
if a%1==0:
    print(str(a) + " number is decimal")
else:
    print(str(a) + " number is non decimal")
    
#%%
# wap to swap a absolute number 
a = 100
if a<0:
   b = a*-1
   print("absolute value of " + str(a) + "is" + str(b))
else:
    b = a*1
    print("absolute value of " + str(a) + "is" + str(b))    
    
#%%
# wap to swap a 2 digit number (18 -> 81)
    
n = 18
tens = n//10
ones = n%10
swapped = ones*10+tens
print(swapped)

#%%
a = 18
quo = a//10
rem = a%10
print(rem*10+quo)