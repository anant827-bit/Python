# Write a Program to find the sum of elements of a list using lambda function
add = lambda x, y: x+y
lst=[1,2,3,4,5]
sum=0
for num in lst:
    sum = add(sum, num)
print(sum)
