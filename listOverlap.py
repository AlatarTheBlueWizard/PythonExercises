"""
A program that returns a list that contains only 
the elements that are common between the lists

Author: Ryan Gale
Date: 11/23/2019
"""
import random   #to generate random lists

#variables for randint() parameters and limit for lists
start = 1
stop = 99
limit = 10

#two random lists generated for testing
list_a = [random.randint(start, stop) for iter in range(limit)]
list_b = [random.randint(start, stop) for iter in range(limit)]

#print lists so user can see for themself common elements 
print(list_a)
print(list_b)

common_list = []

for x in range(len(list_a)):
    for y in range(len(list_b)):
        if list_a[x] == list_b[y]:
            common_list.append(list_a[x])
            common_list.sort()

#output new list with common elements
print("Common elements between lists are: " + str(common_list))
