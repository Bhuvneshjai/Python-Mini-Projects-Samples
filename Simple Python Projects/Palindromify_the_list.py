# Problem Statement:-
# You are given a list that contains some numbers. You have to print a list of the next palindromes only if the number is greater than 10;
# otherwise, you will print that number.
# Input:
# [1, 6, 87, 43]

# Output:
# [1, 6, 88, 44]

n = int(input("How many numbers you want to give into the list : "))
list1 = []
for i in range(n):
    user = int(input("Enter the number : "))
    if user < 10:
        list1.append(user)
        # print(list1)
    elif user > 10:
        for i in range(50):
            user1 = user + i
            user1 = str(user1)
            if user1 == user1[::-1]:
                user1 = int(user1)
                list1.append(user1)
                break
    print(list1)
        