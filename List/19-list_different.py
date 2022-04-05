# 19. Write a Python program to get the difference between the two lists

def list_diff(list1, list2):
    new_list = list(set(list1) - set(list2)) + list(set(list2) - set(list1))
    new_list.sort()
    return new_list


def diff(list1, list2):
    new_list1 = [x for x in list2 if x not in list1]
    new_list2 = [x for x in list1 if x not in list2]
    new_list = new_list1 + new_list2
    new_list.sort()
    print(new_list)


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [3, 23, 4, 6, 56, 78, 76, 2, 1]
print(list_diff(list1, list2))
diff(list1, list2)
