# Python Program for Finding Compound Interest

def compound_interest(p,r,n):
    Amount = p*(pow((1+r/100),(n)))
    ci = Amount - p
    return ci

p = int(input("Enter Principle : "))
r = float(input("Enter Rate : "))
n = int(input("Enter Number of Times Interest Applied Per Time Period : "))

result = compound_interest(p,r,n)
print(f"Compound Interest : {result}")