# wap to turn every item of a list into its square
# Create a list
numbers = [2, 4, 6, 8, 10]

print("Original List:", numbers)

# Squaring each element
for i in range(len(numbers)):
    numbers[i] = numbers[i] ** 2

print("List after squaring:", numbers)