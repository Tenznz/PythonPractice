# 23. Write a Python program to flatten a shallow list.
import itertools


def flatten_list(list_d):
    new_list = list()
    for i in list_d:
        new_list.extend(i)
    return new_list


original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
# print(original_list)
# print(list(itertools.chain(*original_list)))
print(flatten_list(original_list))
