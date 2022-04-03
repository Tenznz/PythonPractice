# 3. Write a Python script to concatenate following dictionaries to create a new one.
#
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def concatenate(dict1, dict2, dict3):
    dict1.update(dict2)
    dict1.update(dict3)
    return dict1


dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

print(concatenate(dic1, dic2, dic3))
