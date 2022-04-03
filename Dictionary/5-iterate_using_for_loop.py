# 5. Write a Python program to iterate over dictionaries using for loops.

def display_dict(dict_data):
    for i in dict_data:
        print("key : ", i, "\tValue : ", dict_data.get(i))


dict_data = {
    1: 10,
    2: 20,
    3: 30,
    4: 40,
    5: 50
}
display_dict(dict_data)
