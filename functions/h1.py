# Write a Program to write user defined function to swap two number and display number before swapping and after swapping
def swap(a, b):
    a=a+b
    b=a-b
    a=a-b
    print("After swapping: ", a, ",", b)

x=8
y=27
print("Before swapping: ", x, ",", y)
swap(x,y)
