class employee:
    def work(self):
        print("employee is working")
class developer(employee):
    def work(self):
        print("Developer is working")
class working(employee):
    def work(self):
        print("working time is 10 am")
class parttime(employee):
    def work(self):
        print("Part time job is available")
employees=[developer(),working(),parttime()]
for emp in employees:
    emp.work()                                