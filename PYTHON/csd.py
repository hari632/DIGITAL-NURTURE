import csv

def read_students():

    with open("students.csv", "r") as file:

        reader = csv.reader(file)

        next(reader) 

        for row in reader:
            print(f"Name: {row[0]}, Salary: {row[1]}")


read_students()