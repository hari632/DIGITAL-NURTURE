def weight():
    weight=input("Enter the weight:")
    try:
        weight=float(weight)
        
        lbs=weight*2.20462
        print(f"The weight in pounds is:{lbs:.2f}")
        
    except ValueError:
        print("enter the valid weight in kg")
    
    
    
weight()    
    
        
        
        
    