import random
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
    print("WELCOME! To start press 'Y': ")
    if input() == "y":
        word = get_word()
        play(word)
        while input("Play again? (Y/N) ").upper() == "Y":
            word = get_word()
            play(word)
    elif input() == "n":
        print("Okay, we can wait here for a bit...")
    else:
        print("Wrong input.")


def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
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
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
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
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, " is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        elif input() == "restart":
            play(word)
        else:
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