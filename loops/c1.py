# wap to find factorial of an number.
num=int(input("Enter a number: "));

fact=1;
i=1;
while(i<=num):
    fact=fact*i;
    i=i+1;

print("Factorial of the given number using while: ", fact);


fac=1;
for i in range(1,num+1):
    fac=fac*i;
print("Factorial of the given number using for: ", fac)