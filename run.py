import random
import os
from words import word_list
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


def display_hangman(tries):
    stages = ["""
                  --------
                  |      |
                  |      O
                  |     \|/
                  |      |
                  |     / \
                  -
                """,
                """
                  --------
                  |      |
                  |      O
                  |     \|/
                  |      |
                  |     / 
                  -
                """,

                """
                  --------
                  |      |
                  |      O
                  |     \|/
                  |      |
                  |     
                  -
                """,

                """
                  --------
                  |      |
                  |      O
                  |     \|
                  |      |
                  |     
                  -
                """,

                """
                  --------
                  |      |
                  |      O
                  |      |
                  |      |
                  |     
                  -
                """,

                """
                  --------
                  |      |
                  |      O
                  |      
                  |      
                  |     
                  -
                """,

                """
                  --------
                  |      |
                  |      
                  |      
                  |      
                  |     
                  -
                """]
    return stages[tries]


def menu():
    print("WELCOME! To start press: 'Y'")
    print("For rules press: 'R'")
    if input() == "y":
        word = get_word()
        play(word)
        while input("Play again? (Y/N) ").upper() == "Y":
            word = get_word()
            play(word)
    elif input() == "r":
        instructions()
    else:
        print("Wrong input.")


def instructions():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("RULES:")
    print("- Guess the word (each '-' under the hanging area shows how many letters is in the word)")
    print("- You get 6 WRONG letter or word guesses before the man is hanged")
    print("- If you wish to go back to the main menu, type: 'MENU'")



def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    os.system('cls' if os.name == 'nt' else 'clear')
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Well done, ", guess, "is correct!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(
                    word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("You already guessed the word", guess)
            elif guess != word:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(guess, " is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        elif input() == "menu":
            os.system('cls' if os.name == 'nt' else 'clear')
            menu()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congratulations, you guessed correctly! You WIN!")
    else:
        print("Sorry, you're out of tries. The word was: " + word + ".")


def main():
    menu()


if __name__ == "__main__":
    main()