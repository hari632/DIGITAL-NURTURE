def add(x,y):
    if x<0 and y<0:
        print("INVALID NUMBER")
        return
    add=x+y
    print(f"Addition of two numbers:{add}")
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
add(a,b)    