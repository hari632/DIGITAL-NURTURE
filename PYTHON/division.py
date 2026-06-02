def divide(x,y):
    try:
        result=x/y
        print("Result :",result)
    except ZeroDivisionError:
        print("Cannot Divide by zero")
divide(10,0) 
divide(10,5)       
            