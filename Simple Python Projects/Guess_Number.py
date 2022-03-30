# Problem Statement:-
# Generate a random integer from a to b. You and your friend have to
# guess a number between two numbers, a and b. a and b are inputs
# taken from the user. Your friend is player 1 and plays first.
# He will have to keep choosing the number, and your program must
# tell whether the number is greater than the actual number or less
# than the actual number. Log the number of trials it took your
# friend to arrive at the number. You play the same game, and then
# the person with the minimum number of trials wins! Randomly generate
# a number after taking a and b as input and don’t show that to the
# user.

# Input:
# Enter the value of a
# 4

# Enter the value of b
# 13

# Output:
# Player1 :
# Please guess the number between 4 and 13
# 5

# Wrong guess a greater number again
# 8

# Wrong guess a smaller number again
# 6

# Correct, you took 3 trials to guess the number

# Player 2:
# Correct, you took 7 trials to guess the number

# Player 1 wins!

import random

def guessNumberGame(playerName):
    # print(playerName)
    x = random.randint(a,b)
    guessIsWrong = True
    trials = 0

    while guessIsWrong:
        num = int(input(f"Enter a number between {a} and {b} : "))
        trials += 1
        if num > x:
            print("Wrong Guess a smaller number again")
        elif num < x:
            print("Wrong guess a greater number again")
        elif num == x:
            print(f"Correct You Took {trials} TRIALS To Guess The Number")
            guessIsWrong = False
    return trials

a,b = int(input("Enter A : ")),int(input("Enter B : "))
print("THE GAME STARTS NOW")
trialP1 = input("Enter First Player Name : ")
p1 = guessNumberGame(trialP1)
trialP2 = input("Enter Second Player Name : ")
p2 = guessNumberGame(trialP2)

if trialP1 > trialP2:
    print(f"{trialP1} Wins")
else:
    print(f"{trialP2} Wins")