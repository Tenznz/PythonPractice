# 20. Write a Python program access the index of a list.

list_d = ['a', 'b', 'c', 'd', 'e']
new_list = list()
for index, value in enumerate(list_d, start=0):
    print(index, value)
    new_list.append((index, value))

print(list_d)
print(new_list)
# print(dict(new_list))
