# Write a Program to print Fibonacci series up to n terms using recursion
def fibo(n):
    if n<0:
        return -1
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
n=int(input("Enter a range:"))

for i in range(n):
    result=fibo(i)
    if result!=-1:
        print(result,"",end="")
    else:
        break