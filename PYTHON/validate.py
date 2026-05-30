def validate(user,password):
    if(user=="" or password==""):
        print("INVALID")
        return
    if(user=="admin"):
        if(password=="pass123"):
            print("LOGIN SUCCESSFULLY")
        else:
            print("UNSUCCESSFULL")
validate("admin","pass123")            
                