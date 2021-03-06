# DICTIONARY
dict = { 1 : 'apple', 2 : 'ball', "name" : "olan" }

print(dict)
print(dict["name"])
print(dict.get("name"))

dict["name"] = "somchai"
dict["fdsfdfa"] = "somchai"
print(dict)
dict.update({ "fdsfs" : "somchai 2" })
print(dict)

del dict["fdsfdfa"]
print(dict)
str = dict.pop("fdsfs")
print(dict, str)
str2 = dict.popitem()
print(dict, str2)

dict.clear()
print(dict)