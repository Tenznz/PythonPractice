# 32. Write a Python program to print a dictionary line by line.

# mydict = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}
#
# for i in mydict.items():
#     print(i)
#
students = {'Aex': {'class': 'V',
                    'rolld_id': 2},
            'Puja': {'class': 'V',
                     'roll_id': 3}}

# for k, v in students.items():
#     print(k)
#     for ik, iv in v.items():
#         print(f'{ik} {iv}')

for a in students:
    print(a)
    for b in students.get(a):
        print(b, ':', students.get(a).get(b))
