import math
def area(radius):
    radius=float(radius)
    if radius<0:
        print("INVALID NUMBER")
        return
    area= math.pi * radius * radius
    print(f"Area of circle: {area:.2f}")
area(17.6)    
        