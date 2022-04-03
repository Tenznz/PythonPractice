# 4. Write a Python program to get the smallest number from a list.

def smallest_number(data_list):
    min = lambda x, y: x if x < y else y
    min_number = data_list[0]
    for i in data_list:
        min_number = min(min_number, i)
    return min_number


def min_number(data_list):
    min = data_list[0]
    for i in data_list:
        if min > i:
            min = i
    return min


num_list = [3, 3, 5, 6, 7, 4, 8, 4, 3, -56]
print(smallest_number(num_list))
print(min_number(num_list))

