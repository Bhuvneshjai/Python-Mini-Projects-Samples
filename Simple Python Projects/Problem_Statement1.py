try:
    apples = int(input("Enter Number of Apples : "))
    mx = int(input("Enter Maximum Value : "))
    mn = int(input("Enter Minimum Value : "))
except ValueError:
    print("Please Enter Only Integer Value")
    exit()

for i in range(mn,mx+1):
    if apples%i == 0:
        print(f"{i} is the divisor of {apples}")
    else:
        print(f"{i} is not the divisor of {apples}")

