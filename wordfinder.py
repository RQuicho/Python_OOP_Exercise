"""Word Finder: finds random words from a dictionary."""

from random import *

class WordFinder:
    """Finds random word in text file."""

    def __init__():
        "Gives a random word from the words.txt file."
        # self.find = find

    def __repr__():
        "Shows representation."
        return "Word Finder"
        # return f"<Word Finder find={self.find}>"

    def get_random_word():
        "Opens words.txt file and gets a random word."
        words_file = open("words.txt", "r")
        stripped_words_file = [line.strip() for line in words_file]
        word = choice(stripped_words_file)
        return word
        
        # file = open("words.txt", "r")
        # file = file.read()
        # new_word = choice(list(file))
        # # file.close()
       


    
