"""
This program will take a number input and will
display a certain message based on whether it is even
or odd using modulus.

Author: Ryan Gale
Date: 11/23/2019
"""

#number to input, make sure it is an int
number = int(input("Enter a number: "))

#using conditionals to identify if it is even or odd
if number % 2 == 0:
    print("The number " + str(number) + " is even!")
elif number % 2 != 0:
    print("The number " + str(number) + " is odd!")

#extra: if multiple of 4, print different message
if number % 4 == 0:
    print("This is a multiple of 4!")

#extra: two variables (check & num) if num divides into check evenly, display message
num = int(input("Enter number: "))
check = int(input("Enter check number to divide by: "))

if num % check == 0:
    print(str(num) + " divides into " + str(check) + " evenly!")
else:
    print(str(num) + " does not divide into " + str(check) + " evenly!")
