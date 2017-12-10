number = 6
if number == 5:
    print("number is 5")
else:
    print("number is NOT 5")

if number:
    print("Number is defined and truthy")

text = "Python"
if text:
    print("Text is defined and truthy")

python_course = True
if python_course:
    print("This will execute")

aliens_found = None # None is equal to null in other language
if aliens_found:
    print("This will NOT execute")

if not python_course: # Not condition
    print("This will also not execuite")

#Use and & or in the codition
if number == 6 and python_course:
    print("This will execcute")

if number == 17 or python_course:
    print("This will also execute")

# Ternary if statement
a = 1
b = 2
ternary_message = "bigger" if a < b else "smaller"
print(ternary_message)

