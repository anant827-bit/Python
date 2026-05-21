#  Write a Program to generate dictionary of numbers and their squares (i, i*i) from 1 to N 

n = int(input("Enter value of N: "))

d = {}

for i in range(1, n+1):
    d[i] = i*i

print("Dictionary of numbers and their squares:")
print(d)