# wap to find even numbers from a list
# Creating a list
numbers = [10, 15, 22, 33, 40, 55, 60]

print("Original List:", numbers)

print("Even Numbers in the List:")

for num in numbers:
    if num % 2 == 0:
        print(num)