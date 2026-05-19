# wap to replace list's item with new value if found
# Create a list
numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

# Value to search and replace
old_value = 30
new_value = 300

# Replace if found
if old_value in numbers:
    index = numbers.index(old_value)
    numbers[index] = new_value
    print("Updated List:", numbers)
else:
    print("Value not found in the list")