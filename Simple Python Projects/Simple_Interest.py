# Python Program for finding Simple Interest

def simple_interest(p,r,t):
    si = (p*r*t)/100
    return si

p = int(input("Enter Principle : "))
r = int(input("Enter Rate : "))
t = int(input("Enter Time : "))

result = simple_interest(p,r,t)
print(f"The Simple Interest : {result}")