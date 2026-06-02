def readfile():
    with open("greeting.txt","r") as file:
        c=file.read()

    print(c)
readfile() 