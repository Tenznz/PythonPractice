# 4. Write a Python script to check whether a given key already exists in a dictionary.

def check_duplicate(dict_data, key):
    if key in dict_data:
        return True
    return False


dict_data = {
    1: 10,
    2: 20,
    3: 30,
    4: 40
}
key = 5
print(check_duplicate(dict_data, key))
