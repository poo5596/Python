while True:
    print("1. Register")
    print("2. Login")
    choice=int(input("enter your choice"))
    if choice<0 or choice>2:
        print("Invalid Choice")


    w=open("login.txt","r")
    print(w.read())
