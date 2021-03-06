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