"""
A program that prints out all the elements of a 
list that are less than 5.

Author: Ryan Gale
Date: 11/23/2019
"""
myList = [1, 4, 3, 2, 5, 6, 10, 21, 32, 16, 9, 900, 2100]
newList = []

for x in myList:
    if x < 5:
        #extra: add nums less than 5 to new list and display
        newList.append(x)
        newList.sort()
        print(newList)

#extra: enter a number and return elements of 
# original list smaller than number inputted
listForNumCheck = []
num = int(input("Enter a number: "))
for y in myList:
    if y < num:
        listForNumCheck.append(y)
        myList.sort()
        print(listForNumCheck)
