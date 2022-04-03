# 11. Write a Python program to multiply all the items in a dictionary.

def multiply_all(dict_data):
    res = 1
    for i in dict_data.values():
        res *= i
    return res


print(multiply_all(dict_data={1: 10, 2: 2, 3: 3, 4: 4}))
