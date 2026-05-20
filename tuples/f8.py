# Find Second Largest Element in a Tuple
t=(8,8,11,27,8,27,26,22,25,17,10,27)

lst=list(set(t))
lst.sort()

print("Second largest element: ", lst[-2])