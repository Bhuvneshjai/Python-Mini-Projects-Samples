# find the sum of natural numbers
num = int(input("Enter a number: "))
if num<0:
    print("Don't type negative number")
else:
    sum = 0
    while(num>0):
        sum += num
        num -= 1
    print("The sum is : ",sum)
