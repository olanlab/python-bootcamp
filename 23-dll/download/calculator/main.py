import ctypes
import os 

dirname, filename = os.path.split(os.path.abspath(__file__))


# Load the DLL
mylib = ctypes.CDLL(f"{dirname}/mylib.dll")

# Define the argument and return types of the function
mylib.add.argtypes = (ctypes.c_int, ctypes.c_int)
mylib.add.restype = ctypes.c_int

# Call the function
result = mylib.add(3, 4)
print(f"The result is: {result}")
