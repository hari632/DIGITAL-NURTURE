def highlow(salary):
    if not salary:
        print("empty list")
        return
    high=max(salary)
    low=min(salary)
    print(f"Highest Salary: {high}")
    print(f"Lowest Salary: {low}")
salary= [50000, 75000, 62000, 95000]
highlow(salary)  