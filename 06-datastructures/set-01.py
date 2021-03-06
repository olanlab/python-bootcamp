cars = {"mini cooper", "honda", "toyota", "toyota"}
print(type(cars))

print(cars)

# ADD
cars.add("bmw")
print(cars)

cars.update(["ford", "nissan"])
print(cars)

# REMOVE
cars.remove("nissan")
print(cars)

cars.discard("bmw")
print(cars)

car = cars.pop()
print(car, cars)

cars.clear()
print(cars)