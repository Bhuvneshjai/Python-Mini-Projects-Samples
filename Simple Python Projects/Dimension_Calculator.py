print("...... Dimensions Calculator Starting ......")

def msquare(l):
    print(f"The Calculated Area is : (l*l) is {l*l} sq.units")

def mrectangle(l,b):
    print(f"The Calculated Area is : (l*b) is {l*b} sq.units")

def mcircle(r):
    print(f"The Calculated Area is : (3.14*r*r) is {3.14*r*r} sq.units")

def mtrapezium(h,a,b):
    print(f"The Calculated Area is : (0.5*h*a+0.5*h*b) is {0.5*h*a+0.5*h*b} sq.units")

def mtriangle(h,b):
    print(f"The Calculated Area is : (0.5*h*b) is {0.5*h*b} sq.units")

want = input("Do You Want To Calculate the Areas of the Objects (Yes/No): ")
if want == "Yes" or want == "yes" or want == "YES":
    type = 0
    while type == 0:
        name = input("Enter the shape of the objects (Square,Rectangle,Circle,Trapezium,Triangle) : ")
        if name == "Square" or name == "SQUARE" or name == "square" or name == "rectangle" or name == "Rectangle" or name == "RECTANGLE" or \
                name == "circle" or name == "Circle" or name == "CIRCLE" or name == "Trapezium" or name == "trapezium" or name == "TRAPEZIUM" or \
                name == "triangle" or name == "Triangle" or name == "TRIANGLE":
            if name == "square" or name == "Square" or name == "SQUARE":
                n1 = int(input("Enter the length of one its side (l) : "))
                msquare(n1)
            elif name == "rectangle" or name == "Rectangle" or name == "RECTANGLE":
                n1 = int(input("Enter the length of the rectangle (l) : "))
                n2 = int(input("Enter the breadth of the rectangle (b) : "))
                mrectangle(n1,n2)
            elif name == "circle" or name == "Circle" or name == "CIRCLE":
                n1 = int(input("Enter the radius of the circle (r) : "))
                mcircle(n1)
            elif name == "Trapezium" or name == "trapezium" or name == "TRAPEZIUM":
                n1 = int(input("Enter the height of the trapezium (h) : "))
                n2 = int(input("Enter the length of the trapezium (a) : "))
                n3 = int(input("Enter the parallel length of the trapezium (b) : "))
                mtrapezium(n1,n2,n3)
            elif name == "triangle" or name == "Triangle" or name == "TRIANGLE":
                n1 = int(input("Enter the height of the triangle (h) : "))
                n2 = int(input("Enter the Base of the triangle (b) : "))
                mtriangle(n1,n2)
            again = input("Restarting Dimension Calculator (Yes/No) : ")
            if again == "Yes" or again == "YES" or again == "yes":
                type = 0
            elif again == "No" or again == "no" or again == "NO":
                print("Stopping Calculator")
                break
            else:
                print("You Entered Wrong Input")
                break
        else:
            print("You Entered Wrong Name")
elif want == "No" or want == "NO" or want == "no":
    print("You Entered No. So We cannot calculate and move forward")
else:
    print("! Invalid Option ! ")
