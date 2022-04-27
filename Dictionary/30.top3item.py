# 30. Write a Python program to get the top three items in a shop.
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3

# max = lambda x, y: x if x > y else y

# sample_data = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}
# for i in range(3):
#     max_value = max(sample_data.values())
#     print(max_value)
#     print(sample_data[max_value])
#     key = sample_data[max_value]
#     sample_data.pop(key)

from heapq import nlargest
from operator import itemgetter

mydict = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}
for name, value in nlargest(3, mydict.items(), key=itemgetter(1)):
    print(name, value)
