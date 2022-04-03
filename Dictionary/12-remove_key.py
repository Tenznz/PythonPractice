# 12. Write a Python program to remove a key from a dictionary.

def remove_key(dict_data, key):
    dict_data.pop(key)
    return dict_data


def delete_key(dict_data, key):
    if key in dict_data:
        del dict_data[key]
    return dict_data


dict_dat = {1: 10, 2: 20, 3: 30}

print(remove_key(dict_dat, 2))
print(delete_key(dict_dat, 2))
print(delete_key({1: 10, 2: 20, 3: 30}, 2))
