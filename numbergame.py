# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 13:03:52 2024

@author: diyab
"""

from art import logo
import random 
def play_easy(number):
    i=10
    while i!=0:
        print(f"You have {i} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess<num:
            print("Too Low")
            i=i-1
        elif guess>num:
            print("Too high")
            i=i-1
        elif guess==num:
            print(f"You got it! The answer is : {guess}")
            break
    if(i==0):
        print("You've run out of guesses. Refresh the page to run again.")
def play_hard(number):
    i=5
    while i!=0:
        print(f"You have {i} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess<num:
            print("Too Low")
            i=i-1
        elif guess>num:
            print("Too high")
            i=i-1
        elif guess==num:
            print(f"You got it! The answer is : {guess}")
            break
    if(i==0):
        print("You've run out of guesses. Refresh the page to run again.")
print(logo)
print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100.")
num = random.randrange(1,101)  
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level=="easy":
    play_easy(num)
elif level=="hard":
    play_hard(num)
else:
    print("WRONG INPUT")

    

    
    
