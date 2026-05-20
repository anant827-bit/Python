# Write a program to demonstrate various tuple operations in python.  
# Creating a tuple
t = (10, 20, 30, 40, 50)

print("Original Tuple:", t)

# Accessing elements
print("First element:", t[0])
print("Last element:", t[-1])

# Slicing
print("Sliced Tuple:", t[1:4])

# Length of tuple
print("Length:", len(t))

# Concatenation
t2 = (60, 70)
new_tuple = t + t2
print("Concatenated Tuple:", new_tuple)

# Repetition
print("Repeated Tuple:", t * 2)

# Membership
print("Is 20 in tuple?", 20 in t)

# Iteration
print("Tuple elements:")
for i in t:
    print(i)