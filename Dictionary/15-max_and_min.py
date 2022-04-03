# 15. Write a Python program to get the maximum and minimum value in a dictionary.
max_of_two = lambda x, y: x if (x > y) else y
min_of_two = lambda x, y: x if (x < y) else y


def max_min_number(dict_data):
    max = 0
    min = 100
    for i in dict_data.values():
        max = max_of_two(max, i)
        min = min_of_two(min, i)
    return max, min


dict_data = {
    2: 20,
    1: 10,
    6: 60,
    3: 30,
    5: 50
}
print(max_min_number(dict_data))
