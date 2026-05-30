def nextage():
    age=input("Enter the age: ")
    if not age.isdigit():
        print("Enter the valid number")
        return
    age=int(age)
    print(f"Next year age:{age+1}")
nextage()
    