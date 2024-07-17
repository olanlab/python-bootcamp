from setuptools import setup, Extension
from Cython.Build import cythonize
import os

# Define the extension
ext = Extension(
    name="dll",
    sources=["dll.pyx"],
    language="cpp"
)

# Compile the extension
setup(
    name="dll",
    ext_modules=cythonize([ext]),
)

# # Rename the .pyd file to .dll (Windows specific)
# output_name = "dll.cp{0}{1}-win_amd64.pyd".format(*os.sys.version_info[:2])
# if os.path.exists(output_name):
#     os.rename(output_name, "dll.dll")