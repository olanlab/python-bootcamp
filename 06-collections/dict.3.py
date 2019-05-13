dict =	{
  "firstname": "Olan",
  "lastname": "Samritjirapon",
  "hp": 100,
  "mp": 50
}

# ADD
dict["job"] = "knight"
print(dict)



# REMOVE
dict.pop("mp")
print(dict)

dict.popitem()
print(dict)

del dict["lastname"]
print(dict)

dictcopy = dict.copy()
dict.clear()
print(dict, dictcopy)

# del dict
# print(dict)