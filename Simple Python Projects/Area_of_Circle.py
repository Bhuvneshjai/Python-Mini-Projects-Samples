# Program for Finding Area of a Circle

def FindArea(r):
    pi = 3.14
    return pi*r*r

radius = int(input("Enter Radius : "))
result = FindArea(radius)

print(f"The Area of Circle is : {result}")