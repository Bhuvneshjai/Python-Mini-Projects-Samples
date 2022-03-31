'''
Problem Statement:-
 Rohan das is a fraud by nature. Rohan Das wrote a python function to print a multiplication table of a given number and put one of the values (randomly generated) as wrong.

Rohan Das did this to fool his classmates and make them commit a mistake in a test. You cannot tolerate this!

So you decided to use your python skills to counter Rohan’s
actions by writing a python program that validates Rohan’s
multiplication table.

Your function should be able to find out the wrong values in Rohan’s
table and expose Rohan Das as a fraud.

Note: Rohan’s function returns a list of numbers like this

Rohan Das’s Function Input:
rohanMultiplication(6)

Rohan’s function returns this output:
[6, 12, 18, 26, …., 60]

You have to write a function isCorrect(table, number) and return
the index where rohan’s function is wrong and print it to the screen!
If the table is correct, your function returns None
'''

# This function is used for to check that table is correct or not
import random

def isCorrect(number,itable):
    list1 = []
    for i in range(1,11):
        list1.append(number*i)
    for i in range(len(list1)):
        if itable[i] != list1[i]:
            print(f"The Index Of Wrong Number {itable[i]} is {i}")

# This function is used for make the table and place a random number to the random place
def isTable(number):
    itable = []
    for i in range(1,11):
        itable.append(number*i)
    ran_num = random.randint(2,9)
    itable[ran_num] = random.randint(number*2,number*9)
    print(itable)

    ask = input("Do You Want To Check The Table : Y/N : ").lower()
    if ask == "y":
        isCorrect(num,itable)
    elif ask == "n":
        exit()
    else:
        print("Not a valid Input")

if __name__ == "__main__":
    try:
        num = int(input("Enter a number : "))
        isTable(num)
    except Exception as e:
        print("Please Enter A Valid Input")