x, y = 5, 11
print(x, y)

x, y = (5, 11)
print(x, y)

my_dict = {"name": "Bob", "age": 25}
x, y = my_dict
print(x, y)
x, y = my_dict.values()  # "Bob", 25
print(x, y)


example_list = ["A", "B", "C"]

for counter, letter in enumerate(example_list):
    print(counter, letter)

people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")
