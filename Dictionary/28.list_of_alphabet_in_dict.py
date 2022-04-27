# 28. Write a Python program to sort a list alphabetically in a dictionary.

dict1 = {
    'a': ['a', 'b', 'c'],
    'b': ['c', 'z', 'e'],
    'c': ['i', 'g', 'h']
}

print({i: sorted(v) for i, v in dict1.items()})
