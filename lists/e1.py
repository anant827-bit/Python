# wap to demonstrate various list operations in python
# Creating a list
numbers = [10, 20, 30, 40, 50]
print("Original List:", numbers)

# Accessing elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Slicing
print("First three elements:", numbers[0:3])

# Adding elements
numbers.append(60)          # Add at end
print("After append:", numbers)

numbers.insert(2, 25)      # Insert at index 2
print("After insert:", numbers)

# Extending list
numbers.extend([70, 80])
print("After extend:", numbers)

# Updating elements
numbers[1] = 200
print("After updating index 1:", numbers)

# Removing elements
numbers.remove(25)         # Remove specific value
print("After remove:", numbers)

numbers.pop()              # Remove last element
print("After pop:", numbers)

del numbers[0]             # Delete element at index 0
print("After delete:", numbers)

# List length
print("Length of list:", len(numbers))

# Sorting
numbers.sort()
print("Sorted list:", numbers)

# Reversing
numbers.reverse()
print("Reversed list:", numbers)

# Counting elements
print("Count of 40:", numbers.count(40))

# Finding index
print("Index of 40:", numbers.index(40))