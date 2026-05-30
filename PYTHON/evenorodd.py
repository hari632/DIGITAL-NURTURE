def evenorodd(x):
    if(x<0):
        print("Invalid number")
        return
    if(x%2==0):
        print("Even number")
    else:
        print("odd number")
y=int(input("Enter the number"))
evenorodd(y)            