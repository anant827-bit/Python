# Write a program to create a list of tuples from given list having number and its cube in each tuple 

# Given list
numbers = [1, 2, 3, 4, 5]

result = []

for n in numbers:
    result.append((n, n**3))

print("List of tuples (number, cube):")
print(result)