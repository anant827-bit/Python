# Write a Program to calculate arithmetic operation on two number using user defined function
def arthmop(a, b, c):
    if(c=='+'):
        return a+b
    elif(c=='-'):
        return a-b
    elif(c=='*'):
        return a*b
    elif(c=='/'):
        return a/b
    elif(c=='//'):
        return a//b
    elif(c=='%'):
        return a%b
    elif(c=='**'):
        return a**b
    else:
        return -1
    
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
z=input("Enter operator: ")
result=arthmop(x, y, z)
print("Result: ", result)