import numpy as np

# Create a 2-dimensional array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Boolean indexing
mask = arr > 5
filtered_arr = arr[mask]
print("Filtered array:")
print(filtered_arr)

# Fancy indexing
row_indices = np.array([0, 2])
col_indices = np.array([1, 2])
selected_elements = arr[row_indices, col_indices]
print("Selected elements:")
print(selected_elements)