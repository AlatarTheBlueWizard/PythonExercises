"""
Ask's the user for a string and prints out whether 
the string is a palindrome or not (read the same backwards)

Author: Ryan Gale
Date: 11/23/2019
"""

user_string = str(input("Enter a word: "))
reverse = user_string[::-1] # reverses the string 
print(reverse) #easy to spot if palindrome from here

if user_string == reverse:
    print("The word " + user_string + " is a palindrome!")
else:
    print("The word " + user_string + " is not a palindrome!")
