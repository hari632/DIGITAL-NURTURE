def marks(x):
    if x<0 and x>100:
        print("INVALID MARK")
        return
    if x>=40:
        print("PASS")
mark=75
marks(mark)