# wap to interchange first and last element of a list
# Create a list
numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

# Swapping first and last elements
numbers[0], numbers[-1] = numbers[-1], numbers[0]

print("List after swapping:", numbers)