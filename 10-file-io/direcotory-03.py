import os

# GET ENVIRONMENT VARIABLE
home_dir = os.getenv('HOME', '/')
print(f"Home Directory: {home_dir}")
print(f"Home Directory: {os.environ['HOME']}")

# EXECUTE A SYSTEM COMMAND
os.system('ping olanlab.com')
