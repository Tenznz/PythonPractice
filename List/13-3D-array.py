# Write a Python program to generate a 3*4*6 3D array whose each element is *.


# array = [[[col for col in range(6)] for col in range(4)] for row in range(3)]
# print(array)
def create3Darray(x, y, z):
    arr = [[['*' for i in range(x)] for j in range(y)] for i in range(z)]
    return arr


# print(create3Darray(3, 4, 5))
print([i for i in range(5)])
