import os

# GET CURRENT WORKING DIRECTORY
print(os.getcwd())

# CHANGE DIRECTORY
os.chdir("..")
print(os.getcwd())

# LIST FILES AND DIRECTORIES
print(os.listdir())

# CHECK DIRECTORY
print(os.path.isdir("demo234"))

# GET THE ABSOLUTE PATH OF THE CURRENT FILE
current_file_path = os.path.abspath(__file__)
print(current_file_path)

# GET THE DIRECTORY OF THE CURRENT FILE
current_directory = os.path.dirname(current_file_path)
print(current_directory)

dirname, filename = os.path.split(os.path.abspath(__file__))
print(f"{dirname} : {filename}")



