# 11. Write a Python function that takes two lists and returns True if they have at least one common member.

def check_at_least_one_common(list1, list2):
    for i in list1:
        if i in list2:
            return True
    return False


input_list1 = ["1", "2", "3", "4", 5]
input_list2 = ["10", "33", "5", "55", 8]
print(check_at_least_one_common(input_list1, input_list2))
