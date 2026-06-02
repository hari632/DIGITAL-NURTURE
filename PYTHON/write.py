def writefile():
    with open("greeting.txt","w") as file:
        file.write("Hello Evevryone")
    print("Succesful")
writefile()        