import os


dirname, filename = os.path.split(os.path.abspath(__file__))

try:
    with open(f"{dirname}/demo.txt", "rt") as f:
        print(f.read())

        # ERROR
        # number = 10 / 0
        print("************")

except FileNotFoundError:
    print("demo.txt is not exist.")
except FileExistsError:
    print("demo.txt is exist.")
except Exception as e:
    print(e)

