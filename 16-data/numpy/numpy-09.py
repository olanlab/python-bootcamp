import numpy as np

# Create a Python function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Apply the function to a NumPy array
arr = np.array([-1, 0, 1])
result = sigmoid(arr)
print("Result:")
print(result)