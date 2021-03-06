import os
import json

with open("students.json", "r+t") as f : 
    render = json.load(f)

    for i in range(2) : 
        name = input("name = ")
        sex = input("sex = ")
        gpa = float(input("gpa = "))
        render["students"].append({ "name" : name, "sex": sex, "gpa" : gpa })

    # print(render["students"])
    f.seek(0)
    f.write(json.dumps(render, indent=4))
    f.truncate()
    



    




