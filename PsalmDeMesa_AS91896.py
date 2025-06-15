#Importing the random variable
import random

#Setting up the loop of the game
while True:

    #Ask user input for name and Print a welcome statement
    name = input("What is your name?")
    
    print("Welcome to Hangman, {}!" .format(name))

    #Ask user input if they want to continue or exit the game
    continue_game = input("Would you like to continue the game? (yes/no)")

    if continue_game == "yes":
        #Set up the number of lives
        lives = 7

        #Print statements that explains the rules of the game
        print("Here are the rules of the game:")
        print()
        print("You will be playing a round of trying to guess the word. You will be given 7 chances to guess the word.")
        print("We will reveal the word once you have guessed all the letters or if you have failed to guess the word.")
        print()
        print("Goodluck and Enjoy!")





    if continue_game == "no":
        print("All good! Let's play again next time!")
    break