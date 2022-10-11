import random
import os
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


def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("WELCOME!")
    print("To select difficulty press: 'Y'")
    print("For rules press: 'R'")
    choice = input("> ")
    if choice == "y":
        difficulty()
    elif choice == "r":
        instructions()
    else:
        menu()


def difficulty():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Choose your difficulty: ")
    print("EASY")
    print("MEDIUM")
    print("HARD")
    global difficulty_level
    difficulty_level = input("> ")
    if difficulty_level == "easy":
        word = get_word()
        play(word)
    elif difficulty_level == "medium":
        word = get_word_medium()
        play_medium(word)
    elif difficulty_level == "hard":
        word = get_word_hard()
        play_hard(word)
    else:
        difficulty()


def instructions():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("RULES:")
    print("- Guess the word")
    print("- Each '_' shows a letter in the word")
    print("- You get 6 WRONG letter or word guesses before the man is hanged")
    print("- If you wish to go back to the main menu, type: 'MENU'")
    choice_one = input("> ")
    if choice_one == "menu":
        menu()


def get_word():
    word = random.choice(word_list)
    return word.upper()


def get_word_medium():
    word = random.choice(medium_words)
    return word.upper()


def get_word_hard():
    word = random.choice(hard_words)
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
            menu()
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
            word = get_word()
            play(word)
        elif choice_two == "n":
            menu()
    else:
        print("Sorry, you're out of tries. The word was: " + word + ".")
        print("Play again? (Y/N)")
        choice_three = input("> ")
        if choice_three == "y":
            word = get_word()
            play(word)
        elif choice_three == "n":
            menu()


def play_medium(words_medium):
    os.system('cls' if os.name == 'nt' else 'clear')
    word_completion = "_" * len(words_medium)
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
            elif guess not in words_medium:
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
                    words_medium) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(words_medium) and guess.isalpha():
            if guess in guessed_words:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("You already guessed the word", guess)
            elif guess != words_medium:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(guess, " is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = words_medium
        elif input() == "menu":
            menu()
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
            word = get_word_medium()
            play_medium(words_medium)
        elif choice_two == "n":
            menu()
    else:
        print("Sorry, you're out of tries. The word was: " + word + ".")
        print("Play again? (Y/N)")
        choice_three = input("> ")
        if choice_three == "y":
            word = get_word_medium()
            play_medium(words_medium)
        elif choice_three == "n":
            menu()


def play_hard(words_hard):
    os.system('cls' if os.name == 'nt' else 'clear')
    word_completion = "_" * len(words_hard)
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
            elif guess not in words_hard:
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
                    words_hard) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(words_hard) and guess.isalpha():
            if guess in guessed_words:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("You already guessed the word", guess)
            elif guess != words_hard:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(guess, " is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = words_hard
        elif input() == "menu":
            menu()
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
            word = get_word_hard()
            play_hard(words_hard)
        elif choice_two == "n":
            menu()
    else:
        print("Sorry, you're out of tries. The word was: " + word + ".")
        print("Play again? (Y/N)")
        choice_three = input("> ")
        if choice_three == "y":
            word = get_word_medium()
            play_medium(words_hard)
        elif choice_three == "n":
            menu()


def main():
    menu()


if __name__ == "__main__":
    main()