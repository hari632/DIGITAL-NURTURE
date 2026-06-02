from datetime import datetime

class Task:

    def __init__(self, name, due_date):
        self.name = name
        self.due_date = datetime.strptime(
            due_date,
            "%Y-%m-%d"
        )

tasks = [

    Task("Project", "2026-07-15"),
    Task("Assignment", "2026-07-05"),
    Task("Exam", "2026-07-10")

]

tasks.sort(
    key=lambda task: task.due_date
)

print("Task Schedule")

for task in tasks:
    print(
        task.name,
        task.due_date.date()
    )