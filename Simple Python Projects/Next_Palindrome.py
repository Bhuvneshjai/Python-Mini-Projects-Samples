# A palindrome is a string that, when reversed, is equal to itself. Example of the palindrome includes:

# 676, 616, mom, 100001.

# You have to take a number as an input from the user. You have to find the next palindrome corresponding
# to that number. Your first input should be the number of test cases and then take all the cases as input from the user.

# Input:
# 3
# 451
# 10
# 2133

# Output:
# Next palindrome for 451 is 454
# Next palindrome for 10 is 11
# Next palindrome for 2311 is 2222
# These tasks will improve your logic-making skills and logic is the basics of programming.

n = int(input("Enter the number of Test Cases : "))
l = []
for i in range(n):
    d = int(input(f"Input {i+1} - Enter the Digit : "))
    l.append(d)
for i in l:
    while True:
        string1 = str(i)
        reverse1 = string1[::-1]
        if string1 == reverse1:
            print(f"Next Palindrome of {i} is {string1}")
            break
        else:
            i = i+1