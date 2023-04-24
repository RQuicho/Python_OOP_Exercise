"""Word Finder: finds random words from a dictionary."""

from random import *

class WordFinder:
    """Finds random word in text file.

    >>> wf = WordFinder("/Users/student/words.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    
    """

    def __init__(self, file_path):
        "Opens file and returns number of items read."
        words_file = open(file_path, "r")
        self.word = self.convert_file(words_file)
        print (f"{len(self.word)} words read.")


    def convert_file(self, words_file):
        "Converts items in file to a list of words."
        return [line.strip() for line in words_file] # removes any whitespace (/n) from each line
        

    def random(self):
        "Outputs a random word from the file."
        return choice(self.word)


class SpecialWordFinder(WordFinder):
	"""Uses WordFinder, but does not return blank lines or comments.

	>>> # Veggies	
    kale
    parsnips

    >>> # Fruits
    apple
    mango
	"kale" or "apple" 

    >>> swf = SpecialWordFinder("complex.txt")
    3 words read.

    >>> swf.random()
    "kale"
	"""
	
	def convert_file(self, words_file):
		return [line.strip() for line in words_file if line.strip() and not line.startswith("#")]
        
        

       


    
