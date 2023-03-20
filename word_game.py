# Name:  
# Student Number:  

# This file is provided to you as a starting point for the "word_game.py" program of Assignment 
# of CSP2151 in Semester 1, 2023.  It mainly provides you with a suitable list of words.
# Please use this file as the basis for your assignment work.  You are not required to reference it.

# Import the random module to allow us to select the word list and password at random.
import random


# This function receives two words as parameters should return the number of matching letters between them.
# See the assignment brief for details of this function's requirements.
def compareWords(word1, word2):
    """
    :param word1: the first word to compare
    :param word2: the second word to compare
    :return: the number of matching characters between the two words
    """
    count = 0
    for i in range(len(word1)):
        if word1[i] == word2[i]:
            count += 1
    return count


# Create a list of 100 words that are similar enough to work well for this game.
candidateWords = ['AETHER', 'BADGED', 'BALDER', 'BANDED', 'BANTER', 'BARBER', 'BASHER', 'BATHED', 'BATHER', 'BEAMED',
                  'BEANED', 'BEAVER', 'BECKET', 'BEDDER', 'BEDELL', 'BEDRID', 'BEEPER', 'BEGGAR', 'BEGGED', 'BELIES',
                  'BELLES', 'BENDED', 'BENDEE', 'BETTER', 'BLAMER', 'BLOWER', 'BOBBER', 'BOLDER', 'BOLTER', 'BOMBER',
                  'BOOKER', 'BOPPER', 'BORDER', 'BOSKER', 'BOTHER', 'BOWYER', 'BRACER', 'BUDGER', 'BUMPER', 'BUSHER',
                  'BUSIER', 'CEILER', 'DEADEN', 'DEAFER', 'DEARER', 'DELVER', 'DENSER', 'DEXTER', 'EVADER', 'GELDED',
                  'GELDER', 'HEARER', 'HEIFER', 'HERDER', 'HIDDEN', 'JESTER', 'JUDDER', 'KIDDED', 'KIDDER', 'LEANER',
                  'LEAPER', 'LEASER', 'LEVIED', 'LEVIER', 'LEVIES', 'LIDDED', 'MADDER', 'MEANER', 'MENDER', 'MINDER',
                  'NEATER', 'NEEDED', 'NESTER', 'PENNER', 'PERTER', 'PEWTER', 'PODDED', 'PONDER', 'RADDED', 'REALER',
                  'REAVER', 'REEDED', 'REIVER', 'RELIER', 'RENDER', 'SEARER', 'SEDGES', 'SEEDED', 'SEISER', 'SETTER',
                  'SIDDUR', 'TEENER', 'TEMPER', 'TENDER', 'TERMER', 'VENDER', 'WEDDER', 'WEEDED', 'WELDED', 'YONDER']

# The rest is up to you...
# See the assignment brief for details of the program requirements.

# Variable to store the number of guesses remaining
guessesRemaining = 4
# Variable to store whether the user has won or not
Won = False

# select 8 random words from candidateWords
wordList = random.sample(candidateWords, 8)

# select a random word from wordList
password = random.choice(wordList)

# Welcome message
print("Welcome to the Guess-The-Word Game.")
print("Password is one of these words:")

while guessesRemaining > 0 and not Won:
    # print the word list
    for i, word in enumerate(wordList):
        print(" " + str(i) + ") " + word)

    print("\nGuesses remaining: " + str(guessesRemaining))
    print("Guess (enter 0-7): ", end="")

    # get the user's guess
    guess = int(input())
    # check if the guess is valid
    if guess == 0 or guess == 1 or guess == 2 or guess == 3 or guess == 4 or guess == 5 or guess == 6 or guess == 7:
        print()
        print(wordList[guess])
        if wordList[guess] == password:
            print("Password Correct.")
            Won = True
        else:
            print("Password incorrect.")
            print(str(compareWords(wordList[guess], password)) + "/" + str(len(password)) + " correct.\n")
            guessesRemaining -= 1
    else:
        print("Invalid guess.")

if Won:
    print("Congratulations! You won")
else:
    print("You lost")
