#Importing the random variable
import random

#Setting up the loop of the game
while True:
    
    #Introduction statement to the game
    print("Welcome to Hangman!")

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
    with open ("words.txt","r") as file:
        word_list = file.read().splitlines()
        chosen_word = random.choice(word_list)
        word_display = [" _ "] * len(chosen_word)
        print()

        #Game starts here
        print("Ready?")
        print()

        guessed_letter = set()

        while lives > 0 and " _ " in word_display:
            print("Word:","".join(word_display)) #Joins the "word:" statement with the underscores from the word display
            letter = input("Guess a Letter:") #Lets the user input a letter
            letter = letter.lower()

            #Checking whether the input contains 1 letter and is in the alphabet
            if len(letter) != 1 or not letter.isalpha():
                print("Please enter only a single letter (a-z)")
                print()
                continue

            #Decision making
            if letter in guessed_letter:
                print("You have already guessed that letter. Try again.")
                print()
                continue

            else:
                guessed_letter.add(letter)

            if letter in chosen_word:
                print("You have guessed a letter!")
                for i in range(len(chosen_word)):
                    if chosen_word[i] == letter:
                        word_display[i] = letter #This replaces the underscore with the guessed letter
                print()
            
            else:
                lives -= 1
                print("Incorrect! You have {} lives remaining." .format(lives))
                print()
        
            if " _ " not in word_display:
                print("Congratulations on guessing the word!! The word was:", chosen_word)
                print()
            
            if lives == 0 and " _ " in word_display:
                print("You have lost the game! The word was:", chosen_word) 
                print()

         #Asks the user if they want to play again
        play_again = input("Would you like to play again?").lower()

        if play_again != "yes": #If the user doesn't say yes, the game will automatically stop at this point.
            print("Thanks for playing!")
            break

        