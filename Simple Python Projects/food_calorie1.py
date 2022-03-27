# Take the size of the list from the user
print("Enter the number of the list one by one")
sizelist = int(input("Enter size of list : "))

# Initialize a blank list
mylist = []

# Take the input from the user one by one
for i in range(sizelist):
    mylist.append(int(input(f"Enter list element {i} : ")))
print(f"Your list is {mylist}")

l1 = mylist[:]
l1.reverse()

l2 = mylist[::-1]
print(f"List1 {mylist} by the help of reverse method {l1}")
print(f"List2 {mylist} by the help of slicing method {l2}")

l3 = mylist[:]
for i in range(len(l3)//2):
    l3[i],l3[len(l3)-1-i] = l3[len(l3)-1-i],l3[i]

print(f"List3 {mylist} by the help of swapping method {l3}")