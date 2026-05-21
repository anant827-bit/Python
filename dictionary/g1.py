# Write a program to demonstrate working with dictionaries in python

# Creating a dictionary
student = {"name": "Vaibhavi", "age": 19, "course": "B.tech"}

# Accessing elements
print("Name:", student["name"])

# Adding new element
student["marks"] = 89

# Updating value
student["age"] = 20

# Removing element
student.pop("course")

# Display dictionary
print("Updated Dictionary:", student)

# Loop through dictionary
for key, value in student.items():
    print(key, ":", value)