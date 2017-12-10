def get_students():
    students = ["mark", "james"]
    def get_student_titlecase():
        student_titlecase = []
        for student in students:
            student_titlecase.append(student.title())
        return student_titlecase

    student_titlecase_names = get_student_titlecase()
    print(student_titlecase_names)

get_students()