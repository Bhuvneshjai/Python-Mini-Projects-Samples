import random

def guessGame(a,b,actual):
    guess = int(input(f"Enter a number between {a} and {b} : "))
    nguess = 1
    while guess != actual:
        if guess < actual:
            guess = int(input(f"Enter a bigger number : "))
            nguess += 1
        else:
            guess = int(input(f"Enter a smaller number : "))
            nguess += 1
    print(f"You Guessed The Number in {nguess} guesses")
    return nguess

if __name__ == "__main__":
    a = int(input("Enter the value of A : "))
    b = int(input("Enter the value of B : "))
    actual1 = random.randint(a,b)
    print("Player-1 Turn")
    g1 = guessGame(a,b,actual1)
    print("Player-2 Turn")
    actual2 = random.randint(a,b)
    g2 = guessGame(a,b,actual2)
    if g1 < g2:
        print("Player-1 Won The Match !")
    elif g1 > g2:
        print("Player-2 Won The Match !")
    else:
        print("Tie")
    print(f"The Number for Player-1 was {actual1} and for Player-2 was {actual2}")