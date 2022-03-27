yearAge = int(input("What is your Age/Year of birth : "))
isAge = False
isYear = False

if len(str(yearAge)) == 4:
    isYear = True
else:
    isAge = True

if (yearAge < 1900 and isYear):
    print("You Seem to be the oldest person alive")
    exit()
elif (yearAge > 2022):
    print("You are not born yet")
    exit()
elif isAge:
    yearAge = 2022 - yearAge

print(f"You will be 100 years old in {yearAge+100}")
interestedYear = int(input("Enter the year you want to know your age in : "))
print(f"You will be {interestedYear - yearAge} years old in {interestedYear}")