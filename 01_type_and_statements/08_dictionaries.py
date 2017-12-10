# a dictionary with 3 keys
student = {
    "name" : "Mark",
    "student_id": 15163,
    "feedback": None
}

# a list of dictionary
all_students = [
    {"name": "Mark", "student_id": 15163},
    {"name": "Katarina", "student_id": 63112},
    {"name": "Jessica", "student_id": 30021}
]

print(student["name"])
# below will show KeyError exception
# print(student["last_name"])

# safe to get uknown keys
print(student.get("last_name", "Uknown"))

# show all values
print(student.values())

# delete item in a dictionary
del student["name"]