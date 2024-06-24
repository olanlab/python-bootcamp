# Install Cython
pip install cython

# Compile the Code
python setup.py build_ext --inplace

# Rename the Output (Optional)
mv example.cpython-38-darwin.so example.dylib
