def marks(x):
    if x<0 and x>100:
        print("INVALID MARK")
        return
    if x>=40:
        print("PASS")
    if x<40:
        print("FAIL")    
mark=75
marks(mark)