while True:
    age = int(input("Enter year of birth or age : "))
    year_of_age = int(input("Find your age for year ? : "))
    if age > 150:
        t = year_of_age - age
        print(f"Your age in year {year_of_age} will be {t}")
    elif (age>0 and age<=150):
        n = 2022 - age
        l = year_of_age - n
        print(f"Your age in year {year_of_age} will be {l}")
    elif age <= 0:
        print("Seems like You are not Born")
    ex = input("Do You Want To Exit ? Y/N : ")
    if ex == "Y" or ex == "y":
        exit()
    else:
        continue