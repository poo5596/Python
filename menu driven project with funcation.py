#calculater programm in menu driven by using function
'''

def add(x,y):
    return(x+y)

def sub(x,y):
    return(x-y)

def multi(x,y):
    return(x*y)

def div(x,y):
    return(x/y)


while True:

    print("1.add")
    print("2.sub")
    print("3.multi")
    print("4.div")
    print("5.exit")

    choice=int(input("enter your choice between (1-4):"))
    a=int(input("enter your first value:-"))
    b=int(input("enter your second value:-"))


    if choice==1:
        c=add(a,b)
        print("sum :-",c)

    elif choice==2:
        d=sub(a,b)
        print("sub:-",d)

    elif choice==3:
        e=multi(a,b)
        print("product:-",e)
    elif choice==4:
        f=div(a,b)
        print("div:-",f)

    else:
        print("program Terminating")
        break;

    

'''

'''

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def multi(x,y):
    return (x*y)

def div(x,y):
    if y!=0:
        return x/y
    else:
        return "Error! Division by zero."


while True:
    print("\nSelect Operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")

    choice=int(input("enter your choice(1-5):"))

    if choice==5:
        print("Program Terminating")
        break

    if choice in [1,2,3,4]:
        a=float(input("enter your first value :"))
        b=float(input("enter your second value:"))


        if choice==1:
            result=add(a,b)
            print(f"result:{a}+{b}={result}")


        elif choice==2:
            result=sub(a,b)
            print(f"result:{a}-{b}={result}")

        elif choice==3:
            result=multi(a,b)
            print(f"result:{a}*{b}={result}")

        elif choice==4:
            result=div(a,b)
            print(f"result:{a}/{b}={result}")

    else:
        print("Invalid choice!Please enter a number between 1 and 5.")
            
    






#WAP to SWAP two No's:


def swap(a,b):
    a,b=b,a # a,b=b,a   a--->b    b----->a
    print("after swapping")
    print("a=",a)
    print("b=",b)

x=int(input("enter the first no:-"))
y=int(input("enter the second no:-"))

swap(x,y)
print("x=",x)
print("y=",y)
'''

#variable lengh argument(arbitry aruments):-

def info(s,*names):  #*can store multiple elements
    print("info.about",s)
    for i in names:
        print(i)


info("food","india","italian","mexican")
print("===========")
info("cars","mercidesd","honda")
print("===========")
info("cities","mumbai","london","paries")




def student(a_1,*names):
    print("student name detaisl:",a_1)
    print(type(student))
    for q in names:
        print(q)

student("pooja","remma","seema","ram")
student("rum","raju","r","o","uu")
student("sum","div","you")
        


    





