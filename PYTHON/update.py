def updatedict(emp1,emp2):
    if not isinstance(emp1,dict) or not isinstance(emp2,dict):
        print("INVALID NUMBER")
        return
    emp1.update(emp2)
    print("Updated list")
    print(emp1)
emp1={
    "name":"Hari",
    "age":20
}
emp2={
    "department":"Information technology",
    "sem":6
}  
updatedict(emp1,emp2)
  