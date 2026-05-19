# wap to check all elements are unique or not in Python
# Create a list
numbers = [10, 20, 30, 40, 50]

print("List:", numbers)

# Convert list to set
if len(numbers) == len(set(numbers)):
    print("All elements are unique")
else:
    print("Elements are NOT unique")


# numbers = [10, 20, 30, 20, 50]

# unique = True

# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] == numbers[j]:
#             unique = False

# if unique:
#     print("All elements are unique")
# else:
#     print("Elements are NOT unique")