import random
from tkinter import Y

with open("wordlist.txt", "r") as p:
    words = p.readlines()

word = random.choice(words)[:-1]

allowed_errors = 9
guesses = []
done = False

while not done:
    for char in word:
        if char.lower() in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
    print("")

    guess = input(f"Errors left {allowed_errors}, Next guess: ")
    guesses.append(guess.lower())
    if guess not in word:
        allowed_errors -= 1
        if allowed_errors == 0:
            break

    done = True
    for char in word:
        if char.lower() not in guesses:
            done = False

if done:
    print("You found the right word: ", word)
else:
    print("##GAME OVER## \n the word was :", word)
