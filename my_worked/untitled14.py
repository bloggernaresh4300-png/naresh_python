# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 08:48:50 2026

@author: HP
"""

""" wap to give grades is the marks if greater than 85 then give a if between 50 to 85 then b 
if between 30 to 50 then c and less than c is fail"""

marks = int(input("Enter your marks: "))

if marks > 85:
    grade = "A"
elif marks >= 50 and marks <= 85:
    grade = "B"
elif marks >= 30 and marks < 50:
    grade = "C"
else:
    grade = "Fail"

print("Your grade is:", grade)

#%%
"""nested if else"""

a = 55

if a%3 == 0:
    if a%5 ==0:
        print("number is divisible by both")
    else:
        print("number is divisible by 3")
        
elif a%5 == 0:
    if a%3 == 0:
        print("number is divisible by both")
    else:
        print("number is divisible by 5")       
else:
      print("number is not divisible by both")       
        