def merge_list(list1, list2):
    list1.extend(list2)
    return list1


list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend([1, 2, 3, 4])
print(list1)
