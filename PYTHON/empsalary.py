class employee:
    def __init__(self,name):
        self.name=name
        self.salary=0
    def setsalary(self,salary):
         self.salary=salary
         return self  
    def raisesalary(self,amount):
        self.salary +=amount
        return self
    def display(self):
        print("Name: ",self.name)
        print("amount:",self.salary)
        
        return self
x=employee("Hari")
x.setsalary(50000).raisesalary(20000).display()    
        