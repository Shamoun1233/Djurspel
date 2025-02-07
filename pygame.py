import time
import random

print("Welcome to Word Sprint.")
print("RULES: You have ten lifes, a life gets taken away as soon as you guess the letter wrong.")
print("If you guess the letter right you'll get a notification that tells you.")
print("Good luck!")

m = ("m")

y = ("y")

s = ("s")

t = ("t")

i = ("i")

c = ("c")




chanser = 10
poäng = 0

while True:
    fråga = str(input("Guess a letter:"))
    if fråga == m:
        print("You guessed the letter right!")
        print("The letter is: M")
        poäng += 1
    if fråga == y:
        print("You guessed the letter right!")
        print("The letter is: Y")
        poäng += 1
    if fråga == s:
        print("You guessed the letter right!")
        print("The letter is: S")
        poäng += 1
    if fråga == t:
        print("You guessed the letter right!")
        print("The letter is: T")
        poäng += 1
    if fråga == i:
        print("You guessed the letter right!")
        print("The letter is: I")
        poäng += 1
    if fråga == c:
        print("You guessed the letter right!")
        print("The letter is: C")
        poäng += 1
    if fråga not in ("m", "y", "s", "t", "i", "c" ):
        print("You have guessed the letter wrong, try again.")
        chanser -= 1  # Fix: -= instead of =-


    if poäng == 4:
        print("You have guessed the word! It was mystic.")
        
        time.sleep(5)
        break    
    
    
    if chanser == 0:
        print("You have no chances left..")
        
        time.sleep(5)
        break