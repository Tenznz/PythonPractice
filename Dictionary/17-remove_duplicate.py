# Write a Python program to remove duplicates from Dictionary.

def remove_duplicate(data_dict):
    res = dict()
    for key, value in data_dict.items():
        if value not in res.values():
            res.update({key: value})
    return res


student_data = {'id1':
                    {'name': ['Sara'],
                     'class': ['V'],
                     'subject_integration': ['english, math, science']
                     },
                'id2':
                    {'name': ['David'],
                     'class': ['V'],
                     'subject_integration': ['english, math, science']
                     },
                'id3':
                    {'name': ['Sara'],
                     'class': ['V'],
                     'subject_integration': ['english, math, science']
                     },
                'id4':
                    {'name': ['Surya'],
                     'class': ['V'],
                     'subject_integration': ['english, math, science']
                     },
                }
print(remove_duplicate(student_data))
