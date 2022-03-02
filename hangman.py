# Name:
# MIT Username: 
# 6.149 Project 1: Hangman
# hangman.py

# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *
import os
# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words
os.chdir("Downloads/")
WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print ("  ", len(wordlist), "words loaded.")
    print ("Enter play_hangman() to play a game of hangman!")
    return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    return word

# end of helper code
# -----------------------------------


# CONSTANTS
MAX_GUESSES = 6

# From par:
def is_word_guessed(secret_word, letters_guessed):
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''

    ####### YOUR CODE HERE ######
    #pass # This tells your code to skip this function; delete it when you
         # start working on this function
    for i in secret_word:
        if i in letters_guessed:
            continue
        else:
            return False
    return True

def print_guessed(secret_word, letters_guessed):
    '''
    Prints a string that contains the word with a dash "-" in
    place of letters not guessed yet. 
    '''
    
    ####### YOUR CODE HERE ######
    #pass # This tells your code to skip this function; delete it when you
         # start working on this function
    output = []
    for i in secret_word:
        if i in letters_guessed:
            output.append(i)
        else:
            output.append("-")
    output_string = "".join(output)
    print(output_string)


def play_hangman():
    # Actually play the hangman game
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0
    secret_word = 'claptrap'
    letters_guessed = []
    # Update secret_word. Don't uncomment this line until you get to Step 8.
    # secret_word  = get_word()

    ####### YOUR CODE HERE ######
    return None