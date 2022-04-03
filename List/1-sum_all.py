# 1. Write a Python program to sum all the items in a list.

def sum_list(item):
    sum_number = 0
    for i in item:
        sum_number += i
    return sum_number


if __name__ == "__main__":
    input_item = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(sum_list(input_item))
