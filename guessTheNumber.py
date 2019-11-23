"""
This program selects a random number which the
user has to guess, once the correct number is
guessed the program terminates and displays the
number as well as the number of guesses.

Author: Ryan Gale
Date: 11/23/2019
"""
import random #used to generate a random number

guess = 0 #guess attempt counter
rand_num = random.randint(1, 9) #generates a random number including 1-9

#loop to allow multiple guesses
while rand_num:
    user_num = int(input("Enter a number: "))
    if user_num < rand_num:
        guess += 1
        print("Number is too low!")
    elif user_num > rand_num:
        guess += 1
        print("Number is too high!")
    elif user_num == rand_num:
        print("Correct! the number is: " + str(rand_num))
        break

print("Number of attempted guesses: " + str(guess))
