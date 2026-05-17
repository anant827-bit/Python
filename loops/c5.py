# Write a Program to construct the following pattern using nested for loop:  
# *  
# **  
# ***  
# ****  
# *****  
# *****  
# ****  
# ***  
# **  
# *  
limit = int(input("Enter a range: "));

i=1;
while(i <= limit):
    j=1;
    while(j<=i):
        print("*", end="");
        j=j+1;
    print("");
    i=i+1;

i=limit;
while(i > 0):
    j=i;
    while(j>0):
        print("*", end="");
        j=j-1;
    print("");
    i=i-1;

        