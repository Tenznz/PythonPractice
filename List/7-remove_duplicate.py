# 7. Write a Python program to remove duplicates from a list

# def remove_duplicate(lists):
#     data = set(lists)
#     return list(data)
#
#
# data_list = [1, 2, 3, 4, 5, 6, 7, 86, 4, 3, 2, 4, 1]
# print(remove_duplicate(data_list))

def distinct(data):
    dup_items = set()
    uniq_items = []
    for x in a:
        if x not in dup_items:
            uniq_items.append(x)
            dup_items.add(x)

    print(dup_items)


a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
distinct(a)
