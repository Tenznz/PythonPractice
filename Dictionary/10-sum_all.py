# 10. Write a Python program to sum all the items in a dictionary.

def sum_all(dic_data):
    res = 0
    for i in dic_data.values():
        res += i
    return res


print(sum_all({1: 10, 2: 20, 3: 30, 4: 40}))
