# WAP to Count Frequency of Elements in a Listv
list1 = [1, 2, 2, 3, 4, 1, 2, 3]

freq = {}

for item in list1:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

print("Frequency of elements:", freq)
print(len(freq))