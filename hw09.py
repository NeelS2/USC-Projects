'''
Neel Sheth
ITP115, Summer 2020
ndsheth@usc.edu
Homework 9
'''

import random

# Main function
def main():
    # Get names of the files and use the functions that read them
    wordFile = input("Word file name: \n> ")
    artFile = input("Art file name: \n> ")
    wordList = loadWords(wordFile)
    artList = loadArt(artFile)

    # print(wordList)
    # for index in artList:
    # print(index)

    userOption = "1"
    # Loop until user does not enter 1 or 2
    while userOption == "1" or userOption == "2":
        print("Pick an option..."
              "\n1) Play Space Man"
              "\n2) Add to word list"
              "\n?) Quit")
        userOption = input("> ")

        # Conditional for when user enters 1
        if userOption == "1":
            print("Let's play some SpaceMan!")
            # Initialize variables needed, pick the random word, and generate underscore list with those functions
            guessedLetters = []
            wrongGuessCounter = int(0)
            loopBool = True
            userError = "1"
            artLen = int(len(artList))
            randWord = pickWord(wordList)
            userGuessList = genEmpties(randWord)

            # These loops play the game, it is nested so that if the user does an error, it doesn't exist the game
            # as a whole (like if the user enters more than one letter and I have to break, it won't break out of the
            # whole game).
            while userError == "1":
                while loopBool:
                    # Prints the art and conditional for if the user uses up all the guesses
                    print("\n" + artList[wrongGuessCounter])
                    if wrongGuessCounter == (artLen - 1):
                        print("You lose!")
                        print("The word was " + randWord)
                        userError = "2"  # userError == "2" because if the user loses, then I have to break out of both loops
                        break

                    # Prints out some info to the user, letters guesses, and what of the word has been guessed
                    guessString = ", ".join(guessedLetters)
                    print("You've already guessed these letters: " + guessString)
                    underscoreString = " ".join(userGuessList)
                    print("Your word is \"" + underscoreString + "\"")
                    letterGuess = input("Letter please: ")
                    guessLen = int(len(letterGuess))

                    # Breaks both loops if the user just presses enter and goes back to menu
                    if not letterGuess:
                        userError = "2"
                        break
                    # Breaks one of the loops and resets to asking for another letter if user enters more than 1 letter
                    if guessLen != 1:
                        print("You can only guess one letter at a time!")
                        break

                    # If user already guessed that letter, alreadyGuessed will be true and one of the loops break
                    alreadyGuessed = False
                    for item in guessedLetters:  # This loop checks the list of guessed letters to see if letter has been guessed
                        if letterGuess == item:
                            print("You've already guessed \"" + letterGuess + "\"!")
                            alreadyGuessed = True
                            break
                    if alreadyGuessed:
                        break
                    guessedLetters.append(letterGuess)   # Adds to the list of guessed letters if it gets this far

                    # Uses the function checkGuess to check if the letter is in the word and update the list of underscores if needed
                    if checkGuess(letterGuess, randWord, userGuessList):
                        letterCount = int(randWord.count(letterGuess))
                        print("Found " + str(letterCount) + " " + "\"" + letterGuess + "\"!")
                    # If the letter is not in the word, it tells the user and increments the wrong guess counter by 1
                    else:
                        print("Didn't find any " + "\"" + letterGuess + "\".")
                        wrongGuessCounter += 1

                    # If gameOver returns True, that means that the word has been gussed and both loops need to be broken out of
                    if gameOver(userGuessList):
                        print("You win!")
                        print("You correctly guessed \"" + randWord + "\"!")
                        userError = "2"
                        break

        # Conditional for when the user enters 2
        elif userOption == "2":
            newWord = input("Enter a word to add to the word list: ")
            newWord = newWord.strip().lower()

            # If addWord returns False, word is in list already
            if not addWord(newWord, wordList):
                print("The word " + newWord + " is already in the list")
            # If returns True, let the user know the word has been added
            elif addWord(newWord, wordList):
                print("Added the new word " + newWord + " to the word list.")

        # If user does not enter 1 or 2, loop stores new words and breaks
        else:
            storeWords(wordFile, wordList)
            print("Goodbye!")
            break
# End main function

# Function: loadWords
# Desc: Opens file and reads each word in the file
# Input: File name (with 1 word on each line)
# Output: List of words
# Side effects: Opens a file, reads it, then closes file
def loadWords(fName):
    retval = []

    # 1. Open file
    wordFile = open(fName, "r")
    # 2. Read file
    for line in wordFile:
        word = line.strip().lower()
        retval.append(word)
    # 3. Close file
    wordFile.close()

    return retval

# Function: loadArt
# Desc: Opens file and reads each line in the file
# Input: File name (with 1 art thing on each line)
# Output: List with each index having a line of the art
# Side effects: Opens a file, reads it, cleans up some of the format, then closes file
def loadArt(fName):
    retval = []

    # 1. Open file
    artFile = open(fName, "r")
    # 2. Read file
    for line in artFile:
        artReplaceOne = line.replace("\\n", "\n")
        artReplaceTwo = artReplaceOne.replace("\\\\", "\\")
        retval.append(artReplaceTwo)
    # 3. Close file
    artFile.close()

    return retval

# Function: addWord
# Desc: Checks if the word is in the list. If not, it adds it to the list.
# Input: The word to add (string), list to add it to (list)
# Output: True if word was added, false if not
# Side effects: Will append and sort a list if word isn't already in list
def addWord(nWord, wList):
    for index in wList:
        if index == nWord:
            return False
    wList.append(nWord)
    wList.sort()
    return True

# Function: storeWords
# Desc: Opens file and writes in new words
# Input: File name (with 1 word on each line), list of words (list)
# Output: None
# Side effects: Opens a file, rewrites it with the new word, closes file
def storeWords(fName, wList):
    # 1. Open file for writing
    newFile = open(fName, "w")
    # 2. Write to file
    for word in wList:
        print(word, file=newFile)
    # 3. Close file
    newFile.close()

    print("Storing words...")
    return None

# Function: pickWord
# Desc: Picks a random word from the list
# Input: List of words (list)
# Output: One word that is picked (string)
# Side effects: None
def pickWord(wList):
    listLength = int(len(wList))
    randNum = random.randrange(listLength)
    return wList[randNum]

# Function: genEmpties
# Desc: Makes a list of underscores with the amount of letters in the word
# Input: One word (string)
# Output: List of underscores
# Side effects: None
def genEmpties(rWord):
    retval = []
    wordLen = len(rWord)
    counter = int(0)
    while counter < wordLen:
        retval.append("_")
        counter += 1
    return retval

# Function: gameOver
# Desc: Finds out if the word has been guessed yet and the game should end
# Input: List of what has already been guessed (list)
# Output: Returns True if every underscore is gone (every letter guessed), false if not
# Side effects: None
def gameOver(usList):
    for letter in usList:
        if letter == "_":
            return False
    return True

# Function: checkGuess
# Desc: Checks if the letter the user guessed is in the word or not
# Input: One letter (string), One word (string), list of what has been guessed (list)
# Output: Returns True if letter is in word, false if not
# Side effects: Edits the list to replace underscore with letter if guessed
def checkGuess(letGuess, rWord, wList):
    wordLen = int(len(rWord))
    if letGuess in rWord:
        for letter in range(wordLen):
            if letGuess == rWord[letter]:
                wList[letter] = letGuess
        return True
    return False


main()