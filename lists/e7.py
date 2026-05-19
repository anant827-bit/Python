# wap to find the position of minimum and maximum element of a list.
# Create a list
numbers = [25, 10, 45, 5, 30]

print("List:", numbers)

# Find minimum and maximum values
min_value = min(numbers)
max_value = max(numbers)

# Find their positions
min_position = numbers.index(min_value)
max_position = numbers.index(max_value)

print("Minimum value:", min_value)
print("Position of minimum value:", min_position)

print("Maximum value:", max_value)
print("Position of maximum value:", max_position)