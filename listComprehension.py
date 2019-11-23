"""
Write one line of Python that takes a list and 
makes a new list that has only the even elements 
of this list in it.

Author: Ryan Gale
Date: 11/23/2019
"""
import random #to generate a random list

start = 1
stop = 99
limit = 10

#random list for testing
list_a = [random.randint(start, stop) for i in range(limit)]

print("Randomly generated list: ")
print(list_a)

#seperates out even numbers in the generated list
even_num = [(x)for x in list_a if x % 2 == 0] #comprehensive even elements list

print("Even numbers from generated list: ")
print(even_num)
