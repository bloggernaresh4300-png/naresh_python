# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 09:37:24 2026

@author: HP
"""

"""wap to find maximum among three no.s"""
# Program to find maximum among three numbers

# Taking input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Nested if-else logic
if a > b:
    if a > c:
        maximum = a
    else:
        maximum = c
else:
    if b > c:
        maximum = b
    else:
        maximum = c

print("The maximum number is:", maximum)

#%%

"""wap to print the minimum no. of notes to make a amount you have notes of 500, 100, 50,
 20, 10, 5, 2, and 1"""
 # Program to find minimum number of notes for a given amount

# Input amount
amount = int(input("Enter the amount: "))

# List of available denominations
denominations = [500, 100, 50, 20, 10, 5, 2, 1]

print("Minimum number of notes:")

for note in denominations:
    if amount >= note:
        count = amount // note   # Number of notes of this denomination
        amount = amount % note   # Remaining amount
        print(f"{note} : {count}")
