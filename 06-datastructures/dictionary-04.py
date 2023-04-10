import random

names = ["Olan", "Seen", "Gerrand"]
students_scores = { student: random.randint(1, 100) for student in names }
print(students_scores)

passed_students = { name : score for (name, score) in students_scores.items() if score >= 50  }
print(passed_students)

sentense = "At the end of the war he went into hiding, but was arrested in 1948, tried and sentenced to death."
result = { word : len( word) for word in sentense.replace(",", "").split()}
print(result)


weather_c = {
    "Monday" : 12,
    "Tuesday" : 14,
    "Wednesday" : 15,
    "Thursday" : 14,
    "Friday" : 21,
    "Saturday" : 22,
    "Sunday" : 24,
}

weather_f = { day : (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)
