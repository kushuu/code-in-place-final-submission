"""
File: word_guess.py
-------------------
Fill in this comment.
"""


import random


LEXICON_FILE = "Lexicon.txt"

def print_word(secret_word, guessed_alpha):
    ret_word = ""
    for char in secret_word:
        if char in guessed_alpha:
            ret_word += char
        else:
            ret_word += '-'
    return ret_word

def play_game(secret_word):
    INITIAL_GUESSES = 8
    guessed_alpha = []
    while INITIAL_GUESSES:
        updated_word = print_word(secret_word, guessed_alpha)
        if updated_word == secret_word:
            print("The guess is correct.")
            print("Congratulation, the word is:", secret_word)
            break
        print("The word now looks like this:", updated_word)
        print("You have {} guesses left".format(INITIAL_GUESSES))
        guess = input("Type a single letter here, then press enter: ").upper()
        guessed_alpha.append(guess)
        if guess not in secret_word:
            INITIAL_GUESSES -= 1
    if INITIAL_GUESSES == 0:
        print("Sorry, you lost. The secret word was:", secret_word)

def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    index = random.randrange(3)
    if index == 0:
        return 'HAPPY'
    elif index == 1:
        return 'PYTHON'
    else:
        return 'COMPUTER'


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)

    
if __name__ == "__main__":
    main()
