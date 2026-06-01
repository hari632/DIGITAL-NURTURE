def rectangle(l,b):
    if l<0 and b<0:
        print("INVALID NUMBER")
        return
    area=l * b
    print(f"Arae of rectangle:{area}")
a=int(input("enter the length: "))
b=int(input("enter the breadth: "))
rectangle(a,b)    