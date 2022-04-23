# 27. Write a Python program to convert a list into a nested dictionary of keys.

num_list = [1, 2, 3, 4]
new_dict = current = {}
for name in num_list:
    current.update({name: {}})
    current = current.get(name)
print(new_dict)
