# Write a Program to filter even values from list using lambda function
list1=[8, 27, 11, 26, 17, 5, 25, 22, 10, 4]

even_numbers = list(filter(lambda x: x%2==0, list1))
print(even_numbers)