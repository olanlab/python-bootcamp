# BEFORE
number = 10
point = 12.50
name = "Olan Samritjiarapon"
active = True

# LIST
numbers = [1, 2, 3, 4, 5]
points = [10.5, 88.5, 99.60]
names = ["olan", "kimmy", "gerrand"]
actives = [True, False]

# ACCESS
print(numbers[2])
print(numbers[-3])
print(numbers[4])
print(numbers[-1])
print(numbers)
print(numbers[:3])

# CHANGE
numbers[2] = 30
print(numbers)

numbers[3:5] = [40, 50]
print(numbers)

# ADD AND REMOVE
numbers.append(60)
print(numbers)

numbers.extend([70, 80, 90])
print(numbers)

numbers = numbers + [100]
print(numbers)

del numbers[6]
print(numbers)
print(numbers[6])
del numbers[6:8]
print(numbers)