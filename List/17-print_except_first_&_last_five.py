def print_expect_fist_last_5():
    new_list = [i ** 2 for i in range(1, 31) if 5 < i < 25]
    return new_list


print(print_expect_fist_last_5())
