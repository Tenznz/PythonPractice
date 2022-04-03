# 8. Write a Python program to check a list is empty or not.
def is_empty(lists):
    # if len(lists) == 0:
    if not lists:
        return True
    else:
        return False


data_list = list()
data_list.append(6)
print(data_list)
print(is_empty(data_list))
