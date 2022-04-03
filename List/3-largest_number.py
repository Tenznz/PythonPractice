# 3. Write a Python program to get the largest number from a list.
# from lamda.max import max


def largest_number(data_list):
    max = lambda x, y: x if x > y else y
    max_number = 0
    for i in data_list:
        max_number = max(i, max_number)
    return max_number


def max_number(data_list):
    max_number = data_list[0]
    for i in data_list:
        if i > max_number:
            max_number = i
    return max_number


num_list = [1, 6, 4, 3, 8, 6, 4, 23, 5, 76, 8, 44]
print(largest_number(num_list))
print(max_number(num_list))
