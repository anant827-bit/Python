# Write a function that takes three numbers as parameters, and returns the median value of those parameters as its result. Include a main program that reads three values from the user and displays their median.
def median(a, b, c):
    list = [a, b, c]
    list.sort()
    return list[1]

x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
z=int(input("Enter third number: "))
print("Median:", median(x,y,z))