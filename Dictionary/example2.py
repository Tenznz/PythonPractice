# 2. Write a Python script to add a key to a dictionary.
#
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

sample = {0: 10, 1: 20}
print("original : ", sample)

sample.update({2: 30})
print("insertion After using update({2:30})")
print(sample)

sample[3] = 40
print("insertion After using sample[3]=40")
print(sample)

sample[2] = 50
print("for update, After using sample[2]=50")
print(sample)


sample.update({3: 60})
print("for update, After using sample.update({3:50})")
print(sample)

# insert dictionary
newsample = {"2": 3, "4": 5, "1": 3}
sample.update(newsample)
print(sample)

# Delete
sample.pop(2)
print("After using pop(2)")
print(sample)

print(set(sample.items()))