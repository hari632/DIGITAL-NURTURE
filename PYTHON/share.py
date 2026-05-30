def individualshare(bill,people):
    if(bill<0 and people<=0):
        print("Invalid")
        return
    share=bill//people
    print(f"bill:{bill}")
    print(f"people:{people}")
    print(f"Share:{share}")
x=int(input("Enter the total amount: "))
y=int(input("Enter the people: "))
individualshare(x,y)
    