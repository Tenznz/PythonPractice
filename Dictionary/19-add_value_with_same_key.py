# 19. Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
from collections import Counter


def add_value_of_same_key(*dict_data):
    counter_obj = {}
    for data in dict_data:
        counter_obj = Counter(counter_obj) + Counter(data)
    return counter_obj


if __name__ == "__main__":
    d1 = {'a': 100, 'b': 200, 'c': 300}
    d2 = {'a': 300, 'b': 200, 'd': 400}
    print(add_value_of_same_key(d1, d2))
