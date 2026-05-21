# WAP to Invert a Dictionary i.e swap key and values (assume Values are Unique)
d = {'a': 1, 'b': 2, 'c': 3}

inverted_dict = {}

for key, value in d.items():
    inverted_dict[value] = key

print("Inverted Dictionary:", inverted_dict)