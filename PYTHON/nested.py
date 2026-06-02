def get_salary(employees, department, employee_name):

    
    if department not in employees:
        print("Department not found")
        return

    if employee_name not in employees[department]:
        print("Employee not found")
        return

    salary = employees[department][employee_name]

    print(f"{employee_name}'s Salary: ₹{salary}")


employees = {
    "IT": {
        "Hari": 50000,
        "Rahul": 60000
    },
    "HR": {
        "Priya": 45000,
        "Anu": 55000
    }
}

get_salary(employees, "IT", "Hari")