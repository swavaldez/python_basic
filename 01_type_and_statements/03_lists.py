# student_names = []
student_names = ["Mark", "Katarina", "Jessica"]

print(student_names[0])
print(student_names[2])
print(student_names[-1]) #accessing last value in the lists

student_names.append("Sherwin")
print(student_names[-1]) 

# check if sherwin is in the lists
if("Sherwin" in student_names):
    print("Sherwin is in the lists")

# count
print("The length of the list is {0}".format(len(student_names)))

#delete item in the lists
del student_names[2]

print("after deletion: ")
print(student_names[0])
print(student_names[1])
print(student_names[2])

#slicing, skip first element
print(student_names[1:])
