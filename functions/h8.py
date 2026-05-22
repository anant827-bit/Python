# Write a Program to find small number between two numbers using Lambda function 

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

result = lambda x,y: x>y
if(result(a,b)):
    print(b)
else:
    print(a)