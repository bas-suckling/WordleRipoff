import random

def generateWordList():
    wordList = list()

    with open("words.csv", "r") as csv:
        for line in csv:
            currentline = line.split(",")
            for word in currentline:
                if word != '\n':
                    wordList.append(word)
    return wordList

def getNewWord(wordList): 
    return random.choice(wordList)



misplacedLetters = list()
incorrectLetters = list()
maximumGuesses = 5
currentGuess = 0
gameTitle = 'My Wordle Ripoff to Learn Python and RaspberryPi'

words = generateWordList()

print('Welcome to ', gameTitle)
print('Your object is to figure out the 5 letter word.')
print('You have ', maximumGuesses - currentGuess, ' guesses left.')
