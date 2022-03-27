# Take age or year of birth as an input from the user.
# Store the input in one variable. Your program should detect
# whether the entered input is age or year of birth and tell the
# user when they will turn 100 years old. (5 points).

# Here are a few instructions that you must have to follow:

# Do not use any type of module like DateTime or date utils. (-5 points)
# Users can optionally provide a year, and your program must tell
# their age in that particular year. (3points)
# Your code should handle all sorts of errors like : (2 points)
# You are not yet born
# You seem to be the oldest person alive
# You can also handle any other errors, if possible!

a = int(input("Enter Current Year : "))
b = int(input("Enter Your Current Age : "))
if a == 2090:
    print(f"Your age is {b}")
elif a>2090:
    print("Please enter a year less than 2090")
elif a<2090:
    c = 2090-a
    print(f"Your age in 2090 will be : {b+c}")
else:
    print("Not Valid !")