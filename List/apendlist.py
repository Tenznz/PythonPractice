# 24. Write a Python program to append a list to the second list.

list1 = [1, 2, 3, 4, 5]
list2 = [9, 8, 7, 6, 5, 3]
list3 = ['a', 'b', 'c', 'd']
print(list1 + list2 + list3)
list1.extend(list2)

print(list1)
# or
print(sorted(list1))
