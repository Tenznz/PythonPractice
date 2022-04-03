# 2. Write a Python program to multiply all the items in a list

def multi_all(input_list):
    res = 1
    for i in input_list:
        res *= i
        print(res)
    return res


data_list = [1, 2, 3, 4, 5, 6, -2, -9]
print(multi_all(data_list))
