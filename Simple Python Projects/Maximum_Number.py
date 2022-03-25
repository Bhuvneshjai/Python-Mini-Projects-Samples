# Maximum of Two Numbers in Python

def maximum_number(a,b):
    if a >= b:
        return a
    else:
        return b

a = int(input("Enter a : "))
b = int(input("Enter b : "))
result = maximum_number(a,b)
print(f"Maximum Number is : {result}")