# 25. Write a Python program to print a dictionary in table format

my_dict = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}
for row in zip(*([key] + value for key, value in sorted(my_dict.items()))):
    print(*row)

print(([key]+value for key, value in sorted(my_dict.items())))
# a = (1, 2, 3, 4, 5, 6, 6)
# print(*a)
print(sorted(my_dict.items()))