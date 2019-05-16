import json

x1 = '{ "name":"Olan Samritjiarapon", "age":34, "city":"Bangkok"}'
y1 = json.loads(x1)
print(y1["city"])

x2 = { "name": "Jame", "age": 29, "city": "Trat" }
y2 = json.dumps(x2)
print(y2)


x3 = {
  "name": "Jame",
  "age": 29,
  "married": True,
  "divorced": False,
  "children": ("Kitty","Bally"),
  "pets": None,
  "cars": [
    {"model": "Toyota", "year": 2017},
    {"model": "Honda", "year": 2014}
  ]
}

print(json.dumps(x3))