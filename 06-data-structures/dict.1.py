dict =	{
  "firstname": "Olan",
  "lastname": "Samritjirapon",
  "hp": 100,
  "mp": 50
}
print(dict)
print(dict["hp"])
print(dict.get("hp"))

dict["hp"] = 200
dict.update({ "mp": 75 })
print(dict)

print(len(dict))

if "hp" in dict:
  print("Yes, 'hp' is one of the keys in dict.")