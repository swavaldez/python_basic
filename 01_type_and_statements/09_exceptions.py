# a dictionary with 3 keys
student = {
    "name" : "Mark",
    "student_id": 15163,
    "feedback": None
}

student["last_name"] = "Kowalski"

try:
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name
except KeyError:
    print("Error finding last_name")
except TypeError:
    print("I can't add these to together")
except Exception:
    print("Uknown error")

print("This code executes")