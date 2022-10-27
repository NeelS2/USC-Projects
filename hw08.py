'''
Neel Sheth
ITP115, Summer 2020
ndsheth@usc.edu
Homework 8
'''

import random

def main():
    playAgain = "y"
    # Variable to hold the user's money
    userMoney = int(100)
    print("Step right up and play some CHUCK-A-LUCK!!!")

    # Keeps the game going as long as the user inputs y - wasn't clear on whether or not to continue if user types in something besides y or n
    while playAgain.strip().lower() == "y":
        print("\nYou have $" + str(userMoney))
        print("Enter a bet amount: ")

        # Loop to get the (valid) amount the user is going to bet
        userBet = int(1)
        while userBet > 0 and userBet <= userMoney:
            userBet = int(input(">$ "))
            if userBet > 0 and userBet <= userMoney:
                break
            else:
                print("Invalid bet. Please enter an amount from $1 to $" + str(userMoney))
                userBet = int(1)

        print("What number do you want to bet on (1-6)?")

        # Loop to get the (valid) number the user is guessing
        userNumber = int(1)
        while userNumber >= 1 and userNumber <= 6:
            userNumber = int(input("> "))
            if userNumber >= 1 and userNumber <= 6:
                break
            else:
                print("Invalid number. Must be between 1 and 6.")
                userNumber = int(1)
        print("You bet $" + str(userBet) + " on " + str(userNumber))
        print("You rolled: ")

        # Call the roll function and print it in a nice way
        rollList = roll()
        delimiter = ", "
        print("\t" + delimiter.join(rollList))

        # .join only works with str, so i had the list in strings, but here i change it to a int list for the next function
        for value in range(0, len(rollList)):
            rollList[value] = int(rollList[value])

        # Call betResults function, print what happened with their bet and add the bet result to their current money
        betResults = int(computeBetResult(rollList, userBet, userNumber))
        if betResults > 0:
            print("You won $" + str(betResults) + "! (plus your original bet back)")
        else:
            print("You lost your bet.")
        userMoney += betResults

        # Conditional that breaks out of the loop (and thus, the game) if the user has 0 money left
        if userMoney <= 0:
            print("You have no money left!")
            break
        else:
            print("You now have $" + str(userMoney))

        # Exits the game if the user says n
        print("Would you like to play again? (y/n)")
        playAgain = input("> ")
        if playAgain.lower().strip() == "n":
            print("\nYou ended the game with $" + str(userMoney))

# end main function

# Function name: roll
# Purpose: Simulate rolling a die 3 times
# Input: None
# Output: A list of 3 random ints between 1-6
# Side effects: None
def roll():
    rollList = []

    # Loop to fill the list with 3 random numbers
    while len(rollList) < 3:
        randomRoll = str(random.randrange(1, 6, 1))
        rollList.append(randomRoll)
    return rollList

# Function name: computeBetResult
# Purpose: Tell the user how many die they matched and calculate how much the user won/lost
# Input: rollList (the list of 3 random rolls from roll function - list), userBet (amount user bet - int), userNumber (number user is betting on - int)
# Output: An int with the amount of money the user won or lost
# Side effects: Tells the user how many die they matched with their number
def computeBetResult(rollList, userBet, userNumber):
    counter = int(0)
    betMoney = int(0)

    # Loop to see how many of the random numbers match the user guess
    for number in rollList:
        if userNumber == number:
            counter += 1
    print("You matched " + str(counter) + " dice!")

    # Conditional to calculate how much the user won or lost
    if counter == 0:
        betMoney = -userBet
    elif counter == 1:
        betMoney = userBet
    elif counter == 2:
        betMoney = (3 * userBet)
    elif counter == 3:
        betMoney = (10 * userBet)
    return betMoney


main()