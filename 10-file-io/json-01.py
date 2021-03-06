import os
import json

with open("students.json", "wt") as f : 
    render = json.load(f)
    
    # print(render["students"])
    for row in render["students"] :
        print(row.get('gpa'))

    print(render["max-gpa"])
    print(render["min-gpa"])