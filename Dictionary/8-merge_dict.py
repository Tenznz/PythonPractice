# 8. Write a Python script to merge two Python dictionaries.

def merge_dict(dict1, dict2):
    dict1.update(dict2)
    return dict1


def merge_dictionaires(*dicts):
    print(type(dicts))
    data_dict = dict()
    for d in dicts:
        data_dict.update(d)
    return data_dict


dic1 = {1: 10, 2: 20, 3: 30}
dic2 = {4: 40, 5: 50, 6: 60}
dic3 = {7: 70, 8: 80, 9: 90}

print(merge_dict(dic1, dic2))
print(merge_dictionaires(dic1, dic2, dic3))
