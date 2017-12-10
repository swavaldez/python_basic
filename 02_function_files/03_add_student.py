students = []

def get_students_titlecase():
    students_titlecase =[]
    for student in students:
        students_titlecase = student["name"].title()
    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

def add_student(name, student_id = 332):
    student = {"name": name, "student_id": student_id }
    students.append(student)

student_list = get_students_titlecase()

student_name = input("Enter student name:")
student_id = input("Enter student ID:")
add_student(student_name, student_id)
want = "yes"

while want == "yes":
    want = input ("Do you want to add more student? [yes:no]")
    if want == "yes":    
      student_name = input("Enter student name:")
      student_id = input("Enter student ID:")
      add_student(student_name, student_id)
    else:
        break
      
print_students_titlecase()

for student in students:
    print("student: {0}, {1}".format(student["name"], student["student_id"]))