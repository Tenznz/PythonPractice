# 33. Write a Python program to check multiple keys exists in a dictionary.

student = {
    'name': 'Alex',
    'class': 'V',
    'roll_id': '2',
    '': ''
}
s = {}

print(student.keys() >= {'class', 'name'})
print(student.keys() >= {'name', 'Alex'})
print(student.keys() >= {'roll_id', 'name'})

print(s.keys() >= {'name'})
