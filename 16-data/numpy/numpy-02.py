import numpy as np


# Array arithmetic
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Array addition:", np.add(a, b))
print("Array subtraction:", np.subtract(a, b))
print("Array multiplication:", np.multiply(a, b))
print("Array division:", np.divide(a, b))

c = a + b
print("Addition:", c)
# Element-wise subtraction
d = a - b
print("Subtraction:", d)
# Element-wise multiplication
e = a * b
print("Multiplication:", e)
# Element-wise division
f = a / b
print("Division:", f)