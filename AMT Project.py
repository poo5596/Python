#ATM Project


Balance=5000
pin=1111
while True:
    print("1.Your Balance\n2.Withdraw\n3.deposit\n4.Change pin\n5.Exit")
    choice=int(input("enter your choice"))

    if choice==1:
        print("Your Balance is:",Balance)

    elif choice==2:
        upin=float(input("enter your pin:"))
        if upin==pin:
            amt=int(input("enter yout withdraw amt:"))
            if amt<=Balance and amt>0 :
                    Balance-=amt
                    print("your transation is succsefully")
                    print("Your new Balance is :",Balance)
           
            else:
                print("Insuffienct Balance  or value entered is negative ")
                
        else:
            print("Incorrect Pin")
    elif choice==3:
        upin=float(input("enter your pin:"))
        if upin==pin:
            deposit_amt=float(input("enter your deposit amt"))
            Balance+=deposit_amt
            print("Your amt is credited succesfully")
            print("Your new Balance is:",Balance)
        else:
            print("Incorrect pin")
    elif choice==4:
        upin=(input("enter your current pin:"))
        if upin==pin:
                 Newpin=int(input("enter your new pin:"))
                 Newpin1=int(input("enter your new pin again:"))
                 if Newpin==Newpin1:
                     pin=Newpin
                     print("your pin genrated succsefully")
                 else :
                     print("your pin not match")
                    
        else:
            print("Your Current pin not match, Try again!!!")
    elif choice==5:
        choice=float(input("do you really want to exit(1 for yes / 0 for no)"))
        if choice==1:
            print("exit")
            break;
        else:
            continue;
    

    else:
        print("Invalid number")


        
    
            

                 
            
