# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.

def removing_even(lists):
    new_list = [x for x in lists if x % 2 != 0]
    # new_list = [lists[x] for x in range(0, len(lists)) if lists[x] % 2 != 0]
    # new_list=[x for x in lists[0:7:3]]
    return sorted(new_list, reverse=False)


print(removing_even([2, 1, 3, 4, 5, 6, 7, 8, 9]))
