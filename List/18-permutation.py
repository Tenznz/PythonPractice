# 18. Write a Python program to generate all permutations of a list in Python.
import itertools

list_d = [x for x in range(1, 5)]

print(list(itertools.permutations(list_d)))
print(len(list(itertools.permutations(list_d))))