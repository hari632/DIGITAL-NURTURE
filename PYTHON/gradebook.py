import json

students = {}

def add_grade(name, grade):

    if grade < 0 or grade > 100:
        print("Invalid Grade")
        return

    students.setdefault(name, []).append(grade)

def calculate_gpa(name):

    grades = students.get(name, [])

    if grades:
        return sum(grades) / len(grades)

    return 0

def class_average():

    all_grades = []

    for grades in students.values():
        all_grades.extend(grades)

    return sum(all_grades) / len(all_grades)


add_grade("Hari", 90)
add_grade("Hari", 80)
add_grade("Rahul", 85)

print("Hari GPA:", calculate_gpa("Hari"))

print("Class Average:", class_average())