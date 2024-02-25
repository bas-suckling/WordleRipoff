import random

def generateWordList():
    wordList = list()

    with open("words.csv", "r") as csv:
        for line in csv:
            currentline = line.split(",")
            for word in currentline:
                if word != '\n':
                    wordList.append(word.lower())
    return wordList

def getNewWord(wordList): 
    return random.choice(wordList)

misplacedLetters = list()
incorrectLetters = list()
maximumGuesses = 5
currentGuess = 0
gameTitle = 'My Wordle Ripoff to Learn Python and RaspberryPi'

words = generateWordList()
solution = getNewWord(words)
boardState = ["?", "?", "?", "?", "?"]
print (solution)
print('--------------------------------------------------')
print('Welcome to ', gameTitle)
print('Your object is to figure out the 5 letter word.')
print('--------------------------------------------------')

while currentGuess < maximumGuesses :
    print('You have ', maximumGuesses - currentGuess, ' attempt(s) left.')
    print("What is your guess?")
    print("")
    userInput = input("")
    lcUserInput = userInput.lower()
    if not lcUserInput.isalpha():
        print('Invalid input, must only contain letters')
        print('====')
    elif len(lcUserInput) != 5: 
        print('Invalid input, must be a 5 letter word')
        print('====')
    else:
        for index, letter in enumerate(lcUserInput):
            if letter not in solution:
                incorrectLetters.append(letter)
            elif letter != solution[index]:
                misplacedLetters.append(letter)
            else: 
                boardState[index] = letter
                misplacedLetters = list(filter(lambda x: x!=letter, misplacedLetters))
        print("".join(boardState))
        
    if (lcUserInput == solution):
        print("Congratulations you got it!")
        break

    else:
        print('')
        print('misplaced letters: ', ", ".join(set(misplacedLetters)))
        print('incorrect letters: ', ", ".join(set(incorrectLetters)))
        print('')
        print('====')
        print('')
        currentGuess += 1

if (lcUserInput != solution): 
    print('')
    print('The word was ', solution)
    print('You lose, better luck next time.')





   