# 18. Write a Python program to check a dictionary is empty or not.
def is_dict_empty(dict_data):
    # print(bool(dict_data))
    if not bool(dict_data):
        return True
    return False


if __name__ == "__main__":
    dict_data = {}
    print(is_dict_empty(dict_data))
    dict_data.update({"a": 1})
    print(is_dict_empty(dict_data))
