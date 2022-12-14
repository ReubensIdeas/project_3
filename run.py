import random
import os
import sys
import time
from words import word_list
from words_medium import medium_words
from words_hard import hard_words


def display_hangman(tries):
    """This function supplies each stage of the hangman process"""
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


def exit_game():
    """This method exits the game"""
    sys.exit()


def clear():
    """This method clears the terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    """This function creates the main menu"""
    clear()
    print(""" 
        |   |   / \   |\  |  / -- \   /\  /\     / \   |\  |
        |---|  / - \  | \ | |   ??__  /  \/  \   / - \  | \ | 
        |   | /     \ |  \|  \_ _ / /        \ /     \ |  \|
    """)
    print("\n")
    print("WELCOME!")
    print("\n")
    print("To exit the game at any time, type 'exit'")
    print("To go back to the menu at anytime, type 'menu'")
    print("\n")
    print("To select difficulty press: 'S'")
    print("For rules press: 'R'")
    choice = input("> ")
    if choice == "s":
        clear()
        difficulty()
    elif choice == "r":
        clear()
        instructions()
    elif choice == "exit":
        exit_game()
    else:
        print("Please select a valid option!")
        time.sleep(2)
        clear()
        menu()


def difficulty():
    """This function enables the user to select their difficulty level"""
    print("Choose your difficulty: ")
    print("\n")
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
    elif difficulty_level == "menu":
        clear()
        menu()
    elif difficulty_level == "exit":
        exit_game()
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
    print("\n")
    print("- Type 'menu' for the main menu")
    print("- Type 'S' to select difficulty")
    print("- Type 'exit' to exit the game")
    main_screen = input("> ")
    if main_screen == 'menu':
        clear()
        menu()
    elif main_screen == "exit":
        exit_game()
    elif main_screen == "s":
        clear()
        difficulty()
    else:
        print("Please select a valid option!")
        time.sleep(2)
        clear()
        instructions()


def get_word(list):
    """This function supplies the words for the difficulty levels"""
    word = random.choice(list)
    return word.upper()


def play(word, diff):
    """This function starts the EASY game"""
    clear()
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
        guess = input(
            "Please guess a letter or word(or 'menu' for main menu): ").upper()
        if guess == "MENU":
            clear()
            menu()
        elif guess == "EXIT":
            exit_game()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                clear()
                print("You already guessed the letter", guess)
            elif guess not in word:
                clear()
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                clear()
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
                clear()
                print("You already guessed the word", guess)
            elif guess != word:
                clear()
                print(guess, " is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                clear()
                guessed = True
                word_completion = word
        else:
            clear()
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
            clear()
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
        else:
            clear()
            menu()


def main():
    menu()


if __name__ == "__main__":
    main()
