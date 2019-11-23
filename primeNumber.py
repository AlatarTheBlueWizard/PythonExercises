"""
Ask the user for a number and determine 
whether the number is prime or not.

Author: Ryan Gale
Date: 11/23/2019
"""

#function that checks if number is prime
def primeFunc():
    return int(input("Enter a number: "))

num = primeFunc()   #function call
if num % 2 != 0 and num % 3 != 0:
    print(str(num) + " is a prime number!")
else:
    print(str(num) + " is not a prime number!")
