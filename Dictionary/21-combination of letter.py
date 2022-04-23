# 21. Write a Python program to create and display all combinations of letters, selecting each letter
# from a different key in a dictionary.
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd
import itertools


def generate_combination(dict_data):
    for i in itertools.product(*[dict_data[k] for k in sorted(dict_data.keys())]):
        print("".join(i))


if __name__ == "__main__":
    sample_data = {'1': ['a', 'b'], '2': ['c', 'd']}
    generate_combination(sample_data)
