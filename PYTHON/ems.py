import json

class Employee:

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Salary: ₹{self.salary}"


employees = {}

employees["E101"] = Employee("E101", "Hari", 50000)
employees["E102"] = Employee("E102", "Rahul", 60000)

# Save to JSON
data = {}

for emp_id, emp in employees.items():
    data[emp_id] = {
        "name": emp.name,
        "salary": emp.salary
    }

with open("emps.json", "w") as file:
    json.dump(data, file, indent=4)

print("Employee data saved!")

# Load from JSON
with open("emps.json", "r") as file:
    loaded_data = json.load(file)

print("\nLoaded Employees:")

for emp_id, details in loaded_data.items():
    print(f"ID: {emp_id}, Name: {details['name']}, Salary: ₹{details['salary']}")