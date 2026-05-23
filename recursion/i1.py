# Write a python program to find factorial of a number using Recursion.
def fact(x):
    if(x==0 or x==1):
        return 1
    else:
        return x*fact(x-1)
    
a=int(input("Enter a number:"))
print("Factorial:", fact(a))