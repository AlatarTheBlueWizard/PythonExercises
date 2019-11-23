"""
A program that asks the user for a number and then 
prints out a list of all the divisors of that number. 

Author: Ryan Gale
Date: 10/23/2019
"""

num = int(input("Enter a number: "))
x = range(1, 51) # list ranging from 1 to 50

divisorList = []

print("Divisors of " + str(num) + ": ")
for elem in x:
    if num % elem == 0:
        divisorList.append(elem)
        divisorList.sort()
        print(divisorList)
