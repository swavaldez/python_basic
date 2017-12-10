students = []

def get_students_titlecase():
    students_titlecase =[]
    for student in students:
        students_titlecase = student.title()
    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

def add_student(name):
    students.append(name)

add_student("Mark")
add_student("Sherwin")
add_student("Chabby")
add_student("Joshua")

student_list = get_students_titlecase()

print_students_titlecase()