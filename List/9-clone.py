# 9. Write a Python program to clone or copy a list.

lists = [1, 2, 3, 4, 5, 6, 7, 4, 2, 3, 2]
print("Original list : ", lists)

copy_list1 = lists.copy()
print("Copy list1 : ", copy_list1)

copy_list2 = lists
print("Copy list2 : ", copy_list2)

copy_list3 = list(lists)
print("Copy list3 : ", copy_list3)

