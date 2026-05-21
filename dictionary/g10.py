# 10. WAP to Sort a dictionary in ascending and descending order based on values.
d = {'a': 3, 'b': 1, 'c': 2}

ascending = dict(sorted(d.items(), key=lambda x: x[1]))

print("Ascending order:", ascending)

descending = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

print("Descending order:", descending)