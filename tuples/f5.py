# Count Frequency of Elements in a Tuple
from collections import Counter
t=(8,8,11,27,8,26,17,27,25,27,22,10,4,5)

result=list(Counter(t).items())
print("Frequency: ", result)

# t = (2,2,2,56,67,56,89,4,4)
# lst = sorted(t)

# list1 = []

# for i in range(len(lst)):
#     count = 0
#     n = lst[i]
    
#     if i > 0 and lst[i] == lst[i-1]:
#         continue   # skip duplicates
    
#     for j in range(len(lst)):
#         if lst[j] == n:
#             count += 1
    
#     list1.append((n, count))

# print(list1)