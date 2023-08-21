import numpy as np

# Create an array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Transpose of the array
transposed_arr = np.transpose(arr)
print("Transposed array:")
print(transposed_arr)

# Flatten the array
flattened_arr = arr.flatten()
print("Flattened array:")
print(flattened_arr)

# Reshape the array
reshaped_arr = arr.reshape(1, 9)
print("Reshaped array:")
print(reshaped_arr)