'''
Neel Sheth
ITP115, Summer 2020
ndsheth@usc.edu
Homework 7
'''

import random

# Part 1: List of starter strings
wordList = ["ape", "computer", "flute", "program"]

# Part 1: Make a dictionary to keep track of guesses...
wordsDict = {}

# Populate dictionary with
# WORD : {"guesses" : 0, "right" : 0}
for word in wordList:
    # Word is now "ape" or "flute"
    # # Way 1:
    # value = {"guesses" : 0, "right" : 0}
    # Way 2:
    value = {}
    value["right"] = 0
    value["guesses"] = 0
    # Add key/value to dictionary
    wordsDict[word] = value

# print(wordsDict)

# Part 1: User interface...
userInput = "1"
while userInput == "1" or userInput == "2" or userInput == "3":
    # print(wordsDict)

    print("\nPick an option:")
    print("1) Add a word")
    print("2) Guess a word")
    print("3) Stats")
    print("?) Quit")
    userInput = input(">")

    if userInput == "1":
        print("\nAdding a word!")
        # Part 2: Adding a new word
        userWord = input("Enter a word: ")
        userWord.strip().lower()

        if userWord not in wordsDict:
            # Then the word doesn't exist
            # print("Adding \"" + userWord + "\"")
            # Creating the value for the dictionary
            value = {}
            value["guesses"] = 0
            value["right"] = 0
            # Add it to the dictionary
            wordsDict[userWord] = value
            print("That word was added. There are now " + str(len(wordsDict)) +
                  " words in the jumble.")

        else:
            print("That word is already in the jumble")

    if userInput == "2":
        print("\nJumbling a word")

        # Pick a random word from the dictionary and jumble it
        computerWord = random.choice(list(wordsDict.keys()))
        # print("Computer picked: " + computerWord)
        computerWordList = list(computerWord)
        # print(computerWordList)
        random.shuffle(computerWordList)
        # print(computerWordList)
        jumbledWord = "".join(computerWordList)
        # print(jumbledWord)

        userGuesses = 0
        userGuess = ""
        maxGuesses = 5

        while userGuesses < maxGuesses:
            userGuess = input("The jumbled word is \"" + jumbledWord +
                              "\". What's the word: ").strip().lower()
            userGuesses += 1
            # Check to see if they guessed the word
            if userGuess == computerWord:
                # They guessed the word
                print("\nThat's right!")
                wordsDict[computerWord]["right"] += 1
                break

        # Record the statistics
        # Update the number of guesses
        wordsDict[computerWord]["guesses"] += userGuesses
        # Did they get the word?
        # if userGuess == computerWord:
        #     wordsDict[computerWord]["right"] += 1

    if userInput == "3":
        print("\nDisplaying statistics")
        formatString = "{:20s}{:>10s}{:>10s}{:>10s}"
        formatNumbers = "{:20s}{:10d}{:10d}{:9.0f}%"
        print(formatString.format("WORD", "GUESSES", "RIGHT", "PERCENT"))

        # Loop over words
        alphabatizedWords = list(wordsDict.keys())
        alphabatizedWords.sort()
        for word in alphabatizedWords:
            if wordsDict[word]["guesses"] == 0:
                print(formatNumbers.format(word, 0, 0, 0))
            else:
                print(formatNumbers.format(word, wordsDict[word]["guesses"],
                      wordsDict[word]["right"], (wordsDict[word]["right"] / wordsDict[word]["guesses"]) * 100))


print("Goodbye!")
