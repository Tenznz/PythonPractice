# 20. Write a Python program to print all unique values in a dictionary.
# Sample Data :
# [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

def get_unique_value(list_dict):
    return set(val for dic in list_dict for val in dic.values())


if __name__ == "__main__":
    sample_data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
                   {"VIII": "S007"}]
    print(get_unique_value(sample_data))
