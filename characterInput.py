"""
This exercise focuses on getting user input and manipulating 
strings based on that input as well. The user enters their age
and first name, then the program will tell them which year they
turn 100 years old.

Author: Ryan Gale
Date: 11/23/2019
"""

#variables to store name and age
name = input("Enter your first name: ")
age = int(input("Enter your age: ")) #make sure age is an int

if age < 100:
    year = str((2019-age) + 100)
    print("Hello " + name + " you will turn 100 years old in the year " + year)
    #extra, print messages as many times as age
    for x in range(age):
        print("I repeat, you will turn 100 years old in the year " + year)
elif age >= 100:
    print("Since you are " + str(age) + " years old, this no longer applies.")
