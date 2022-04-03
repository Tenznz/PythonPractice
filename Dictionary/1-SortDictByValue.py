import operator

# 1. Write a Python script to sort (ascending and descending) a dictionary by value.

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print("Original: ", d)

sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1)))
# sorted()
print("Dictionary in ascending order by value : ", sorted_d)
sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print('Dictionary in descending order by value : ', sorted_d)

print(operator.itemgetter(1)(d))
