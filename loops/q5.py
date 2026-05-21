# wap to find the sum of first 'n' natural numbers
n=int(input("Enter the value of n: "));

i=1;
sumw=0;
while(i<=n):
    sumw=sumw+i;
    i=i+1;
print("Sum of first n natural numbers using while loop: ", sumw);

sumf=0;
for i in range(1,n+1):
    sumf=sumf+i;
print("Sum of first n natural numbers using for loop: ", sumf);