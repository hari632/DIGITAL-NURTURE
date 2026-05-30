def grade(marks):
    if marks<=0:
        print("INVALID INPUT")
    elif marks>=80:
        print("A")
    elif marks>=40 and marks<80:
        print("B")
    else:
        print("C")
mark=88
grade(mark)               


