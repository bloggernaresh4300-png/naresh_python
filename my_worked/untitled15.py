# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 09:18:52 2026

@author: HP
"""
"""asuming age of the computer is 25 and gender is male take the input from the user of age and
gender and establish whether computer will call you brother or you will call computer brother"""

computer_age = 25
computer_gender = "male"

# User input
user_age = int(input("Enter your age: "))
user_gender = input("Enter your gender (male/female): ").lower()

# Nested if-else logic
if user_gender == "male":
    if user_age > computer_age:
        print("Computer will call you Brother.")
    else:
        print("You will call Computer Brother.")
else:
    if user_gender == "female":
        if user_age > computer_age:
            print("Computer will call you Sister.")
        else:
            print("You will call Computer Brother (since computer is male).")
    else:
        print("Invalid gender entered.")
