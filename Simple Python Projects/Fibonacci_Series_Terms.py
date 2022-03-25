# Program for How to check if a given number is Fibonacci Series

terms = int(input("Enter Terms : "))

n1,n2 = 0,1
count = 0

if terms <= 0:
    print("Please Enter a Positive Integer")
elif terms == 1:
    print(f"Fibonacci sequence upto {terms} : ")
    print(n1)
else:
    print(f"Fibonacci Sequence : ")
    while count < terms:
        print(n1)
        nth = n1+n2
        n1 = n2
        n2 = nth
        count = count + 1
