# 2. Write a Python program to multiply all the items in a list

def multi_all(input_list):
    res = 1
    for i in input_list:
        res *= i
        print(res)
    return res


def multi_first3(input_list):
    res = 1
    for i in input_list[:3:]:
        res *= i
    return res


def multi_even_index(input_list):
    res = 1
    # print(len(input_list))
    for i in range(0, len(input_list), 2):
        res *= input_list[i]
        print(input_list[i])
    return res


if __name__ == "__main__":
    data_list = [1, 2, 3, 4, 5, 6, -2, -9]
    # print(multi_all(data_list))
    # print(multi_first3(data_list))
    print(multi_even_index(data_list))
