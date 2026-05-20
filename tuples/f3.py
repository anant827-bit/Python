# Write a program to find the maximum and minimum K elements in a tuple 

# Tuple
t = (10, 4, 25, 18, 7, 32, 1)

# Number of elements
k = int(input("Enter value of K: "))

# Convert tuple to list and sort
sorted_list = sorted(t)
print(sorted_list)

# Minimum K elements
print("Minimum", k, "elements:", sorted_list[:k])

# Maximum K elements
print("Maximum", k, "elements:", sorted_list[-k:])