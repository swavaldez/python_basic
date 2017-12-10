# student_names = []
student_names = ["Mark", "Katarina", "Jessica", "Sherwin"]
print(len(student_names))

# for loops
for name in student_names:
    print("Student name is {0}".format(name))

# for range
x = 0
for index in range(10):
    x += 10
    print("The value of x is {0}".format(x))

# start in 5 and ends in 9
for index in range(5, 9):
    x += 10
    print("The value of x is {0}".format(x))

# index increase by 2
for index in range(5, 9, 2):
    x += 10
    print("The value of x is {0}".format(x))

for index in range(len(student_names)):
    print("Student name is {0}".format(student_names[index]))

    