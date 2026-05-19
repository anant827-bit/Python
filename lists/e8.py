# wap to find the cumulative sum of elements of a list
# Create a list
numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

cumulative_sum = []
total = 0

for num in numbers:
    total = total + num
    cumulative_sum.append(total)

print("Cumulative Sum List:", cumulative_sum)