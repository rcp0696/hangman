# Importing libraries
import random

# Creating dictionary of words
words = {1: 'india', 2: 'britain', 3: 'python', 4: 'ruby', 5: 'jaguar', 6: 'nissan', 7: 'mustang'}

# Variable which stores a different word from dictionary each run
word = words[random.randint(1, len(words))]

print(word)
lives = 10
found = False
lettersguessed = ''
var = '_' * len(word)

while not found and lives > 0:
    userguess = input("Enter a character: ")
    lettersguessed += userguess
    # Checks if user input is a letter
    if userguess.isalpha():
        if len(userguess) == len(word):
            if userguess == word:
                print("Nicely done")
                found = True
            else:
                lives -= 1

        elif len(userguess) == 1:
            if userguess in word:
                for char in word:
                    if char in lettersguessed:
                        # Index of letter guessed in the final word
                        ind = word.index(userguess)
                        var = var[:ind] + userguess + var[ind + 1:]
                        if word.count(userguess) > 1:
                            for i in range(1, word.count(userguess)):
                                ind = word.index(userguess)
                                var = var[:ind] + userguess + var[ind + 1:]
            else:
                lives -= 1
                print("Wrong guess mate")
            print(var)
            if var == word:
                print("You Won! Well Done.")
                found = True

    else:
        print("Please enter letters only")

    print(f" You have {lives} lives left")
