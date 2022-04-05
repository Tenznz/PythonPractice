# 16. Write a Python program to generate and print a list of first and last 5 elements
# where the values are square of numbers between 1 and 30 (both included).

def get_list():
    new_list = [x ** 2 for x in range(1, 31)]
    print(new_list[:5:])
    print(new_list[-5::])
    print(new_list[0::5])
    return new_list


print(get_list())
