# 2. Write a Python script to add a key to a dictionary.
#
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

def addkey(dict_data, key, value):
    dict_data.update({key: value})
    return dict_data


# data = dict()
data = {0: 10, 1: 20}
key = int(input("Enter key : "))
value = int(input("Enter value : "))
print(addkey(data, key, value))
