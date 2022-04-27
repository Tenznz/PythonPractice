# 34. Write a Python program to count number of items in a dictionary value that is a list.

mydict = {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']}
print(len([value for value in mydict.values()]))

dict = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
ctr = sum(map(len, dict.values()))
print(ctr)
