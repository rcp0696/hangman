# Importing libraries
import random
from math import *

# Creating dictionary of words
words = {1: 'India', 2: 'Britain', 3: 'Python', 4: 'Ruby'}

# Variable which stores a different word from dictionary each run
word = words[random.randint(1, len(words))]

print(word)

print("Hi")
