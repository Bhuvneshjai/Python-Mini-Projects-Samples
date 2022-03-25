# Program for n -- th Fibonacci Series

def fibonacci_series(n):
    if n <= 0:
        print("Incorrect Value")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_series(n-1)+fibonacci_series(n-2)

n = int(input("Enter Value of N : "))
res = fibonacci_series(n)
print(f"Fibonacci Series are : {res}")