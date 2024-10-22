import random as random

# Reads the words.txt file.
with open('words.txt', 'r') as f:
    words = f.read()

# Gathers the words from the txt file and assigns a word to guess at random.
wordsList = words.rstrip().split()
RandomWord = random.choice(wordsList)
WordToGuess = list(RandomWord)

MaxTurns = 5
NumOfTurns = 0  

incorrect_letters = [] # incorrect letters
MisLetters = []  # Misplaced Letters


def letter_to_value(letter):  # Calculates the value of the letter
    return ord(letter.lower()) - 96



print("Welcome To Hangman's Guess, where you, the player, will guess the letters in the word.\n")
print("You will have 5 turns to guess what letters are in each word, each word consists of 5 letters.\n")

Show = ['_'] * len(WordToGuess)
print(Show)

while NumOfTurns < MaxTurns:
    guessed_letter = input("Enter a letter: ")  # Give player input

    if guessed_letter in WordToGuess:
        print("The letter '{}' is in the word!".format(guessed_letter))
        for i, letter in enumerate(WordToGuess):
            if letter == guessed_letter:
                Show[i] = guessed_letter
        print(Show)  # Print the updated Show list

        # Check if all letters in Show match the WordToGuess
        if all(Show[i] == WordToGuess[i] for i in range(len(WordToGuess))):
            print("Congratulations, you won!")
            break  # Exit the loop since the game is won

    else:

        incorrect_letters.append(guessed_letter)
        incorrect_letters.sort()  # Sort the list in alphabetical order

        NumOfTurns += 1  # Increase input
        print("Number of turns.", NumOfTurns)  # Print input
        print("The letters '{}' is not in the word.".format(incorrect_letters))

if NumOfTurns == MaxTurns:
    print("You have used up all your Turns, You Have lost!")