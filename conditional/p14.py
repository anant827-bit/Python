# wap to create a simple calculator using if-elif and perform operations(+,-,*,/)
a=int(input("Enter first number: "));
b=int(input("Enter second number: "));
c=str(input("Enter operation to perform: "));

if(c=='*'):
    print(a*b);
elif(c=='/'):
    if(b!=0):
        print(a/b);
    else:
        print("Error: Divisor cannot be zero.");
elif(c=='+'):
    print(a+b);
elif(c=='-'):
    print(a-b);
else:
    print("Error: Invalid operator.");