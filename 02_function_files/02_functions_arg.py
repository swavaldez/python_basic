students = []

def get_students_titlecase():
    students_titlecase =[]
    for student in students:
        students_titlecase = student.title()
    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

# optional parameters
def add_student(name, student_id = 0):
    student = {"name": name, "student_id": student_id}
    students.append(student)
    students.append(name)
# named parameters
add_student(name = "Mark", student_id = 332)
add_student("Sherwin", 335)
add_student("Chabby", 336)
add_student("Joshua")

# n number of arguments
def var_args(name, *args):
    print(name)
    print(args)

var_args("Sherwin", "Yes", "NO", 23, 45)

# n number of arguments dictionary
def var_args_kw(name, **kwargs):
    print(name)
    print(kwargs["description"], kwargs["feedback"])

var_args_kw("Sherwin", description="Loves Python", feedback=None, pluralsight_subscriber=True)

