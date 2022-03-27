# You visited a restaurant called CodeWithHarry, and the food items in that restaurant are sorted, based on their amount of calories. You have to reserve this list of food items containing calories.

# You have to use the following three methods to reserve a list:

# Inbuild method of python
# List name [::-1] slicing trick
# Swap the first element with the last one and second element with second last one and so on like,
# [6 7 8 34 5] -> [5 34 8 7 6]

# Input:
# Take a list as an input from the user

# [5, 4, 1]

# Output:
# [1, 4, 5]

# [1, 4, 5]

# [1, 4, 5]

# All three methods give the same results!

food_calorie = list(map(int,input("Enter the Calories : ").split()))
print(food_calorie)
l2 = list(reversed(food_calorie))
l3 = food_calorie[::-1]
length = len(food_calorie)
for i in range(length//2):
    temp = food_calorie[i]
    food_calorie[i] = food_calorie[-1+i]
    food_calorie[-1+i] = temp
print(f"By using in-built method List2 : {l2}")
print(f"By using slicing method list3 : {l3}")
print(f"By swapping : {food_calorie}")
if l2 == l3 == food_calorie:
    print("Same")