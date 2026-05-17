#  Write a Program to print Fibonacci series up to n terms using loop statement.
n=int(input("Enter a range: "));

i=0;
sum=0;
a=0; b=1;
while(i<n):
    print("\t", a, end="");
    sum=a+b;
    a=b;
    b=sum;
    i=i+1;