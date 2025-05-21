while True:
    Name=input("enter your name:",)
    address=input("enter your address:",)
    print("enter your marks for the given subjects out of 100:")

    maths=int(input("enter maths marks :"))
    if maths<0 or maths>100:
        print("invalid marks")
        continue
    physics=int(input("enter physics marks:"))
    if physics<0 or physics>100:
        print("Invalid marks")
        continue

    Chemistry=int(input("enter chemistry marks:"))
    if Chemistry<0 or Chemistry>100:
        print("Invalid marks")
        continue
    Biology=int(input("enter biology marks:"))
    if Biology<0 or Biology>100:
        print("Invalid marks")
        continue
    English=int(input("enter English marks:"))
    if English<0 or English>100:
        print("Invalid marks")
        continue

    marks=maths+physics+Chemistry+Biology+English
    percentage=((maths+physics+Chemistry+Biology+English)/500)*100
    print("                 Name:",Name)
    print("              Address:",address)
    print("=============================================================")
    print("Subject    |Total marks |obtain marks       |percentage      ")
    print("=============================================================")
    print("maths      |100         |"+str(maths)+"     |            "+str(maths))
    print("physics    |100         |"+str(physics)+"   |            "+str(physics))
    print("Chemistry  |100         |"+str(Chemistry)+" |            "+str(Chemistry))
    print("Biology    |100         |"+str(Biology)+"   |            "+str(Biology))
    print("English    |100         |"+str(English)+"   |            "+str(English))
    print("=============================================================")
    print("Total      |500         |"+str(marks)+"     |            "+str(percentage))
    break;
    
    
