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

while currentGuess < maximumGuesses :
    print('You have ', maximumGuesses - currentGuess, ' attempt(s) left.')
    userInput = input("What is your guess? ")
    lcUserInput = userInput.lower()
    if (not lcUserInput.isalpha()) or (len(lcUserInput) != 5):
        print('Invalid input')
    else:
        print ('Game logic goes here')
        currentGuess += 1







   