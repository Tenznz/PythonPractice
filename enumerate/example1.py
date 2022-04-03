
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
print(obj1)

for ele in enumerate(l1):
    print(ele)
    print(type(ele))


for ele in l1:
    print(ele)
    print(type(ele))

# print("Return type:", type(obj1))
print(list(enumerate(l1)))
print(dict(enumerate(l1)))

# changing start index to 2 from 0
# print(list(enumerate(s1, 2)))