# import itertools
#
# dict_data = {'1': ['a', 'b'], '2': ['c', 'd']}
# print(*[dict_data[k] for k in sorted(dict_data.keys())])
# # for i in itertools.cycle(dict_data.items()):
# #     print(i)
import itertools

# for in loop
for i in itertools.count(5, 5):
    if i == 100:
        break
    else:
        print(i, end=" ")
