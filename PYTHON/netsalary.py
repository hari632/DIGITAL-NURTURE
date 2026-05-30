def calculatenetsalary(salary,taxrate):
    if(salary<=0):
        print("Invalid salary")
        return
    
    if(taxrate<0 or taxrate>1):
        print("Invalid taxrate")
        return
    taxamount=salary *taxrate
    netsalary=salary-taxamount
    print(f"Salary:{salary:.2f}")
    print(f"taxrate:{taxrate:.2f}")
    print(f"netsalary:{netsalary:.2f}")
salary=75000.5
taxrate=0.18
calculatenetsalary(salary,taxrate)