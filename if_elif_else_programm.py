
#menu driven programms

while True:
    print("1.addition\n2.substraction\n3.multiplication\n4.division\n5.exit")
    a=int(input("enter your choice:"))
    if a==1:
        b=int(input("enter 1st no.:"))
        c=int(input("enter 2nd no."))
        print(b+c)
    elif a==2:
        b=int(input("enter the 1st no.:"))
        c=int(input("enter the 2nd no."))
        print(b-c)
    elif a==3:
        b=int(input("enter the 1st no.:"))
        c=int(input("enter the 2nd no."))
        print(b*c)
    elif a==4:
        b=int(input("enter the 1st no.:"))
        c=int(input("enter the 2nd no."))
        print(b/c)
    elif a==5:
        choice=int(input("do you want to really exit?(1 for yes/0 for no)"))
        if choice==1:
            print("exit")
            break
        else:
            continue
    else:
        print("invaild number")
        
'''area of circle= IIr2
    area of triangle=1/2*base*height
    area of rectangle=length*width
    area of square=square*square
    area of parallelogram=base*height'''

while True:
    print("1.area of circle\n2.area of rectangle\n3.area of square\n4.area of triangle\n5.area of parallelogram\n6.exit")
    x=int(input("enter you choice"))
    if x==1:
        y=int(input("enter the pie value:-"))
        z=12.56
        print(y**z)

    elif x==2:
        y=int(input("enter the length:-"))
        z=int(input("enter the width:-"))
        print(y*z)

    elif x==3:
        y=int(input("enter the square value :-"))
        print(y*y)

    elif x==4:
        y=float(input("enter the base value :-"))
        z=float(input("enter the height value :-"))
        print(float(1/2*y*z))

    elif x==5:
        y=int(input("enter the base value :-"))
        z=int(input("enter the height value :-"))
        print(y*z)

    elif x==6:
        choice=int(input("do you want to really exit?(1 for yes / 0 for no)"))
        if choice==1:
            print("exit")
            break
        else:
            continue
    else:
        print("invalid number")
                
            
    
