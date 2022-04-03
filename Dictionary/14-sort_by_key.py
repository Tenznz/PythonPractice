# 14. Write a Python program to sort a given dictionary by key

def sort_by_key(dict_data):
    sorted_data = dict(sorted(dict_data.items()))
    return sorted_data


print(sort_by_key({2: 20, 1: 10, 5: 50, 3: 30, 4: 40}))
