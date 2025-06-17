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
    

        #Print statements that explains the rules of the game
        print()
        print("Here are the rules of the game:")
        print()
        print("You will be playing a round of trying to guess the word. You will be given 7 chances to guess the word.")
        print("You will type a letter that you think will be in the word. If the letter you've written is not in the word, you will be deducted 1 life.")
        print("We will reveal the word once you have guessed all the letters or if you have failed to guess the word.")
        print()
        print("Goodluck and Enjoy!")

        #Set up the number of lives
        lives = 7

        #Setting up the randomiser and the game setup
        word_list = ['tree','apple','banana','pepparoni','car','computer','chair','watch','milk','orange','circus','spaghetti']
        chosen_word = random.choice(word_list)
        def print_underscores(word):
            for letter in word:
                print(" _ ", end="") 
            print()

        #Game starts here
        print("Ready?")
        print()
        print_underscores(chosen_word)
        letter = input("Guess a Letter:")
        letter.lower

        #Decision making
        if letter in chosen_word:
            print("You have guessed a letter!")
        if letter not in chosen_word:
            print("Incorrect! You have {} lives remaining." .format(lives - 1))
            lives -= 1

    







    #This is for when the user want to exit the game.
    if continue_game == "no":
        print("All good! Let's play again next time!")
    break