import ctypes
import os

dirname, filename = os.path.split(os.path.abspath(__file__))

# Load the DLL
mylib = ctypes.CDLL(f"{dirname}/hello-world-x64.dll")


mylib.MessageBoxThread()