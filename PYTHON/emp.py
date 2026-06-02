class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("Employee name :",self.name)
        print("Salary :",self.salary)
x=employee("Hari",20000)   
y=employee("Dharshini",5000)

x.display()
y.display()         