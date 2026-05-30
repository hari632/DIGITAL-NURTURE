def individualshare(bill,people):
    if(bill<0 and people<=0):
        print("Invalid")
        return
    share=bill//people
    print(f"bill:{bill}")
    print(f"people:{people}")
    print(f"Share:{share}")
x=1250
y=4
individualshare(x,y)
    