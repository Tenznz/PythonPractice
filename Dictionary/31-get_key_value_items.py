# 31. Write a Python program to get the key, value and item in a dictionary.
import itertools

mydict = {'item1': 45, 'item2': 35, 'item3': 41, 'item4': 55, 'item5': 24}
#
for count, (key, value) in enumerate(mydict.items(), 1):
    print(key, '   ', value, '    ', count)


myit = iter(mydict.items())
print(myit)
print(next(myit))
print(next(myit))