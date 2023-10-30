# Importing libraries
import random

# Creating dictionary of words
words = {1: 'India', 2: 'Britain', 3: 'Python', 4: 'Ruby', 5: 'Jaguar', 6: 'Nissan', 7: 'Mustang'}

# Variable which stores a different word from dictionary each run
word = words[random.randint(1, len(words))]

print(word)
lives = 10
found = False
lettersguessed = ''

while not found and lives > 0:
    for char in word:
        print('_', end='')
    print()
    userguess = input("Enter a character: ")
    lettersguessed += userguess
    print(lettersguessed)
    # Checks if user input is a letter
    if userguess.isalpha():
        if userguess in word:
            for char in word:
                if word in lettersguessed:
                    print(char,end='')
                else:
                    print('_',end='')
        else:
            lives -= 1
            print("Wrong guess mate")
    else:
        print("Please enter letters only")

    print(f"You have {lives} lives left")
