# Convert Tuple into a List and Remove Duplicates
t=(8,8,11,27,8,27,26,22,25,17,10,27)

lst=list(set(t))
print(lst)

lst2=[]
for i in t:
    if i not in lst2:
        lst2.append(i)

print(lst2)