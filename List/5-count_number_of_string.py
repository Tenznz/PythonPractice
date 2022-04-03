# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and
# last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba','1221']
# Expected Result : 2

def count_str_with_same_last_char(data_list):
    count = 0
    for i in data_list:
        list_item = list(i)
        num_list = len(list_item)
        if num_list >= 2 and list_item[0] == list_item[num_list-1]:
            print(i)
            count = count + 1
    return count


data_list = ['abc', 'xyz', 'aba', '1221']
print(count_str_with_same_last_char(data_list))
