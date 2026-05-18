# wap to calculate the sum and average of the digits present in your registration number
str1=input("Enter your registration number: ")
count=0
sum=0

for char in str1:
    if char.isdigit():
        count+=1
        sum= sum + int(char)

print("Sum of digits:", sum)
print("Average of digits: ", sum/count)