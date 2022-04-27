# from random import random
#
# names = ['john', 'Bob', 'Mosh', 'Sarah', 'Mary']
#
# print(names[:])
# print(names[0])
# print(names[0:1])
# print(names[-1])
# print(names[2:])
# print(names[2:3])
#
# # find largest number
#
# num = [i for i in range(1, 100)]
# print(num)
# print(max(num))
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 5],
#     [7, 8, 9]
# ]
# print(matrix[0])
#
# for row in matrix:
#     for item in row:
#         print(item)


num = [2, 3, 41, 6, 3, 2]
print(num)
num.append(8)
print(num)
num.extend([12, 3])
print(num)
num.insert(0, 4)
print(num)
# num.remove(2)
# print(num)
# num.clear()
# print(num)
num.pop()
print(num)

print(num.index(2))
print(50 in num)
print(num.count(2))
num.sort()
print(num)
num.reverse()
print(num)
copy_num = num.copy()
print(copy_num)

# write a program remove the duplicate in list
nums = [2, 3, 8, 6, 3, 2, 6]

unique = []
for num in nums:
    if num not in unique:
        unique.append(num)
print(unique)
