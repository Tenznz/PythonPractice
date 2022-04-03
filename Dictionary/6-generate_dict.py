# 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n)
# in the form (x, x*x).

# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

def generate_dict(num):
    dic = dict()
    for i in range(1, num + 1):
        dic.update({i: i * i})
    return dic


print(generate_dict(5))
