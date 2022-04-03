# 13. Write a Python program to map two lists into a dictionary.

def create_dic(list1, list2):
    new_dict = dict()
    for i in range(0, len(list1)):
        new_dict.update({list1[i]: list2[i]})
    return new_dict


list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

print(create_dic(list1, list2))
