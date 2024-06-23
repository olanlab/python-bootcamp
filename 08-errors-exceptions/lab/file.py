try:
    with open("file.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print("An error occurred:", e)