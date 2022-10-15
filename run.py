import random
import os
import time
from words import word_list
from words_medium import medium_words
from words_hard import hard_words


def display_hangman(tries):
    stages = ["""
                  --------
                  |      |
                  |      O
                  |     \|/
                  |      |
                  |     / |
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


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    """This function creates the main menu"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(""" 
        |   |   / \   |\  |  / -- \   /\  /\     / \   |\  |
        |---|  / - \  | \ | |   ¬__  /  \/  \   / - \  | \ | 
        |   | /     \ |  \|  \_ _ / /        \ /     \ |  \|
    """)
    print("\n")
    print("WELCOME!")
    print("\n")
    print("To select difficulty press: 'Y'")
    print("For rules press: 'R'")
    choice = input("> ")
    if choice == "y":
        clear()
        difficulty()
    elif choice == "r":
        clear()
        instructions()
    else:
        menu()


def difficulty():
    """This function enables the user to select their difficulty level"""
    print("Choose your difficulty: ")
    print("EASY")
    print("MEDIUM")
    print("HARD")
    difficulty_level = input("> ")
    if difficulty_level.lower() == "easy":
        word = get_word(word_list)
        play(word, difficulty_level)
    elif difficulty_level.lower() == "medium":
        word = get_word(medium_words)
        play(word, difficulty_level)
    elif difficulty_level.lower() == "hard":
        word = get_word(hard_words)
        play(word, difficulty_level)
    else:
        print("Please select a valid option!")
        time.sleep(2)
        clear()
        difficulty()


def instructions():
    """This function shows the rules to the game"""
    print("RULES:")
    print("- Guess the word")
    print("- Each '_' shows a letter in the word")
    print("- You get 6 WRONG letter or word guesses before the man is hanged")
    input("- Press ENTER to continue")
    clear()
    menu()



def get_word(list):
    """This function supplies the words for the 'EASY' difficulty"""
    word = random.choice(list)
    return word.upper()


def play(word, diff):
    """This function starts the EASY game"""
    os.system('cls' if os.name == 'nt' else 'clear')
    difficulty = diff
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
        if guess == "MENU":
            clear()
            menu()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                os.system('cls' if os.name == 'nt' else 'clear')
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
                os.system('cls' if os.name == 'nt' else 'clear')
                guessed = True
                word_completion = word
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congratulations, you guessed correctly! You WIN!")
        print("Play again? (Y/N)")
        choice_two = input("> ")
        if choice_two == "y":
            if difficulty == "easy":
                play(get_word(word_list), "easy")
            elif difficulty == "medium":
                play(get_word(medium_words), "medium")
            elif difficulty == "hard":
                play(get_word(hard_words), "hard")
        elif choice_two == "n":
            menu()
    else:
        print("Sorry, you're out of tries. The word was: " + word + ".")
        print("Play again? (Y/N)")
        choice_three = input("> ")
        if choice_three == "y":
            if difficulty == "easy":
                play(get_word(word_list), "easy")
            elif difficulty == "medium":
                play(get_word(medium_words), "medium")
            elif difficulty == "hard":
                play(get_word(hard_words), "hard")
        elif choice_three == "n":
            menu()


def main():
    menu()


if __name__ == "__main__":
    main()